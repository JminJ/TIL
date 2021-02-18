# Vocab make methods #
------------
> **vocab**
>>단어와 해당 단어의 인덱스를 가지고 있는 사전.

## Methods ##
### Chracter level ###
Chracter 단위로 vocab을 만드는 방법이다. 한국어를 기준으로 보면 자음, 모음 단위로 vocab을 나누거나 글자['가', '갸',....,'힣']와 같이 가능한 모든 글자를 단위로 해 vocab을 나누는 것이다.

모든 글자를 vocab으로 표현하는 것이 가능하지만 ***각 단어 고유한 의미를 표현하고 있지 않으므로 좋은 성능을 내지 못하는 경우가 많다.***

### Space level ###
띄어쓰기 단위로 vocab을 만드는 방법. 띄어쓰기로 할 경우 한국어의 경우 조사 또는 어미 등으로 인해 중복단어 문제가 발생해 버린다. '책'이라는 단어로 예를 들어보면 ['책이', '책을', '책과',...]과 같이 나타나므로 이 ***모든 단어들을 vocab으로 만들 경우 vocab이 매우 커지게 되고 빈도수가 낮은 단어들은 학습이 잘 되지 않는다.*** 

### Subword level ###
많은 단어를 처리하면서도 vocab에 해당 단어가 없어 unknown이 발생할 확률을 줄이는 방법으로 단어의 빈도수를 계산해 subword 단위로 쪼개는 방법이다. Byte Pair Encoding을 보면 더 자세히 알 수 있다. 이 기능을 쉽게 처리하기 위해 google에서는 sentencepiece라는 툴을 제공한다.

----------
### 출처 ###
* <https://paul-hyun.github.io/vocab-with-sentencepiece/>