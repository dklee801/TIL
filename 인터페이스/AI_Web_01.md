# Web service

### 1. Internet?

> - Local Area Network
>
> 일반적으로 하나의 컴퓨터를 standalone으로 사용하지 않고 
>
> 여러개의 컴퓨터를 network으로 묶어서 사용합니다.



- Internet : Network 으로 구성된 전세계적인 Networt
- 인터넷이란 용어는 물리적인 네트워크 망을 지칭하는 용어



###  2. 서비스(service)

- 인터넷을 잘 이용하기 위해서는 인터넷 위에 여러가지 프로그램이 동작하고 있어야함.

- 이런 프로그램을 통칭해서 service라고 함.

- email

- torrent

- web service 등: HTML,CSS,JavaScript를 이용해서 web page를 만들고 web서가 이 web page를 web client에게 전송해서 데이터를 주고 받는 서비스

  

### 3. Web service는 기본적인 구조가 CS구조

- CS: Client- Server 구조
- Web Client - Web server
- Web Client(Web Browser -Chrome, IE, Edge, Safari, firefox, Opera)
- Web Server(만들수도 있지만, 상용프로그램 사용)



### 4. Web Service에 대해 알아봅시다.

- 정적 웹서비스(static web service)
  - HTML, CSS, JavaScript
  - 클라이언트가 특정 HTML 파일을 요청
- 동적 웹서비스(dynamic web service)
  - HTML, CSS , JavaScript + Python
  - 클라이언트가 특정 프로그램을 실행해서 결과를 요청
  

### 5. 개발환경을 세팅.

- 개발툴 : Web Storm
- Web Storm: Pycharm을 만든 회사와 같은 회사.

- HTML, CSS, JavaScript를 사용하기에 가장 괜찮은 툴.

1. ##### Webstorm 다운로드 > 설치

2. ##### 프로젝트 생성 > HTML_basic

3. ##### 파일 생성 > html file 생성 > 01_index



```html
<!DOCTYPE html>


</html>
```

- 모든 내용은 `<html>` 과 `</html>` 영역 사이에 있어야함.
- 주석 `<!-- -->`



4. ##### 출력할 내용 작성

5. ##### web server가 web client 에게 제공할 html을 만들었음.

   1. web server가 존재해야함

   2. web server가 내가 작성한 프로젝트를 인식해야함. 

      > = Configure

   3. web server 프로그램을 기동(실행)하면 자신이 인식하고 있는 web project를 web에서 사용할 수 있도록 전개(deploy) 함.

      - 클라이언트가 접속할 서버 컴퓨터의 IP와 포트번호(웹서버 프로그램 지칭)를 정하게됨.

   4. Web client를 실행해야함. - 크롬실행

   5. 크롬을 이용해서 Web server 에 접속해서 우리가 작성한 HTML 파일을 받아옴

   6. 크롬 브라우저가 받은 HTML을 해석해서 화면을 그림 (Rendering)

      http://localhost:63343/HTML_basic/01_index.htm



HTML 

- tag로 구성되어 있음.
- 문서의 구성(DOM ; Document Object Model)과 내용을 담당

CSS

- 문서의 스타일

JavaScript

- 문서의 동적처리를 담당

- 주석처리 `//`

```html
<!DOCTYPE html>
<html lang="en">

    <head>
        <!-- 일반적인 설정 -->
        <meta charset="UTF-8"> <!-- 인코딩 -->
        <title>Title</title>
        <style>
            h1{
                color : red;
            }
        </style>
        <script>
            function myfunc(){
                alert("소리없는 아우성"); // 경고창을 출력!
            }
        </script>

    </head>

    <body>
        <!-- 출력하고 싶은 내용 -->
        <H1> 이것은 소리없는 아우성 </H1> <!-- heading1(headline) -->
        <input type ="button" value ="클릭클릭" onclick = "myfunc()">
        <br>
        <img src = "image/owl.jpg"> <!-- 끝나는 태그가 없음-->
        <!-- element, tag, property(attribute) -->
        <!-- element : <H1> 이것은 소리없는 아우성 </H1> -->
        <!-- tag: <img -->
        <!-- property : src = -->

    </body>

</html>
```





##### 6. HTML5 : HTML 의 특정버전

- 초기의 웹은 정적(static) web service 위주였음.
- HTML의 표준은 W3C(World Wide Web Consortium)에서 관리.
- 2000년 넘어오면서, 더 이상 버전업 의미가 없어...
- 이유:
  1. 확장성
  2. 정형성(오타에 대한 불허용)이 없음(유지보수에 문제가 발생)
- XML + HTML = XHTML 1.0 .... 망했음(불편함)
- HP, Opera, IBM 기타 등등이 모여서 workgroup을 결성
  - HTML5 을 만듦, 표준이 됨.
  - HTML5가 지향하는 것... Web Application을 만들 수 있음.



#### HTML, CSS, JavaScript 주요스펙



##### HTML - 주요 태그



##### Web 개발 환경의 변화

- Roud trip 방식에서 SPA(Singel Page  Application)으로 변화하고있음.-

- Front_end Web Application으로 작성해야만함.
- AJAX (서버와의 통신을 통해 데이터를 받음)

- HTML, CSS는 기본임
- Java Script 를 잘해야함



JavaScript > jQurey > AJAX

> 순수 JavaScript는 프로그래밍하기가 너무 힘들고 복잡함.
>
> 대신 JavaScript library인 jQuery를 이용해서 이 프로그래밍 처리를 수행

##### jQuery는 사용하기 편하게 만들어 놓은 JavaScript library

결론적으로 HTML, CSS, JavaScript(jQuery)를 이용해서 웹 브라우져 화면을 제어



##### jQuery

1. JavaScript로 만든 사용하기 편한 library
2. 모든 browser에서 동일하게 동작.
   - JavaScript는 browser 마다 상이하게 동작하는 경우가 있음.
     - 브라우저마다 퍼모먼스가 다를 수도 있음.
     - 하지만 jQuery 코드는 browser에 상관없이 잘 동작
3. 무료로 사용가능.



- jQuery를 사용하려면
  - 설치할 수도 있지만, 일반적으로 CDN방식 이용.
  - CDN( Content Delivery Network) : 라이브러리를 네트워크를 통해서 동적으로 다운로드해서 사용하는 개념

