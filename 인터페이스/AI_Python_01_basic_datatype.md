## AI 융복합과정 1일차

## 인터페이스 개발

### 20.07.14

### 

#### 파이썬 개요 및 기초



##### 파이썬 개요

###### python

- 1990년에 만들어진

- 데이터 처리에 강점
- 현재는 실무에서 많이 사용



###### Python의 장점

- 러닝커브가 얕음
- 무료 / 간결 / 성능좋음 : 정말 빠른 처리가 필요한 부분은 C로 작성, Python과 결합
- 가독성좋음 : 중괄호({})를 이용하지 않고 indentation(들여쓰기)를 이용해서 코드 블럭을 표현
- 다양한 분야의 프로그램을 할 수 있음
- web program, GUI, Database 프로그램, data analysis 프로그램
- System program, Mobile App program은 안됨

###### R 

- 통계, 데이터분석 : 데이터를 레포팅/ 발표할 때 유용



###### 개발환경 구축

진행순서 Pycharm > Jupyter notebook >  Google Colab 순으로 배울 것임

이후 Colab만 이용



##### Python 문법

1. 주석

   - 1줄 주석 : #

   - 1줄 이상 주석 : """  """ or  ''' '''

   - 블럭 잡고 ctrl + /

2.  Python의 keyword

   imort keyword

   print(keyword.kwlist)

3.  변수의 생성과 삭제

   - 변수명 생성시 _ 등을 사용하여 충돌 방지

   my_var = 100

   - 변수를 생성하고 값을 입력 >> 메모리에 값을 저장(객체)하고 변수에 객체의 메모리상의 주소를 저장

4. 변수를 삭제할 수 있음

   del my_var

   - 변수를 삭제하면 메모리에 저장된 객체값을 포인팅하는 변수가 없어지기 때문에 결국 객체도 삭제(메모리 확보)



##### Python의 데이터 타입(data type)

- Python의 built-in data type (이미 정의되어있는 데이터 타입)
  -  numeric : 숫자
  - sequence : 순서가 있는 데이터 타입
  - text sequence : 문자열
  - set
  - mapping
  - bool

###### Numeric data type (숫자형)

- int(정수)

- float(실수)
- complex(복소수)

```python
a = 100 # 정수
b = 3.14159 # 실수
c= 1+2j
d = 0o34 # 8진수
e = 0xAB # 16진수

# 데이터 타입 확인
print(type(a)) # class int
print(type(b)) # class float
print(type(c)) # class complex
```



###### Text sequence type(str)

- 다른 언어는 문자와 문자열 구분
- 문자는 한글자, 문자열을 두글자 이상으로 구성
- 표현 (' ', " ")

- 문자열 연산

  ```python
  first = "haha"
  second = "hoho"
  print(first + second) #hahahoho
  print(first + str(10)) #haha10
  print(first * 3) #hahahahahaha = first + first + first
  ```



- indexing

  ```python
  my_var = "hello"
  print(my_var[1]) # = "h"
  print(my_var[-1]) # = "o" , 맨뒤
  ```

- slicing

  ```python
  my_var = "이것은소리없는"
  print(my_var[0:3]) # = 이것은 # 앞의 시작점은 포함, 뒤는 제외 > 0번 ~ 2번
  print(my_var[:3]) # = 이것은
  print(my_var[0:-1]) # = 이것은소리없
  print(my_var[:]) # = 이것은소리없는
  ```

- formating

  ```python
  num_of_apple = 10
  myStr = "나는 사과를 %d개 가지고 있어요." % num_of_apple
  
  myStr = "나는 사과를 {}개, 바나나 {}개 가지고 있어요.".format(num_of_apple,20)
  
  myStr = "나는 사과를 {0}개, 바나나 {1}개 가지고 있어요.".format(num_of_apple,20)
  
  myStr = "나는 사과를 {1}개, 바나나 {0}개 가지고 있어요.".format(num_of_apple,20)
  ```

- 함수와 매서드의 차이
  - 함수 : 기본 제공되는(정해져 있는) 코드 집합 (독립적으로 존재)
  - 매서드: 종속되어 있는 코드 집합 (sth + . + func)
