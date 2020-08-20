# ModelForm을 이용해서 CRUD구현

> CRUD : Create, Read, Update, Delete



- ModelForm을 이용하면 사용자 입력양식 처리하는게 한결 쉬워짐.
- 여기에 Bootsrap도 포함해서 Web application생성

1. ##### 필요한 패키지 설치

   1. pip install Django

   2. 추가적으로 bootsrap에 대한 package를 설치

      - 일반적인 HTML 파일을 만들고 Bootsrap을 적용할 때는 CDN과 tag속성을 이용하면 Bootstrap을 이용할 수 있음.

      - 하지만 ModelForm을 이용하면 사용자 입력양식 HTML을 자동으로 생성하기 때문에 Bootstrap을 적용 할 수 없음.

      - 이런 경우에 사용자 입력양식에 Boostrap을 적용하기 위해서 특정 package설치해야함.

        > `pip install Django-bootsrap4`
   
   
   
2. ##### Project를 생성

   - Django는 framework이고 scaffolding기능을 제공

     - cmd > working directory를 python-Django폴더로 변경

       `cd/`

       `cd python-Django`

     - `django-admin startproject` + project name

     - project와 앞으로 생성할 application를 폴더가 하나 만들어지는데,  상위 폴더의 이름을 MyBlogSystem으로 변경

     - 하나의 appliaction을 우리 프로젝트에 추가

       > python mange.py startapp  posts

     

