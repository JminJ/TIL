# What is 'inf'?? #
----------------------------
### *'inf'* ###
* 어떠한 값을 뜻하며 다른 어떤 값보다도 큰 값을 말한다.(infinity)
* -inf의 값은 +inf와는 반대로 어떤 값보다고 작은 값을 말한다.

### 'inf' 확인하기 ###
* math package의 isinf() 함수를 사용하면 확인이 가능하다.
```python
import math

a = float('inf')

if math.isinf(a):
    print('a is inf!')
else:
    print("a isn't inf...")
```

-------------------
### 출처 ###
* <https://shydev.tistory.com/8>
* <https://shydev.tistory.com/9>