# Python_Django

### Django: Python으로 만들어진

- 오픈소스
- 웹 어플리케이션을 쉽게 작성할 수 있도록 도와주는 Framework



- ###### 라이브러리(library)

  - 특수한 처리를 하기 위한 함수의 집합
  - jQuery 도 라이브러리라고 볼 수 있음.
  - 장점: 모든걸 직접 작성할 필요 없음.
  - 단점(특징): 전체 프로그램의 로직을 담당하지 않음
    - 예) jQuery를 이용해서 영화정보를 출력하는 문제를 구현할 때 사람마다 구현이 다름



- ###### 프레임워크(Framework)

  - 프로그램의 전체적인 로직이 이미 구현이 되어 있음
  - 프레임워크를 사용할때 기본적으로 사용되는 코드가 제공(스케폴딩 - scaffolding)
  - 유지보수성이 좋음.
  - 단, 처음에 프레임워크의 동작원리를 이해해야함.



- Django를 이용하면 Web Application에서 많이 자주 구현해야 하는 내용을 쉽게 구할 수 있음.

  ### Django의 특징


1. 장고는 MVC Model을 기반으로 한 MVT model을 이용함.

   MVC Model : Model, View, Controller

   <u>MVT Model : Model, View, Template</u>

   - Model : 데이터 베이스 처리
   - View : 로직을 담당
   - Template : 클라이언트에게 보여줄 화면을 담당.





### Polls system

- ###### 간단한 web appliaction을 작성

  1. Django를 설치해야함.

     - 도스창에서 pip이용해서 Django 설치 `pip install Django`

     - pip(python install pakage)

     - PyPl(python package index)라는 repository에 있는 Django 설치

       

  2. Project Setup

     - 프로젝트의 뼈대들 만드는 일부터 시작

     - 폴더 하나생성. C:/python-Django 라는 폴더 생성

       > 이 폴더는 여러개의 Django project들을 모아놓은 폴더
       >
       > cmd)) django-admin startproject 프로젝트 이름
       >
       > - 해당 프로젝트 폴더 내에 해당 프로젝트의 파일들을 넣음
       >   - 여기에 새로운 어플리케이션 추가

     프로젝트에 하나의 application을 추가

     - python manage.py startapp polls
     - 수행시키면 polls라는 application이 생성, 폴더가 생성되고 필요한 파일들이 scaffolding됨.
       - scaffolding:  web 페이지를 만들기 위해 필요한 요소들을 자동으로 생성하는 것.
- 이제 PyCharm을 이용해서 처리
     
1. mysite > setting.py에서 프로젝트의 설정
     
     ```python
     # SECURITY WARNING: don't run with debug turned on in production!
     DEBUG = True # 만약 DEBUG가 True 이면 개발모드
                  # False 이면 운영모드
     
     ALLOWED_HOSTS = [] # 만약 DEBUG = True 여서 개발모드면
                         # 비워놔도 됨.
                         # ['localhost','127.0.0.1'] # 비워놨을 시 자동으로
                         # Debug = False이면 운영모드, 실제 운영되는 서버의 IP주소나 Domain Name이 들어와야함.
                 
     ...
     
     INSTALLED_APPS = [ # 어떤 어플리케이션이 이 프로젝트안에 포함되는지 정의
         'django.contrib.admin',
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages',
         'django.contrib.staticfiles',
         'polls.apps.PollsConfig' # polls 패키지 안에 apps모듈안에 PollsConig 클래스
     ]
     
     ...
     
     # Internationalization
     # https://docs.djangoproject.com/en/3.0/topics/i18n/
     
     LANGUAGE_CODE = 'en-us'
     
     TIME_ZONE = 'Asia/Seoul'
     
     USE_I18N = True
     
     USE_L10N = True
     
     USE_TZ = True
```
     
2. Django의 특징, 관리자 모드(화면)을 기본으로 제공
     
   - 관리자에 대한 ID/ PW 가 있어야함
     
   - 이 ID/ PW가 어딘가에는(Database)에 저장되어 있어야함.
     
   - 따라서 Django는 <u>기본적으로 Database 가 설정된 상태로 사용해야함.</u>
     
     
     
3.  기본 테이블(기본 데이터 베이스)를 생성해야함.
     
   - python manage.py migrate
     
          > cmd
          >
     > C:\python-Django\MyFirstWebpoll>python manage.py migrate
     
   
     
