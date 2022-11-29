# endswith #
--------
## 형태 및 설명 ##
* endswith(*end_of_char, start_string, end_string*)
* endswith(끝나는 문자, 문자열의 시작, 문자열의 끝)
* 문자열이 특정 문자로 끝나는지 여부를 알려준다.

## 예제 ##
```python
str = '가나다라 마바사아 자차카타'
str.endswith('마')
# False

str.endswith('마',0,6)
# True
```
-------------
### 출처 ###
* <https://dpdpwl.tistory.com/119>