





# 07_Python_Decorator

- 사전적 의미 : 장식가, 도배업자
  - Python decorator는 기존의 코드에 여러가지 기능을 추가하는 python 구문

```python
import time
def my_outer_func(func):
    def my_inner_func():
        print("{} 함수 수행시간을 계산합니다.".format(func.__name__))
        start = time.time() # 1970년 1월 1일  = 0
        func()
        end = time.time()

    return my_inner_func

@my_outer_func # Decorator, 원래 기능에 새로운 기능추가
def my_func():
    print("my_func()가 호출")
```

*args

```python
def print_user_name(*args): # 인자로 들어온 사람의 이름을 출력,
# args는 tuple로 여러개로 받을 수 있음
    for name in args:
        print(name)

print_user_name("홍길동","신사임당")
print_user_name("홍길동","신사임당","유관순")
```

**kwargs

```python
def print_user_name(**kwargs):
    #kwargs 는 dict 로 받음
    for key in kwargs.keys():
        print(kwargs.get(key))

#{"name1" : "홍길동, "name2" : "유관순"}
print_user_name(name1= "홍길동", name2 = "유관순")
```



###### Decorator에 대해 한가지 더

~~~python
def my_outer(func):

    def my_inner(*args,**kwargs):
        print("decorator 시작")
        func(*args, **kwargs)
        print("decorator 종료")

    return my_inner

@my_outer
def my_func():
    print("이것은 소리없는 아우성")
    
my_func()

```
decorator 시작
이것은 소리없는 아우성
decorator 종료
````
    

@my_outer
def my_add(x, y):
    print("두 수의 합은 : {}".format(x+y))

my_add(10,20)

```
decorator 시작
두 수의 합은 : 30
decorator 종료
```
~~~