4. 서버 기동 하기.
     
   - 내장된 테스트서버를 이용해서 프로젝트를 deploy해보기
     
          > cmd
          >
     > python manage.py runserver : 서버실행
     
          > browser
          >
     > http://localhost:8000/admin : 관리자화면
     
   
     
5. 관리자 ID와 PW 생성
     
        >  cmd
        >
   > python manage.py createsuperuser
     
   
     
   ##### 6. polls application 구현
     
   1.  Model 생성부터 해야함
     
   - Database : 데이터의 집합체
     
   - DBMS(Database Management System) : 데이터 베이스를 구축하고 원하는 정보를 추출하고 새로운 데이터를 입력하고 기존 데이터를 삭제하고 기존 데이터를 수정하는 작업을 진행(프로그램)
     
     > sqlite3 라는 DBMS를 Django에서는 default 로 사용
     
   - CS의 시작부터 생긴 DB
     
          - 극 초기 : 계층형 데이터 베이스(폴더처럼)
          - 1970s? : Relation이라는 주제로 논문발표, IBM에서 이를 토대로 DBMS를 만듦. : DB2
            - 다른 기업들도 이 논문을 근간으로 DBMS를 만들어서 판매
            - Relational Database(관계형 데이터 베이스)
       - 객체 지향의 개념이 추가 되어 '객체 관계형 데이터 베이스' 탄생
     
   - Model 작업은 우리가 사용하는 Database에 Table을 생성하는 작업
     
     (table == relation)
     
   - 강사님 blog 참고
     
   - DB browser for sqllite : portable APP : squlite DB 브라우저
     
   
     
   2. Model 작업부터 시작
     
      application 에서 사용할 데이터베이스 구조를 생각해야함.
     
      ![image-20200803114634320](C:\Users\이동규\AppData\Roaming\Typora\typora-user-images\image-20200803114634320.png)
     
      모델 작업을 하기위해 특정파일을 수정
     
      model.py 안에 모든 Model들을 정의
     
      class의 이름은 table이름과 mapping됨.
     
           ```python
           # model.py
           class Question(models.Model):
               #id = models.IntegerField
               question_text = models.CharField('투표질문제목',max_length = 200)
               pub_date = models.DateTimeField('투표생성날짜')
           
               def __str__(self):
                   return self.question_text
           
           class Choice(models.Model):
               question = models.ForeignKey(Question, on_delete= models.CASCADE)
               # models.FroreignKey : 포린키임을 지정, _id가 컬럼명에 자동으로 붙음
               # on_delete = models.CASCADE : PK 지워지면 연결된 Foreign key삭제
               choice_text = models.CharField("투표문구",max_length= 30)
               votes = models.IntegerField('투표수', default=0)
           
               def __str__(self):
                   return self.choice_text
           ```


~~~python
       class를 다 작성한 후에는 admin page에서 사용할 수 있도록 등록 : admin.py

       ```python
       # admin.py
       from django.contrib import admin
       from polls.models import Question, Choice
       
       admin.site.register(Question)
       admin.site.register(Choice)
       ```
~~~


           이제 SQL구문이 있어야 데이터베이스에 테이블을 생성함.
    
           - class와 매핑되는 테이블을 만들기 위해서 필요한 SQL구문을 생성해야함.
    
             `python manage.py makemigrations`
    
           - 그 다음 이구문을 실행해서 실제 테이블을 생성
    
             `python manage.py miagrate`

