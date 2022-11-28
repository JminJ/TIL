# Conda install in Homebrew
## install 
* homebrew 사이트에서 conda 설치 command를 확인할 수 있다.
* brew install --cask anaconda (22.11.28 기준)
## test
* conda
* 위 명령어를 통해 conda가 잘 설치 되었는지 확인이 가능하다.
```
Note) 만약 zsh: command not found: conda 라는 에러가 발생할 경우, anaconda의 경로를 지정해 주어야 한다. 아래 내용을 참고하자.
```
### zsh: command not found: conda 해결
* 해당 내용은 **zsh, homebrew**를 통해 anaconda를 설치 할 경우 참고해야 한다.
* homebrew를 통해 anaconda를 설치 할 경우 기본적으로 "/opt/homebrew/anaconda3" 위치로 설치가 진행된다.
* 따라서 ~/.zshrc 파일의 마지막 줄에 아래 command를 추가해 주면 정상적으로 터미널에서 conda를 사용이 가능하다.
* export PATH="/opt/homebrew/anaconda3/bin:$PATH"
-----
### 참고
* https://wizdom.tistory.com/15
* https://velog.io/@yoonene/Mac%EC%97%90%EC%84%9C-anaconda-%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98-%EC%84%A4%EC%A0%95