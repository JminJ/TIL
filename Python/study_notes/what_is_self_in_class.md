# What is "self" in class
## Self in class
```python
>>> class Student:
...     def greet(self, name):
...         print(id(self))
...         print('Good Morning, ' + name)
... 
>>> student = Student()
>>> student.greet('John')
4546580944
Good Morning, John
>>> id(student)
4546580944
```

위 코드를 보면 Student라는 class가 있고 Student 내에는 greet라는 method가 존재하는 것을 확인 할 수 있다. 

주의깊게 확인해야 하는 부분은 **print(id(self))**, Student class type으로 선언된 student라는 instance의 id가 동일하다는 점이다. 
* 즉, greet method의 인자 self는 자신 class를 사용하는 instance이다.


위 사실을 증명해주는 또 다른 예시를 아래에 기입해 본다.
```python
>>> Student.greet(student, 'John')
Good Morning, John
```
위 예시는 student라는 instance내의 instance method인 greet를 사용하는 것이 아닌 Student class 자체의 greet method를 사용한 예시이다. self인자 자리에 instance인 student가 들어가 있는 것을 확인할 수 있을 것이다.
* 또 하나 중요한 내용은 instance student 자체에서 greet method를 가지고 있는 것이 아니라 Student class의 greet를 호출해 사용한다는 것이다. (자세한 설명은 하단 출처를 참고하자)

<img src="/image/2022_11_29_01.png" width="70%">

## Is self a Keyword?
* Keyword? : 파이썬에서 이미 예약되어있는 문자열로서 다른 용도로 사용이 불가능한 문자열이다.

특정 이름이 Keyword인지 확인하는 가장 쉬운 방법은 그 이름으로 변수를 선언해 보는 것이다.
```python
>>> def=5
  File "<stdin>", line 1
    def=5
       ^
SyntaxError: invalid syntax
>>> class=4
  File "<stdin>", line 1
    class=4
        ^
SyntaxError: invalid syntax
>>> self=3
```
위의 예시에서 확인 가능한 것처럼 self는 Keyword에 포함되어있지 않으며 self라는 이름 대신 다른 이름을 사용할 수 있다.

```python
>>> class Teacher:
...     def say_hello(professor, name):
...         print('Hello, ' + name)
...
>>> teacher = Teacher()
>>> teacher.say_hello('John')
Hello, John
```

```
Note) 그러나, 위 코드처럼 self대신 professor로 코드를 작성하는 것은 다른 사람의 가독성을 위해 사용하지 않는 것이 좋다.
```
-----
### 출처
* [Unlock the 4 Mysteries of self in Python](https://betterprogramming.pub/unlock-the-4-mysteries-of-self-in-python-d1913fbb8e16)
