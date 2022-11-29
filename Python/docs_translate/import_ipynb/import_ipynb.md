# import_ipynb 간단 사용법 및 소개 #
------------------
## ipynb? ##
* ipynb란 jupiter notebook 또는 google colab에서 사용되는 파일 형식이다. 
* json 일반 텍스트 형식으로 저장된다.

## .py 파일에서 다른 파일을 불러오던 방법 ##
* 라이브러리들을 import 하듯 ***import 파일 이름*** 처럼 import를 하면 사용이 가능하다.
* 그러나 .ipynb 파일은 이 방식으로 하면 import가 되지 않는다.

## 그럼 어떻게 import 하지? ##
* 'import_ipynb'라는 라이브러리가 파이썬에는 존재한다. 이름에서 느껴지듯 .ipynb 파일을 import 해주는 고마운 라이브러리다.
> **사용법**
>```python
>!pip install import_ipynb
>```
> 이 명령어를 통해 ipynb 파일 내에서 install이 가능하다.
> install 한 뒤 아래의 명령어를 차례로 적어주면 된다.
>```python
>import import_ipynb
>import file_name # .ipynb를 붙이지 않는다!

--------------
### 참고 ###
* <https://seobway.tistory.com/entry/ipynb-file-import-%EB%B0%A9%EB%B2%95>

감사합니다:)