2. Model 작업이 끝나면 url 처리를 하러 가면됨

   django url document : https://docs.djangoproject.com/en/3.0/topics/http/urls/
   
   클라이언트가 특정 URL(http://localhost:8000/polls)을 이용해서 서버 프로그램을 호출하면 URLConf 처리를 통해서 호출할 View를 설정

- http://localhost:8000에 대한 

- URLConf : 

```python
# root configuration
# url.py(root내의)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/',include('polls.urls')),
]
```

```python
# polls/ urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'), #http://localhost:8000/polls/ 여기로 들어오면 view.index를 실행하라
]
```

- views.py : url 에서 request를 받아서 html에 띄워줄 데이터를 정의하고 html로 돌려줌.

```python
def index(request):
    # database에서 투표질문의 목록을 가져올것임
    # 원래는 문자열로 표현되어야함, ORM을 사용하다보니 각 레코드가
    # Question 클래스의 객체로 표현.

    my_list = Question.objects.all().order_by('-pub_date') # 해당 클래스의 객체 모두 가져오기
    context = {'question_list':my_list}
    # context 에 'question_list라는 key로 my_list를 value로 저장'
    return render(request, 'index.html', context)
	# index 를 호출하면 index.html과 context를 return
```



- index.html 생성

```html
<body>
    <h1>투표목록임다</h1>
    <ul>
    {% for question in question_list %}
        <!-- polls/ 앞에 '/' 가 없으면 상대경로: 현재경로기준으로 잡음-->
        <!-- 앞에 '/'가 붙으면 http://localhost:8000 뒤에 붙음 -->
        <li><a href = "/polls/{{ question.id }}">{{ question.question_text }}
        </a></li>
        <!-- <a> 앵커엘리멘트 : 링크연결,
		href = '' : 링크를 지정 -->
    {% endfor %}
    </ul>

</body>
```

{{ variable }} : {{ }안의 변수의 결과에 따라 {{}} 안의 내용을 변화시킴.

- 이제 index.html내의 링크가 되어 있는 polls/{{question.id}}에 대한 페이지를 

  Django는 url.py의 urlparttern 내에서 찾음.

  ```python
  urlpatterns = [
      path('', views.index, name = 'index'), #http://localhost:8000/polls/ 여기로 들어오면 view.index를 실행하라
      path('<int:aaa>/', views.detail, name = 'detail'), #http://localhost:8000/polls/<int:aaa> : polls/<int:aaa> : polls/ 뒤에 인티져 값이 오는 url
  ```

  - 즉 `polls/<int:aaa>`의 url이 호출되면 view.detail 을 실행하게됨 : view.detail 프로그램

    ```python
    # view.py
    
    def detail(request, aaa): #받는 aaa:{{question.id}}
        tmp = get_object_or_404(Question, pk=aaa)
        context = {"question":tmp}
        return render(request, 'detail.html',context)
    ```

  - detail.html

    ```html
    <body>
        <!--action=http://localhost:8000/polls/1/vote/-->
        <h1>{{ question.question_text }}</h1>
        <form action ="{% url 'polls:vote' question.id %}" method="post">
        {% csrf_token %}
        {% for choice in question.choice_set.all %}
            <input type = "radio" name = "choice"
                   id = "choice{{forloop.counter}}"
                   value = "{{choice.id}}">
        <label for = "choice{{forloop.counter}}">
            {{choice.choice_text}}
        </label>
        {% endfor %}
        <br><br>
        <input type ="submit" value = "투표" >
        </form>
    </body>
    ```

    ```html
    <form action ="{% url 'polls:vote' question.id %}" method="post">
    ```

    - `form` : An HTML form is used to collect user input. The user input can then be sent to a server for processing.
    - `action` :  The action attribute specifies where to send the form-data when a form is submitted
    - `namespace:name` app_name = 'polls'(네임스페이스) application 선택 , name = ' name'으로 정의된.
    - `url` : url 로 만들기 위한 명령
    - 즉 : url를 만듦 > polls의 네임스페이스에서 vote로 정의된 형태.
    - `method = "post"`  POST 방식 : 서버에 데이터를 보내주는 방식 < - > GET 방식 : 서버에서 받아서 HTML에 띄워주는 방식

    polls\url.py

    ```python
    app_name = 'polls'
    
    urlpatterns = [
        path('<int:bbb>/vote/', views.vote, name = 'vote')
    ]
    ```

    - `<int:bbb>/vote/` 의형태면, views.vote을 호출

    views.py

    ```python
    def vote(request, bbb):
        # url로 넘어온 데이터(bbb)는 detail.html의 question id가 넘어왔음.
        question = get_object_or_404(Question, pk = bbb)
        # request header안에 form에서 선택한 데이터가 포함되서 전달되고
        # 이것을 추출하기 위해서 request.POST["choice"]를 사용
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        selected_choice.votes +=1
        selected_choice.save()
        context = {'tmp':question}
        # result.html에서 현재 투표항목에 대한 각 항목들의 투표현황을 출력
        return render(request, 'result.html',context)
    ```

Django allows you to access reverse relations. By default, Django creates a manager ([`RelatedManager`](https://docs.djangoproject.com/en/1.6/ref/models/relations/#django.db.models.fields.related.RelatedManager)) on your model to handle this, named `<model>_set`, where `<model>` is your model name in lowercase.

​	`<model>_set`: 역관계로 DB 수정

​	`request.POST[" "]` :



- result.html

```html
<body>
    <h1>{{tmp.question_text}}</h1>
    <ul>
    {%for choice in tmp.choice_set.all %}
        <li>{{choice.choice_text}}:{{choice.votes}}</li>
    {%endfor%}
    </ul>

</body>
```

​		

