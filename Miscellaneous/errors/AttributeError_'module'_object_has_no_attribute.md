# AttributeError:'module' object has no attribute... #
---------
### 에러 메시지 ###
```
Traceback (most recent call last):

  File "<pyshell#18>", line 1, in <module>

    t.foward(50)

AttributeError: 'module' object has no attribute 'foward'
```

### 발생 이유 ###
```
모듈의 함수나 변수를 잘못 입력했을 때 발생한다.
```

### 내 발생 이유 ###
```
colab에서 'import_ipynb'라 하는 라이브러리를 사용해 .ipynb 파일의 class를 받아 사용하는 작업을 하고 있었다. 
그러나 한 파일에서 class를 찾아오지 못했고 이 에러 메시지를 내보냈다.(그러나 class이름을 제대로 적었다...)
```

### 해결 방법 ###
```
함수나 변수의 철자와 대소문자가 올바른지 확인한 후 수정한다.
```

-------
### 출처 ###
* <https://thebook.io/007026/xa/02_04/>