## AI 융복합과정 2일차

## 인터페이스 개발

### 20.07.15

### 

#### 제어문 / 함수



###### Python의 입출력

- input(" ")

###### Print 함수는 한줄 출력 후 line feed(줄바꿈) 수행

print("a" , end = " ") 

#end = "문자"로 대체할 수 있음



###### control statement (제어문)

1. if문

- Python의 형태는 두가지로

- 전통적인 if ~ elif ~ else

  ```python
  a = 10
  if a % 3 == 0:
      pass # *아무것도 안하고 종료
  elif a % 5 ==0:
      print("5의 배수")
  else: print("3의 배수도 5의 배수도 아님")
  ```

- in을 이용한 구문

  ```python
  my_list = ["서울", "인천", "부산"]
  if "수원" in my_list:
      print("포함")
  else:
      print("미포함")
  ```

  

2. for문

- for문은 2가지 형태로 사용
- for ~ in range () # 반복회수 지정
- for  ~ in list, tuple, dict, ...# 집합자료의 데이터 수만큼

```python
# 1부터 100까지의 합 구하기
my_sum = 0
for tmp in range(1,101,1):
    my_sum += tmp
print("누적값: {}".format(my_sum))

# 집합 자료형 for 문
my_list = {"서울", "부산", "인천"}
for tmp in my_list:
    print(tmp)

# tuple관련 예
total = 0
my_data = [(1, 2), (3, 4), (5, 6)]
for (tmp1, tmp2) in my_data:
    total += (tmp1 + tmp2)
print(total)
```

- list comprehension
  - Python에만 있음
  - 하나의 자료형으로 리스트를 쉽게 생성하는 방법 중 하나

```python
my_list = [1, 2, 3, 4, 5]
goal = [2, 4, 6 , 8, 10]

# 일반적인 for문
result = []
for tmp in my_list:
    result.append(tmp*2)
print(result)

# *** list comprehension
my_list = [1, 2, 3, 4, 5]
goal = [tmp * 2 for tmp in my_list]
print(goal)

# 짝수만 뽑아내기
goal = [tmp for tmp in my_list if tmp%2 == 0]
print(goal)
```

- while

  - 조건 만족할 때까지

  - ```python
    idx = 0
    while idx <10:
        print("현재 idx : {}".format(idx))
        idx += 1
    ```