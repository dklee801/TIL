# Python

1. datatype

2. 자료구조(list, tuple, dict, set...)

3. 제어문(if, for, while...)

4. 객체지향 언어

   함수형 언어

5. 기타 등등의 기능, 문법(예외 처리)

6. 모듈(package)



#### 1. python datatype = built-in type

- numeric (숫자형)  : 정수(int)/ 실수(float) / 복소수(complex)
- Sequence : list, tuple, range
  - tuple = (1 ,2 ,3 ) / 1, 2, 3 :()
- Text Sequence type : 문자열 (str)
- Mapping type : dict
  - dict = key: value 의 쌍으로 데이터 표현 :{key:value}
- Set : set
  - set = 중복되는 것 삭제 dict와 표현식이 같음. : {1, 2, 3}
- Boolean : True/ False
  - True, False, 빈 list, 빈 dict, 빈 tuple, 숫자 0 , None

클래스의 타입 출력 : type()



- 문자열,list : indexing, slicing
- 연산 
  - 프로그래밍 언어에서의 연산은 기본적으로 같은 데이터 타입끼리 수행



#### 3. 제어문

1. if형식/, for문형식...

   if 조건: ...elif조건:...else:

   for tmp in range()

   for tmp in list, tuple, dict





#### 4. 객체지향 

-  프로그램의 유지보수와 재활용성에 초점을 맞추는 개발방법론
- 프로그램의 기능보다는 구성요소, 각 요소들간의 작용
- 살계하고 구현하기가 상대적으로 어렵
- 현실세계의 문제를 그대로 프로그래밍 적으로 모델링하는 방법



- 하나의 클래스의 내용을 이어받아서 다른 클래스를 작성 : 상속

- class로부터 실제 사용가능한 메모리 공간을 만듦 : instance . 객체

- 객체를 생성할때 맨 처음에 초기화 목적으로 호출되는 함수

  `__init__(self)`

  - `__` 를 이용해서 특정 목적의 함수가 클래스 내부에 정의되어 있음.(magic function)

- 하위 클래스에서 이런 method를 재정의 하는 일을 변경해서 사용할 수 있음.: method overriding

- 클래스의 method나 함수의 인자를 사용할때, 

  - 원래는 형식에 맞게끔 사용해야됨.

  - def my_sum(*a):

    a=  (10,20,30,40)

- class 내부에는 여러가지 나올 수 있음

  - init에서 정의되는 instance variale
  - class안에서 정의되는 class varible

- First class, Closure, Decorator

  - first class cititznen
    	1. 프로그래밍 개체가 변수나 데이터 구조에 저장이 가능.
     	2. 프로그래밍 개체가 함수의 인자로 사용.
     	3. 프로그래밍 개체를 함수가 리턴 할 수 있음.

  ​	

- list comprehension

  ​	[tmp for tmp in range(100) if tmp%10 ==0]





# html





...

AJAX : 서버쪽 프로그램을 호출해서 그 결과를 JSON, XML

- 서버쪽 웹 프로그래밍을 하가위해 : Django

  - 코드로 연습을 했음.

    1. 프로젝트 생성 

    2. application 생성

    3. class 구현을 가지고 어떻게 database를 구축할지 표현한 명세

       > make migrations

    4. 명세가 준비 되면 실제 database에서 처리 진행

       > migrate

    5. 서버쪽 세팅

    6. URL 세팅 후 views, template

    7. template파일에서 template tag 사용 

       {% %}: 로직처리, {{ }}: 값 가져오기

    8. ModelForm 사용하는 방법

       post방식을 이용해서 처리, request.POST

    9. 장고가 가지는 특징

       MVC > MVT(model, view, template)

       ORM(Object Relation Mapping)

       관리자 화면을 기본으로 제공

       Elegant URL(정규 표현식으로 URL표현)



총 30문제 (오픈북 x)

url: e-ncs에 접속



수행평가는

워드파일 하나 생성 :

우리 수행평가 문제 2개

화면 캡쳐

1. 영화 진흥위원회 open api 이용한 영화 검색

   동작하는 화면 캡쳐

   소스 코드를 워드 파일에 입력

   comment 적기.

2. 게시판

   - 기본 게시판

   - 댓글 

   - 로그인

     반드시 comment

     (여러번 하다보니 migration 초기화가 안되서? 에러가 나는듯?...)

     