# Hello world!
## Install Mojo(Mac 기준)
macOS Apple silicon을 기준으로 작성되었습니다.

1. Homebrew를 설치해 줍니다(설치가 되어있지 않았을 경우).
2. 아래 커맨드를 통해 Modular CLI를 설치합니다.
    ```zsh
    curl https://get.modular.com | sh - && \
    modular auth mut_3089b3d3d28c40e39bd1fc3c6ed702bd
    ```
3. 아래 커맨드를 통해 Mojo SDK를 설치합니다.
    ```zsh
    modular install mojo
    ```


### Hello World 예제를 시작하기 전에..
MODULAR_HOME, PATH 환경변수 세팅을 modular install mojo 명령어의 output으로 나온대로 적용을 해주셔야 합니다. bash 또는 zsh를 사용하신다면 아래 명령어를 설정파일(.bash_profile, .bashrc, .zshrc)에 추가해 주세요.
```zsh
export MODULAR_HOME="$HOME/.modular"
export PATH="$MODULAR_HOME/pkg/packages.modular.com_mojo/bin:$PATH"
```
추가 후, source 명령어를 통해 적용해 주세요.
```zsh
source ~/.zshrc
```

## Run code in the REPL
먼저 Mojo REPL에서 mojo 코드를 실행해 보겠습니다.
1. REPL 세션을 시작하기 위해, `mojo`를 터미널에 입력하고 `Enter`를 눌러주세요.
2. 이후, `print("Hellom world!")`를 입력하고 `Enter`를 눌러주세요.
```
$ mojo
Welcome to Mojo! 🔥

Expressions are delimited by a blank line.
Type `:quit` to exit the REPL and `:mojo help` for further assistance.

1> print("Hello, world!")
2.
Hello, world!
```

## Build and Mojo source files
Mojo 코드를 작성하고 실행시켜 보겠습니다:

1. `hello.mojo`(또는 `hello.🔥`)의 이름으로 파일을 생성하고 아래 코드를 입력해 줍니다:
    ```mojo
    fn main():
        print("Hello, world!")
    ```
2. 저장 후, `mojo` 커맨드로 실행시킵니다:
    ```zsh
    mojo hello.mojo
    ```

## Build an executable binary
이번에는 excutable을 생성 및 실행해 봅니다:

1. `build`커맨드를 통해 stand-alone excutable로 만들어줍니다.
    ```
    mojo build hello.mojo
    ```
    `.mojo`파일의 이름과 동일한 이름으로 executable이 생성됩니다. 이는 `-o`옵션을 통해 변경이 가능합니다.
2. excutable을 실행합니다:
    ```
    ./hello
    ```

## 번외: vscode Mojo세팅
1. Extensions에서 Mojo를 검색 후 `Mojo 🔥`를 설치해 줍니다.
2. .mojo파일을 생성 후 vscode에서 작업할 경우 `Mojo: Modular Home Path`를 설정 혹은 install하라고 경고가 뜰 텐데 우리는 이미 SDK를 설치, 환경변수 작업까지 완료해 주었기 때문에 경로를 세팅해 주겠습니다.

    1. 터미널을 열어 `$MODULAR_HOME`을 입력해 줍니다.
    2. `pwd` 명령어를 통해 현재 주소를 확인 후 `Mojo: Modular Home Path`에 입력해 줍니다.
-----
### 참고
* https://docs.modular.com/mojo/manual/get-started/hello-world.html