3. ##### Project 설정(setting)

   - blog project에 있는 setting.py

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'posts.apps.PostsConfig',
       'bootstrap4'
   ]
   
   ...
   
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR,'blog','templates')],
           # 수정하고 blog폴더에 templates폴더 생성할 것.
           
   ...
   
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'static')
   ]
           # 최상위폴더로 static하나 생성할 것.
           
   ```

   

4. ##### Project를 web에 deploy해 봐야 함.

   - Django 는 admin 페이지가 존재하기 때문에, web에 deploy하기 전에 기본 table이 꼭 database에 존재해야함

     - `python manage.py migrate` 데이터 베이스에서 사용할 명세가 존재하는 경우, 데이터 베이스 생성

     - 관리자 계정이 있어야 Admin page(관리자 화면)을 사용할 수 있음.

       `python manage.py createsuperuser`

       `python manage.py runserver`

   -----setting 끝-----

5. ##### 기능 구현/ application구현 (Model 구현)

   - 기능 구현할 때 제일 먼저 해야할 일은 사용할 데이터에 대한 정확한 명세를 작성.

   - Django는 ORM을 이용하기 때문에 class를 이용해서 database를 사용.

   - posts application 폴대 내에 models.py 파일에 Model 을 정의.

     ```python
     #model.py
     class Post(models.Model):
         author = models.CharField('작성자',max_length=20)
         contents = models.TextField('글내용', max_length= 1000) #TextField: 여러 줄 입력 양식
     
         def __str__(self):
             return self.contents
     ```

   - 이렇게 만든 model을 Admin page에 반영하기 위해서 admin.py 에 등록해야함.

     ```python
     # admin.py
     from django.contrib import admin
     from posts.models import Post
     
     admin.site.register(Post)
     ```

     

   - Model을 생성했기 때문에 데이터베이스에 변경이 필요

     - 데이터 베이스를 어떻게 변경할지 명세(초안)이 필요

       `python manage.py makemigrations`

       posts/migrations/0001_initial.py 에 생김

       

     - 초안이 완성되면 실제로 데이터 베이스에 적용해서 Table을 생성

       `python manage.py migrate`

     

6. ##### URL 경로 설정

   blog project안에 url.py 부터 설정해야함.

   posts application 안에서 urls.py를 설정해야함.

   ```python
   #url.py
   from django.contrib import admin
   from django.urls import path, include
   from django.conf.urls import url
   from django.views.generic.base import TemplateView
   ..
   
   
   urlpatterns = [
       url(r"^$", TemplateView.as_view(template_name ='index.html'),name = 'home'),
       # view의 함수를 거치지않고 template 바로 보여줌.
       path('admin/', admin.site.urls),
       path('posts/', include('posts.urls'))
   ```

   - `url(r"^$", TemplateView.as_view(template_name ='index.html'),name = 'home'),`

     메인화면 html = index.html bootsrap중 example의 element Copy/paste & 필요없는 것 삭제

   

   /posts 에 url.py copy&paste 

   name space 추가

   ```python
   # posts/url.py
   ...
   app_name = 'posts'
   ```

   enter BBS눌렀을때...

   ```python
   # posts/url.py
   from . import views
   ...
   urlpatterns = [
       path('list/',views.p_list, name = 'list')
   ]
   ```

   base.html 파일 만들기

   - blog project/templates 폴더 안에 생성.

   - bootsrap cdn `<head>`에 넣기

   - ```html
     <body>
         {% block container %}
         {% endblock %}
     </body>
     ```

   

7. ##### ModelForm 생성

   - 사용자 입력 양식을 HTML template 안에 직접 입력하는 것이아닌, Model을 기반으로 사용자 입력양식을 자동으로 생성해줄 수 있는데, ModelForm을 이용하면 이 작업을 할 수 있음.


~~~python
 # class를 작성해야함 : /posts/forms.py에서 정의해야함.
 #form.py
 
 from django import forms
 from posts.models import Post
 
 class PostForm(forms.ModelForm):
     class Meta:
         model = Post
         fields = ['author','contents'] # 모델을 기반으로 입력칸 생성
 ```
~~~


​     

8. ##### list page 생성

   - views.py를 수정해서 

     ```python
     from django.shortcuts import render
     from posts.models import Post
     
     # Create your views here.
     def p_list(request):
         my_list = Post.objects.all().order_by('-id') # '-id' id역순으로
         context = {'posts':my_list}
         return render(request, 'list.html', context) # html 에 데이터 전달할 때 꼭 dict형
     ```

`posts/templates/list.html` 생성

```html
<!-- list.html -->
{% extends 'base.html' %}
{% block container %}

    <div class="container">
        <h1>Bulletin Board System(BBS)</h1>
        <button class = "btn btn-primary"
                onclick="new_post()">새글작성</button>
        <div class = "m-1"></div>

        <table class= "table table-hover">
            <thead class = "thead-dark">
                <tr>
                    <th scope ="col">#</th>
                    <th scope ="col">작성자</th>
                    <th scope ="col">내용</th>
                    <th scope ="col">수정</th>
                    <th scope ="col">삭제</th>
                </tr>
            </thead>
        <tbody>
            {% for post in posts %}
            <tr>
                <th scope="row">{{post.id}}</th>
                <td>{{post.author}}</td>
                <td>{{post.contents}}</td>
                <td></td>
                <td></td>
            </tr>
            {% endfor %}
        </tbody>
        </table>

    </div>

{% endblock %}
```

- `scope` : 해당 셀이 행/열 헤더 인지/ 혹은 행/열 그룹인지 지정

 The scope attribute specifies whether a header cell is a header for a column, row, or group of columns or rows.



- `<thead>` : 테이블 헤더

The `<thead>` tag is used to group header content in an HTML table.

The `<thead>` element is used in conjunction with the and elements to specify each part of a table (header, body, footer).



- `<tr>` :테이블 row / 행 정의

The `<tr>` tag defines a row in an HTML table.

A `<tr>` element contains one or more



- `<td>` : 테이블 데이터/  셀 내 데이터 정의

`<td>` tag defines a standard data cell in an HTML table.



##### 9.create page 생성

- js 경로 추가

```html
<!-- list.html -->
{% extends 'base.html' %}
{% block container %}
    <script src = "/static/js/post.js"></script>
    <div class="container">
```

static 폴더에 js 폴더생성 , post.js생성

```javascript
//posts.js

function new_post() {
// 현재 page의 url을 변경하려면
location.href = '/posts/create/'
}
//'posts/create 를 호출하라'
```

이제create url 추가

```python
#url.py

urlpatterns = [
    path('list/',views.p_list, name = 'list'),
    path('create/',views.p_create, name = 'create')
]
```

이제 views.p_create 작성

```python
def p_create(request):
    # POST 방식으로 호출될 때
    if request.method == 'POST':
       pass

    # GET 방식으로 호출될 때
    else:
        post_form = PostForm()

    return render(request, 'create.html', {'post_form':post_form})
```

create.html 작성

```html
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block container %}
    <div class ="container">
        <h1>새글작성</h1>
        <form method="post">
            {%csrf_token%}
            {% bootstrap_form post_form %}
            <button type = "submit" class = "btn btn-primary">등록</button>
        </form>
    </div>
{% endblock %}
```

views.py에서 class p_create의  "POST"정의(위의 html에서 submit에 대한 대응)







##### 10.delete 기능 구현

1. html 에서 버튼 추가

   ```html
   <!-- list.html -->
   <tbody>
      ...
           <td>
               <a href="{% url 'posts:delete' post.id %}" class = "btn btn-danger">삭제</a>
           </td>
       </tr>
       {% endfor %}
   </tbody>
   ```

2. url 추가

   ```python
   # url.py
   urlpatterns = [
       ...
       path('<int:post_id>/delete/',views.p_delete, name = 'delete')
   ]
   ```

3. views.p_delete 추가

   ```python
   #views.py
   from django.shortcuts import render, redirect
   ...
   def p_delete(request, post_id):
       post = Post.objects.get(id=post_id)
       post.delete()
   
       return redirect('posts:list')
   ```



##### 11. 수정기능 추가

 1. html 에서 버튼 추가

 2. url.py 추가

 3. views.p_edit 추가

    ```python
    def p_edit(request, post_id):
        post = get_object_or_404(Post, pk=post_id)
    
        if request.method == 'POST':
            post_form = PostForm(request.POST, instance=post)
    
            if post_form.is_valid():
                post_form.save()
                return redirect('posts:list')
    
        else:
            post_form = PostForm(instance=post)
            return render(request, 'create.html', {'post_form':post_form})
    ```



##### 12. 댓글기능

https://tutorial-extensions.djangogirls.org/ko/homework_create_more_models/