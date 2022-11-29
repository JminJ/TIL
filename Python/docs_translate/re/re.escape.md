# re.escape #
----------
## 형태 및 설명 ##
* re.escape(*string*) - 영문자, 숫자가 아닌 문자에 대해 백슬러시 문자를 추가한다. 메타문자를 포함한 문자열을 정규식으로 변경할 수 있다.
>
## Parameters ##
* string - 변환될 문장
>
## 예제 ##
```python
import re
print re.escape("Hello 123 .?!@ World")

# Hello\ 123\ \.\?\!\@\ World
```
---------
## 출처 ##
* <https://greeksharifa.github.io/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D(re)/2018/08/24/regex-usage-09-other-functions/>
* <https://www.kite.com/python/docs/re.escape>