# 06_fisrtclass / closure

## 

### First class

- 1급 시민



##### 프로그램의 구성요소(개체, 값,객체, 함수)가 다음 조건을 만족하면 first citizen이라고 함

1. 구성요소가 변수나 데이터구조의 속성으로 저장될 수 있다.
2. 함수의 인자로 전달될 수 있다.
3. 함수의 결과로 리턴될 수 있다.



- 일반적으로 사용하는 숫자타입의 데이터
  - 변수에 저장 가능
  - 함수의 인자로 넘겨줄 수 있고, 함수의 결과로 리턴될 수 있음
  - 그러므로 일반 숫자는 일급 시민



- 객체( class 로 부터 파생된 instance)
  - Python에서 사용되는 객체는 1급 시민의 조건을 만족 = 1급 객체



- 함수

  - 일급 시민의 조건에 만족한다면, 일급 함수(first class function)

  - Python은 일급함수를 지원함.

  - 함수를 runtime(실시간)으로 생성할 수 있다.

    ###### 1. 함수를 변수에 저장할 수 있음.

    ```python
    def my_add(x,y):
        return x + y
    
    print(my_add) # 함수의 주소값 출력
    f = my_add # 함수를 변수에 저장
    print(f(100,200))
    ```

    

    ###### 2. 함수를 다른 함수의 인자로 전달할 수 있음.

    ```python
    def my_add(x,y):
        return x + y
    ```

    함수가 하는일을 인자인 함수로 받음

  - ```python
    def my_operation(func, arg_list):
        result = []
    
        for (tmp1,tmp2) in arg_list:
            result.append(func(tmp1,tmp2))
    
        return result
    
    data = [(1, 2), (3, 4), (5, 6)]
    print(my_operation(my_add,data))
    ```

    ###### func 만 수정하면 되기 때문에 유지보수 차원에서 편리하게 수정



###### 				3. 함수를 다른 함수의 return 값으로 사용할 수 있음.

​					> closure라는 개념도 이해해야함.

```python
def add_maker(x): # x는 지역변수로 함수가 호출되면 생성되고 함수가 종료되면 없어짐

    def my_add_maker(y):
        return x + y

    return my_add_maker

add_5 = add_maker(5) # x는 return my_add_maker할 때 사라져야하는데 closure 때문에 남아있음.
add_10 = add_maker(10)
print(add_10(100)) # x가 남아있음, 동적으로(runtime) 함수를 만들어 낼수 있음.
```

- #### Closure

  - first class function(일급함수)의 개념을 이용하여
  - 스코프에 묶인 변수를 바인딩 하기 위한 기술을 의미
  - closure는 데이터를 저장한 레코드
  - 스코프안의 변수가 소멸되어도 그에 대한 접근을 closure를 통해서 할 수 있음.
  - closure의 도움을 받아 런타임시에 내가 필요한 함수를 만들어 낼 수 있음.