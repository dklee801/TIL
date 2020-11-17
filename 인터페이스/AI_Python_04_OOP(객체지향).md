## AI 융복합과정 2일차

## 인터페이스 개발

### 20.07.16

### 

##### 객체 지향

- 대표적인 프로그램 작성 방식

  - 구조적 프로그래밍(절차적 프로그래밍)

    - 프로그램 작성시 기능으로 세분화해서 각각의 기능을 모듈로 제작,  프로그램을 작성
    - 설계가 쉬워 시간과 비용을 절약
    - 유지보수가 어렵다, 모듈을 변경하면 연결된 모든 코드와 영향을 주고 받기때문에

  - 점점 유지보수가 중요하게 대두

    - 현실 세계의 해결해야 하는 문제에 대한 구성요소 파악

    - ex)) 은행의 구성: 은행지점, 고객, 텔러, ATM, 계좌  >> 개체(object)

      

###### Object oriented programming (OOP)

- 개체들을 파악해서 개체들간의 관계를 프로그래밍 하는 방식

- 개체들을 파악하고 각각의 개체를 프로그램으로 묘사해야함 : 객체 모델링

  

  ######  e.g)	사람들을 프로그램적으로 묘사

-  추상화(Abstraction) 과정을 거쳐서 사람을 객체 모델링

- 이런 개체들은 속성, 행위가 있음.

- 속성: 변수(property, member field, field), 행위: 함수(method)

- class라는 걸 이용해서 추상화과정을 거친 프로그램적으로 표현하게 됨

  - class 사람
    - 키: height  (변수) (float)
    - 몸무게 : weight  (변수) (float)
    - 나이: age  (변수) (int)
    - 이름 : name (변수) (str)
    - 걷는다 (메소드)
    - 말한다 (메소드)
    - 잔다 (메소드)

- class는 data type의 관점에서 봤을 때, 기존 데이터 타입을 이용해서 새로운 data type을 만드는 것
- class >> 추상적인 데이터 타입 (Abstract data type  = ADT)



> 객체 지향 프로그래밍
>
> - 현실 세계의 해결해야할 문제를 그대로 프로그램으로 묘샤(표현)
> - 프로그램을 구성하는 주체들(객체, object)을 파악.
> - 각 객체들 간의 데이터 흐름에 초점을 맞춰서 프로그램 작성
> - 설계와 작성에 어렵지만 유지보수가 편함



```python
# 학생의 이름, 학과, 학번, 평균평점을 저장하는 방법에 대해 생각
stu_name = "홍길동"
stu_dept = "경영학과"
stu_num = "20200714" # 학번은 연산할 필요가 없기 때문에, str로 저장하면 처리하기 더 쉽다.
stu_grade = 3.5
```

###### 클래스로 작성

```python
class Student(object): #클래스는 첫글자 대문자
    # 클래스가 생성되면 클래스를 기반으로부터 메모리에 공간들(instance: 인스턴스, object: 객체)이 생성 (홍길동 인스턴스, 김길동 인스턴스...)
    def __init__(self, name, dept, num, grade):
    # __init__ 모든 클래스가 가지고 있는 필수 매소드
    # 인스턴스 생성 후 init 호출 > intit 이 ()안의 인자로 해당 인스턴스를 초기화함.
    # self > 현재의 인스턴스를 가리킴
        self.name = name
        self.dept = dept
        self.grade = grade
        self.num = num
        # ' . ' dot operator(연산자), 앞에가 가리키는 것에 대해서
        ## 초기화 완료 ## 인스턴스에 name, dept, grade, num을 입력함
        ## instance가 가지고 있는 변수 name, dept, grade, num > instance variable(변수)
students = []
students.append(Student("홍길동","경영학과","20200714","3.5"))
students.append(Student("김길동","심리학과","20200094","4.0"))
```

- Python은 객체지향 언어
- Python의 모든 것은 전부 객체(instance)

```python
a = 10
print(type(a)) # class 'int'
my_list = [10]
print(type(my_list)) # class 'list
print(students[0].dept)
```

- 숫자, 리스트, 문자열, 함수 모두 객체

- 객체가 있다는 것은 class가 존재

- 객체가 있다는 것은 변수/ method가 존재

  > 객체(instance)란 속성과 같은 여러가지 데이터 + 메소드를 가지고 있는 데이터 구조를 지칭

  ```python
  class Student(object): #클래스는 첫글자 대문자
      def __init__(self, name, dept, num, grade): # constructor(생성자), 파이썬에서는 initializer
          self.name = name
          self.dept = dept
          self.grade = grade
          self.num = num
  
      def __repr__(self): # print(student) 했을때 메모리 주소값이 아니라 아래의 값들이 나옴
          return self.name
  
      def change_dept(self,tmp_dept):
          # tmp
          self.dept = self.dept
  ```

```python
student = Student("홍길동", "경영학과", "20201111", "4.5")
print(student.dept)
student.dept = "경제학과" # 객체를 다이렉트 수정 : 권장되지 않음
print(student.dept)
# 정보은닉 (information hiding - 원본 객체 보존)
```

```python
# Python이 제공하는 내장함수 중
# dir() : 객체가 인자로 들어오면 해당 객체의 모든 속성과 메소드를 알랴줌
student = Student("홍길동", "심리학과" , 4.0, "20200714")
print(dir(student)) ## __func__ : 매직function

# python의 함수도 객체
def my_func(a,b):
    return a+b
print(dir(my_func))
my_func.myName = "홍길동" # 함수도 객체다, myName 이 추가됨
print(dir(my_func))
```