- len() : 길이
- x.count('y')  : x에서 y가 몇개 있는지
- x.upper() : 대문자
- x.lower() : 소문자
- x.strip() : 의미없는 공백 날리기 



###### sequence type

- list

  - 임의의 객체(데이터)를 순서대로 저장하는 집합 자료형

  - 코드로 표현(literal)할 때 [] (대괄호)

    ```python
    my_list = []
    my_list = list()
    my_list = [1, 2, 3,3.4,"hello"]
    my_list = [1, 2, 3, [5, 6, 7],100]
    ```

  - indexing과 slicing을 할 수 있다.

    - 리스트의 slicing > 리스트로

  - 리스트의 연산

    ```python
    a = [1, 2, 3]
    b = [4, 5, 6]
    print(a+b) 
    # [1, 2, 3, 4, 5, 6]
    print(a*3) 
    # [1, 2, 3, 1, 2, 3, 1, 2, 3]
    ```

  - 리스트의 변환

    ```python
    a = [1, 2, 3]
    a[0] = 5
    print(a)
    # [5, 2, 3]
    ```

  - 리스트의 추가

    ```python
    a = [1, 2, 3]
    a.append([5, 6, 7])
    print(a)
    # [1, 2, 3, [5, 6, 7]]
    ```

  - 리스트의 정렬

    ```python
    my_list = ["홍길동", "아이유", "강감찬", "english"]
    result = my_list.sort() #오름차순 정렬(유니코드 코드표 순서대로)
    print(result)
    #<class 'tuple'>
    print(result)
    # None >매서드는 리턴값을 가지지  않는 것이 있음. = 객체 스스로 변경하는 매서드인 sort
    print(my_list)
    # ['english', '강감찬', '아이유', '홍길동']
    ```

- Sequence type : tuple

  - ()로 표현

  - indexing, slicing 모두 가능

  - 일단 만들어지면 내용 변경이 안됨 (read-only)

  - 원본 데이터 보호

  - 1개 요소만 있을 때는

    - a = (1, )

  - 괄호 없으면 tuple

    - ```python
      a = 1, 2, 3
      print(type(a))
      # <class 'tuple'>
      ```

  - tuple + tuple : 자기 요소가 변하지 않으므로 문제없음.



- Sequence : range

  - 주로 for 문에서

  - 적은 양의 메모리로 같은 데이터를 표현

    ```python
    my_range = range(1,10,3) # 1부터 10까지 3씩 증가
    ```

###### Mapping (dictionary = dict)  (key <> value) (python 3.8부터 순서 개념 생김)

- key와 value로 데이터를 저장하는 자료 구조

- { }로 표현

  ```python
  a = {"name":"홍길동","age":48}
  
  print(type(a),a)
  # <class 'dict'> {'name': '홍길동', 'age': 48}
  
  print(a["name"])
  # 홍길동
  
  a["address"] = "서울"
  print(a)
  # {'name': '홍길동', 'age': 48, 'address': '서울'}
  
  # dict 에서 많이 사용하는 method
  print(a.keys()) # key값의 리스트
  print(a.values()) # value 값의 리스트
  ```



###### ----7월 14일 끝

###### ---- 7월 15일 내용 시작



###### bool data type (boolean, True / False)

- 사용하는 연산자
  - and / or / not
- 다음의 경우에는 Python에서 False로 간주
  1. 빈 문자열 ==  "", ''
  2. 빈 리스트/ 튜플/ 딕셔너리 == [] / () / {}
  3. 숫자 0
  4. None
- bitwise 연산

```python
print(a & b) # & : bitwise 연산
             # 0101 & 0000 = 0000
print(a | b) # | : bitwise 연산
             # 0101 | 0000 = 0101
```



###### Set data type

- 집합 자료형, 중복을 허용하지 않음, 순서가 없음

- {key: value} == dict

- {1, 2, 3} == set

- ```python
  my_set = {1,2,3,4,1,2}
  print(my_set)
  # {1, 2, 3, 4}
  ```

- set 에서 사용하는 연산자

  - 합집합(union) == |

  - 교집합(intersection) == &

  - 차집합(difference) == -

  - ```python
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    print(s1 | s2) #union
    print(s1 & s2) #intersection
    print(s1 - s2) #difference
    ```



