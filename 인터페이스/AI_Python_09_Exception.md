# 09_Python exception



###### 예외 처리를 위한것.

### Error

- compile time error : 문법 오류
- runtime error : 실행 시 발생하는 오류

###### 

###### 어떤 runtime error들은 비정상 종료되지 않고 프로그램을 지속적으로 수행할 수 있는 방법이 있음.

> exception handling
>
> 오류 중 복구가능한 error



###### exception의 처리는 하나의 구문만 사용

###### 4개의 단어

- try

- except

- else

- finally

  

```python
def my_func(my_list):
    total_sum =0 # list안의 숫자들을 누적

    try:
        total_sum = my_list[0] + my_list[1] + my_list[2]
        print("try 가 수행됨")
        
    except Exception: #try 에서 수행한것이 오류가 발생했을때 except 이후 상황인 경우, (Exception은 모든 오류 지칭)
        print("오류가 존재함") # 예외처리를 해야함.

    else:# try에서 오류가 없을 경우
        print("오류 없음")

    finally: # 오류가 있던 없던 수행
        print("무조건 수행됨")

my_func((1, 2))
```