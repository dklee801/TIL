## AI 융복합과정 2일차

## 인터페이스 개발

### 20.07.15

### 

#### 함수

- ###### Python의 함수는 크게 2가지 분류

  1. ###### 내장함수

  2. ###### 사용자 정의 함수(user define function)

  

- 함수 = 특정 작업을 수행하는 일정량의 코드 모음

- 함수 정의 - 위에 두줄 띄우기(코드 컨벤션)

```python


def my_sum(a, b, c):
    return a + b + c

result = my_sum(1,2,3)
print(result)
```

- 함수를 호출하는데 인자가 가변적일 때

  ```python
  def my_sum(*args):                  # 전달되는 인자를 tuple 로 받음
      tmp = 0
      for k in args:
          tmp += k
      return tmp
  
  result = my_sum(1,2,3,4) 
  print("결과:{}".format(result))
  ```

- Python은 함수의 결과값(return값)이 2개 이상일 수 있다?
  - 2개가 아니라 소괄호가 생략된 tuple

```python
def my_operator(a,b):
    result1 = a + b
    result2 = a * b
    return result1, result2
result = my_operator(1,2)
print(type(result))
tmp1, tmp2 = my_operator(1,2)
print(type(tmp1))
```

- Python의 함수는 default parameter를 사용할 수 있다.

  ```python
  def my_default(a,b,c= True): # 가변인자 (변하는 인자, formal parameter)
      # 맨 마지막 인자에만 파라미터의 값을 지정# (default parameter, 입력안하면 디폴트로 지정한 값으로)
      data = a + b
      if data > 10 and c:
          return data
      else:
          return 0
  
  print(my_default(10,20))
  print(my_default(10,20,False)) # 10,20 실인자 (실제 있는 인자, real parameter)
  ```

  - Python의 함수의 인자는 mutable(불변), immutable(가변) 둘 중 하나

  - Python에서 함수에 인자를 전달하고 함수는 그 전달된 인자를 받음

  - 실인자의 데이터가 변하는 immutable

  - 실인자의 데이타가 변하지 않는 mutable

  - ```python
    def my_func(tmp_number, tmp_list):
        tmp_number = tmp_number + 100
        tmp_list.append(100)
    
    data_x =10 # numeric
    data_list =[10] #list
    
    my_func(data_x,data_list)
    print(data_x) # 원본에 변화가 없음 == immutable (숫자, 문자열, tuple)
    print(data_list) # 리스트(원본)에 값 추가됨 == mutable (list, dict)
    ```

###### 내장 함수

- id 함수

  - 객체의 고유 주소값을 return하는 함수

  - ```python
    my_list = [1,2,3,4]
    print(id(my_list))
    
    #3187732091848
    ```

- lambda 함수

  - 함수와는 다르지만 함수의 역할을 수행
  - 한줄로 함수를 정의하는 방법
  - 함수의 이름이 없음(anonymous function)
  - 이름없이 사용방법
    - 이름이 없기 때문에 변수에 저장, 함수의 인자로 사용
    - 함수의 결과값(리턴값)으로 함수를 리턴
    - first class

  ```python
  my_lambda = lambda x1,x2,x3 : x1+x2+x3 #
  # 람다가 함수와 다른점은 람다는 대체식
  ```