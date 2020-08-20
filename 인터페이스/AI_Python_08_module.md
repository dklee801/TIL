# 08_Python_module

> Python에서 module은 함수나 변수 또는 클래스를 모아놓은 파일을 지칭
>
> - 다른 Python 파일에서 불러와서 사용할 수 있음.
> - 코드의 재사용성과 관리목적으로 사용



###### Python의 모듈은 2가지

- C언어로 구성된 binary module
- Python 언어로 구현된 일반 module



###### Module 을 사용하기 위해서 사용하는 keyword  = import

###### module도 Python에서 객체로 관리됨



```python
import sys

print(sys.path) #list

sys.path.append("c:/python_data") # module을 저장할 폴더를 지정
```



```python
import module1 as m1

print(m1.my_pi)

from module1 import * # 파일안에 있는 것 다땡겨오기
print(my_adder(10,20))

# c:/python_data안에 module.py를 저장.
# c:/python_data/test_module/module.py 로 다시 저장.

import test_mudule.module1 as my_module
print(my_module.my_pi)
```