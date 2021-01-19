# (torchtext) ValueError: too many dimensions 'str' #
----------------------
## Why? ##
* dataset의 field를 지정해주던 도중 id, label에 sequential = True를 주었기 때문
## Solution ##
* id, label field의 sequential 속성에 False를 넣어주면 해결된다.
----------
## 출처 ##
* <https://stackoverflow.com/questions/55550641/unable-to-load-one-hot-labels-in-a-torchtext-iterator-valueerror-too-many-dim>