# OOV_Problem #
------
## OOV ##
* OOV는 Out-Of-Vocabulary의 줄임말이며 기계가 알고있는 단어들의 집합 중 미처 배우지 못한 단어들을 부르는 말이다.
>
## OOV_Problem ##
* OOV_Problem란 기계가 모르는 단어, 즉 OOV에 대처하지 못하는 상황이 있을 시 이 상황을 OOV_Problem라고 부른다. 이 문제는 단어 분리 방법으로 해결할 수 있다.
>
## 단어 분리 방법 ##
**WPM**
* 하나의 단어를 내부 단어들로 분리하는 단어 분리 모델
* 기존의 띄어쓰기를 _로 바꾸고 단어는 내부단어로 통계에 기반해 띄어쓰기로 분리한다.
> Jet makers feud over seat width with big orders at stake
->
***_J et _makers _fe ud _over _seat _width _with _big _orders _at _stake***
* 기존 문장의 띄어쓰기를 _로 치환하는 이유는 복원을 하기 위한 장치라고 한다.
* *변환 후 기존 문장으로 바꾸는 방법은 변환 된 문장의 띄어쓰기를 모두 제거하고 _를 띄어쓰기로 바꾸면 된다.*
>
**BPE(Byte_Pair_Encoding)**
* 가장 많이 등장한 문자열에 대해 병합하는 작업을 반복한다. 원하는 단어 집합의 크기(단어의 개수)가 될 때까지 위 작업을 반복한다.
```python
import re
import collections
from Ipython.display import display, Markdown, Latex

def get_stats(dictionary):
    # 유니그램의 pair들의 빈도수를 카운트
    pairs = collections.defaultdict(int)
    for word, freq in dictionary.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i],symbols[i+1]] += freq
    print('현재 pair들의 빈도수 :', dict(pairs))
    return pairs

def merge_dictionary(pair, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out

bpe_codes = {}
bpe_codes_reverse = {}

for i in range(num_merges):
    display(Markdown("### Iteration {}".format(i + 1)))
    pairs = get_stats(dictionary)
    best = max(pairs, key=pairs.get)
    dictionary = merge_dictionary(best, dictionary)

    bpe_codes[best] = i
    bpe_codes_reverse[best[0] + best[1]] = best

    print("new merge: {}".format(best))
    print("dictionary: {}".format(dictionary))
```
----------
## 출처 ##
* <https://wikidocs.net/22592>
* <https://omicro03.medium.com/자연어처리-nlp-5일차-단어-분리-60b59f681eb7>