from flask import Flask, request
import os
from pprint import pprint as pp
import requests
import random
from datetime import date, timedelta
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
api_url = 'https://api.hphk.io/telegram'
token = os.getenv('TELE_TOKEN')

@app.route(f"/{token}",methods=['POST'])
def telegram():
    #naver api를 사용하기 위한 변수
    naver_client_id = os.getenv('NAVER_ID')
    naver_client_secret = os.getenv('NAVER_SECRET')
    
    #tele_dict = 데이터 덩어리
    tele_dict = request.get_json()
    pp(request.get_json())
    
    #유저정보
    chat_id = tele_dict['message']['from']['id']
    # print(chat_id)
    
    #유저가 입력한 데이터
    text = tele_dict.get('message').get('text')
    # print(text)
    
    tran = False
    img = False
    
    # 사용자가 이미지를 넣었는지 체크
    if tele_dict.get('message').get('photo') is not None:
        img = True
    
    # text(유저가 입력한 데이터) 제일 앞 두 글자가 번역인지 확인
    else :
        if text[:2]=="번역":
            # 번역 안녕하세요
            tran = True
            text = text.replace(text[:3],"")
         
            print(text)
            # 안녕하세요
    
    # 번역 안녕하세요 => 번역하는 조건문 작성
    if tran:
        papago = requests.post("https://openapi.naver.com/v1/papago/n2mt",
                    headers = {
                        "X-Naver-Client-Id":naver_client_id,
                        "X-Naver-Client-Secret":naver_client_secret
                    },
                    data = {
                        'source':'ko',
                        'target':'en',
                        'text':text
                    }
        )
        trans = papago.json()
        text = trans['message']['result']['translatedText']
    
    elif img:
        text="사용자가 이미지를 넣었어요."
        
        #텔레그렘에게 사진정보 가져오기
        file_id = tele_dict['message']['photo'][-1]['file_id']
        file_path = requests.get(f"{api_url}/bot{token}/getFile?file_id={file_id}").json()['result']['file_path']
        file_url = f"{api_url}/file/bot{token}/{file_path}"
        print(file_url)
        #사진을 네이버 유명인 인식 api로 넘겨주기
        file = requests.get(file_url, stream=True)
        clova = requests.post("https://openapi.naver.com/v1/vision/celebrity",
                    headers = {
                        "X-Naver-Client-Id":naver_client_id,
                        "X-Naver-Client-Secret":naver_client_secret
                    },
                    files = {
                        'image':file.raw.read()
                    }
        )
        
        # 가져온 데이터 중에서 필요한 정보 빼오기
        pp(clova.json())
        # 인식이 되었을 때
        if clova.json().get('info').get('faceCount'):
            text = clova.json()['faces'][0]['celebrity']['value']
        else:
            text="사람얼굴이 아니에요ㅠㅠ"
        
        # 인식이 되지 않았을 때
        
        
    elif text=="메뉴":
        menu_list = ["한식","중식","양식","분식","선택식"]
        text = random.choice(menu_list)
    elif text=="로또":
        num_list = range(1,46)
        text = random.sample(num_list,6)
        text.sort()
        
    elif text=="오늘 날짜":
        today=date.today()
        text=today.isoformat()
    # elif text=="언제 집에가":
    #     now=datetime.now()
    #     at = time(18,00,00)
    #     at_time = at.hour, at.minute, at.second
    #     text = at_time-now
        
        
    
    #유저에게 그대로 돌려주기
    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
    return '', 200
    
app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))