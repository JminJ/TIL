# startswith #
-------------
## 형태 및 설명 ##
* string1.startswith(*str, beg = 0, end = len(string)*)
* 괄호 안에 적은 문자열로 시작하는지를 확인
* True, False를 반환
* 문자열만 적을 시 전체에서 찾는다.

## 예제 ##
```python
string = 'hello!'
print(string.startswith('!'))
# False
print(string.startswith('!', 5))
# True
```

-------------
### 출처 ###
* <https://m.blog.naver.com/PostView.nhn?blogId=shwotjd14&logNo=221501880837&categoryNo=9&proxyReferer=https:%2F%2Fwww.google.com%2F>