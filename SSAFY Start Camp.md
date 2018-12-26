# SSAFY Start Camp 챗봇 퀘스트

[광주_1_이지선, https://github.com/wiahawm/Telegrame-chatbot](https://github.com/wiahawm/Telegrame-chatbot)

## I. 스펙(Specification)

------

### 구현된 어플리케이션의 주요 기능

- 사용자가 Telegram을 통해 챗봇에게 전송한 데이터를 분석한다.

- 데이터가 Text일 경우,

  1. 번역 Content

     : Content를 Naver API Papago를 통해 번역

  2. 메뉴

     : menu list에서 랜덤으로 하나의 값을 꺼내서 추천

  3. 로또

     : 로또 번호를 랜덤으로 뽑아서 추천

  4. 오늘 날짜

     : 오늘 날짜를 보여줌


- 데이터가 Photo일 경우,

  1. 사진 판별

     : Naver API Clova를 이용하여 Celebrity(유명인)라면 파악하여 일치성과 해당 이름을 나타냄(이름만 나타내게 함) 

## II. 회고(Retrospective)

------

어플리케이션 구현 과정에서의 어려움과 문제점

- 보안상 크롤링을 일반적인 방법으로 접근할 수 없게 만든 사이트가 있어서 어려움이 있었다.

### III. 보완 계획(Feedback)

------

현재 미완성이지만 추가로 구현할 기능 및 기존 문제점 보완 계획

#### (1) 남은 시간 알려주는 기능

- 집에 가기까지 남은 시간을 알려주는 기능을 개발하고 싶다.
- 현재시간에서 오후6시까지 남은 시간을 알려주는 부분의 기능을 추가적으로 개발하고 싶다.



#### (2) 사진 기능

- 여러명인 사진을 올리면 모든 사람의 이름을 나타낼 수 있게 만들고 싶다.