```python
### class variable
class Student(object): #클래스는 첫글자 대문자

    scholarship = 3.0 # class variable, 클래스가 가지고 있는 variable, 모든 instance가 공유하는 변수

    def __init__(self, name, dept, num, grade):
        self.name = name
        self.dept = dept
        self.grade = grade
        self.num = num

    # 메소드를 통해 해당 학생이 장학생인지 아닌지 확인하고 싶다
    def is_scholarship(self):
        if self.grade >= Student.scholarship: # scholarship은 클래스가 가지고 있는 variable이기 때문에 앞에 class.
            return True
        else:
            return False

student = Student("홍길동", "심리학과", "20202020", 4.5)
print(student.is_scholarship())
```

##### 

#### Name space

- 객체가 가지는 데이터를 나누어서 관리하는 공간
- intance/ class / super class namepace 가 있다.
- instacne namespace < class namespace < super class namespace
- 객체를 instacne namespace에서 찾고 다음 class namespace 그 다음 super class에서 찾음



###### python은 동적으로 속성이나 method를 추가할 수 있음.

```python
print(student.dept)
student.depts = "컴퓨터"  # depts 속성이 추가
print(student.depts)

student.scholarship = 4.5 # instance에 scholarship 이란 variable이 없기 떄문에 instance variable에 추가됨
# class instance가 변경되는것이 아니다 > namespace 가 다르기 때문에
print(Student.scholarship) # class
print(student.scholarship) # instance
```



```python
class Student(object):
    scholarship = 3.0

    def __init__(self, name, dept, num, grade):
        self.name = name
        self.dept = dept
        self.grade = grade
        self.num = num

    @classmethod #class method decorator, 데코레이터
    def change_scholarship(cls,rate):  #cls: class
        cls.scholarship = rate
        print("장학금 기준 {}로변경".format(rate))
        # class method 는 class 를 인자로 받아서 class variable 을 생성, 변경, 참조 하기위해 사용
        # 속성을 직접 엑세스하는 것보단 def를 통해 하는 것이 바람직함

    def is_scholarship(self):
        # instacne method(self를 지칭하는 모든 method)
        # 인스턴스에 한정된 데이터를 생성,변경,참조하기 위해서 사용
        if self.grade >= Student.scholarship:
            return True
        else:
            return False

    # staticmethod : class namespace 안에서 정의된 일반 method
    @ staticmethod
    def is_valid_schoarship(rate):
        if rate < 0:
            print("학점은 음수 불가능")

Student.change_scholarship(3.7)
Student.is_valid_schoarship(-2)
```



##### Information hiding (정보 은닉)

- instance가 가지는 속성은 매우 중요한 데이터 이기 때문에 외부에서 직접 access하는 것은 좋지 않음.
- 외부에서 직접 access하는 것을 막는 방법
- 프로그램 언어마다 다름
- public(접근 가능) vs private(접근 불가능)

```python
class Student:
    def __init__(self,name,dept):
        self.name = name
        self.__dept = dept
    # __variable : private 처리
```

- private 으로 처리된 속성이 잇으면 외부에서 직접적인 access가 안되기 때문에 method를 이용해서 사용하도록 처리

  

  ###### getter

- private으로 되어 있는 속성의 값을 알아보는 용도의 method가 필요함. = getter (값을 가져옴)

- getter 이름 정하는 방법 : get_ + 변수(대문자 첫글자 + 나머지 소문자)

  ```python
  def get_Dept(self):
      return self.__dept
  ```



###### 	setter

- 값을 설정해줌

```python
def set_Dept(self,dept):
    self.__dept = dept
```



###### 	method private

- method를 cls 내부에서만 사용되고 외부에서 사용안되게 하는 방법

```python
def __print_name(self):
    return self.name
```



####  

#### Class

- 객체 지향을 하는 이유는 유지보수와 재사용성.
- 재사용성을 위한 대표적인 객체지향 기법 > inheritance (상속)
- parent class (super class) > child class (sub class)
- Python의 모든 class는 object class로 부터 상속



###### is - A 관계 (sub class is a super class) 관계, 역은 성립하지 않음

- starcraft 예제
- 두개의 class를 이용해서 상속 알아보기

- Unit class > sub class

- ```python
  class Unit(object):
      def __init__(self,hp,dmg):
          self.utype = self.__class__.__name__ #지금 인스턴스가 어떤 cls인지, 그리고 이름을 불러오기
          self.hp = hp
          self.dmg = dmg
      def show_status(self):
          print("직업: {}".format(self.utype))
          print("공격력: {}".format(self.dmg))
          print("생명력: {}".format(self.hp))
  
  class Marine(Unit):
      # method overriding
      def __init__(self,hp,dmg,range_up):
          super(Marine, self).__init__(dmg, hp) # (cls)의 상위 cls 찾아가서 .__init__ 호출, 인자는 (dmg,hp)
          self.range_up = range_up
      def show_status(self):
          super(Marine, self).show_status()
          print("사거리 업그레이드: {}".format(self.range_up))
  
  marine_1 = Marine("100","100",True)
  marine_1.show_status()
  ```

- super(현재 cls, self). method 로 상위 cls method 호출
- 상속은 코드를 복사하는 것이 아니라 namespace에 연결되어 super cls namespace에서 찾을 수 있게함.