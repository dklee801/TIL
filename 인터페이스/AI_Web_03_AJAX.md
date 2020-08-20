## AJAX

- 서버가 제공하는 데이터를 받아서 그 데이터를 이용해서 화면을 제어해야함.

- 서버로부터 데이터를 받아오는 방법 > AJAX처리

- AJAX는 JavaScript가 가지고 있는 서버와의 비동기 통신방법.

  ###### 동기 방식 : 프로그램적으로 처리가 쉬움,but 비효율적

  ##### 비동기 방식 : 프로그램적 처리가 어려움.

  ##### 						이벤트 처리방식(서버를 기다리지않고 다른 작업.. 효율적.

  #####  

AJAX로 서버와 통신해서 서버가 보내준 데이터를 받아서 화면처리를 진행.

- 서버는 어떤 형식의 데이터를 보내주는가?

  1. CSV (Comma Seperated Value)

     예: 홍길동,20,서울,김길동,서울,30,,,,,

     - 장점 : 많은 양의 데이터를 처리하기에 적합

       ​			가적인 데이터가 `,` 만 이용하기 때문에 상대적으로 적음.

     - 단점 : 데이터 구조를 표현하기 쉽지않음. 데이터가 변경되면 데이터를 사용하는 프로그램을 같이 변경해줘야함. 유지보수 문제가 발생

     

  2. XML (eXtended Markup Language)

     예 : <name>홍길동</name><age>20<age/><address> 서울</address>

     장점 : 데이터 구조를 표현하기 좋음. 사용하기 좋음

     단점 : 부가적인 데이터가 너무 많음. 데이터가 커지면 네트워크를 이용해서 전송하기 힘듦.

     => 90~2000년대 초 많이 사용.

     

  3. JSON(JavaScript Objet Notation)

     예: {name : "홍길동", age:20,address: "서울"}

     - 데이터를 표현하는 표현법.
     - 문자열

     1. 서버쪽 프로그램이 필요

        - 클라이언트에게 HTML.JavScript로 되어 있는 page가 전송
        - 클라이언트는 이 page에 있는 버튼을 클릭해서 특정 서버프로그램 호출
        - 이 서버 프로그램은 data 를 JSON 형식으로 클라이언트에 전송
        - 받은 JSON을 적절하게 처리 > 화면 구성
        - 서버프로그램 : 제공된 프로그램 이용
        - http://192.168.0.200:8080/bookSearch/search?keyword=java
          - 한빛 미디어에서 출간된 IT도서 데이터

     2. 제공 받은 데이터를 이용해서 화면을 만들기

        개발자들이 쉽게 화면 디자인 하기 위해서 사용하는 framework이 있음.

        Bootsrap을 이용 화면 만들기



- 제공된 서버프로그램을 이용해서 클라이언트 사이드에서 프로그램 처리
  1. 도서검색
  2. 영화 일일 박스 오피스 순위 Open API
  3. 다음 API를 이용한 검색



- 서버쪽 프로그램을 제공 받는게 아니라 우리가 직접 작성
  - Python + Django



- 3주짜리 web 프로젝트



```javascript
$.ajax({
    async : true,   // 비동기 방식의 호출(default)
    url : "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json", // api url
    data : {
        key: "ce9dadd4f55de8ecbed0a447de4ba1ea", // 할당된 key
        targetDt: $("input[type=text]").val() // 검색 key
    },
    type : "GET",
    timeout : 3000,
    dataType : "json",   // 결과 JSON을 JavaScript객체로 변환.
    success : function(result) {
    
    }
```