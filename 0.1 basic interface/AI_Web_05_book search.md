# 04_book search









===



###### 07/27일



- 프로토콜 (약속/ 규칙) (서로 맞아야 데이터를 주고받을 수 있음.)
  - 프로토콜://서버쪽 컴퓨터의 IP : 웹서버 프로그램의 포트번호/프로젝트/프로그램명
  - http://192.168.0.200:8080/bookSearch/search?keyword=java



- 프로그램에 데이터를 넘겨주려면?

  1. URL 을 이용해서 데이터를 넘겨주는 방법

     - get 방식

     - Query String이라는 문자열을 이용해서 데이터를 넘기기.

       ?key=value&key=value&key=value&...

  2. Request header를 이용해서 데이터를 넘겨주는 방법

     - post 방식

