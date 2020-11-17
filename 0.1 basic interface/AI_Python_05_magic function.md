# 05_Python_magic function

##### 소멸자

- __ del __ 로 호출됨

  ```python
  class Student:
      def __init__(self,name,dept):
          self.name = name
          self.dept = dept
      def __del__(self):
          print("메모리에서 객체 삭제)")
  
  stu1 = Student("홍길동", "경영학과")
  
  del Student
  ```



##### 연산자

- __ add __ 

```python
class MyInt(int): # int 클래스 상속
    pass
my_num = MyInt(100)

print(my_num +200) == print(my_num.__add__(200))
```



##### repr

- __ repr __
- 메모리 주소가 아닌 원하는 정보를 출력할 수 있음.

```python
class Student(object):
    def __init__(self,name,dept):
        self.name = name
        self.dept = dept

stu1 = Student("홍길동", "경영학과")
print(stu1)  ## instacne 의 class정보와 저장되어 있는 메모리 주소가 출력
# __repr__ 로 메모리주소가 아닌 원하는 정보 출력가능
```

```python
class Student(object):
    def __init__(self,name,dept):
        self.name = name
        self.dept = dept

    def __repr__(self):  ##주소값대신 출력
        return self.name

stu1 = Student("홍길동", "경영학과")
print(stu1)
```



##### __ lt __

```python
class Car(object):
    def __init__(self, model, price):
        self.model = model
        self.price = price

car1 = Car("G70", 5000)
car2 = Car("Sonata", 3000)

print(car1.price < car2.price)
```

######  False, .price 없이 하고 싶을때 >> __ lt __

```python
class Car(object):
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __lt__(self, other):
        if self.price < other.price:
            return "{} 가격이 더 낮습니다.".format(self.model)
        elif self.price == other.price:
            return "가격이 같습니다."
        else:
            return "{} 가격이 더 높습니다.".format(self.model)

car1 = Car("G70", 5000)
car2 = Car("Sonata", 3000)
print(car1 < car2)
```