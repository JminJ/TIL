# pipeline
-----
## normalizers

```python
from toknizers import normalizers
from tokenizers.normalizers import NFD, StripAccents

normalizer = normalizers.Sequence([NFD(), StripAccents()])
```

- normalizers는 말 그대로 raw data를 normalization 해주는 함수이다. Sequence()를 통해 여러 개의 normalization 함수를 동시에 적용이 가능하다.

```python
## normalizer 예제
normalizer.normalize_str("Héllò hôw are ü?")
# "Hello how are u?"

## tokenizer의 normalizer 교체 
tokenizer.normalizer = normalizer
```

## Pre-tokenization

- text를 word단위로 끊어 어느 부분이 training의 끝인지를 알 수 있게 해주는 방법이다.
- (영어 기준) 가장 쉬운 방법은 띄어쓰기 단위로 끊는 방법이다.

```python
from tokenizers.pre_tokenizers import Whitespace

pre_tokenizer = Whitespace()
pre_tokenizer.pre_tokenize_str("Hello! How are you? I'm fine, thank you.")
# [("Hello", (0, 5)), ("!", (5, 6)), ("How", (7, 10)), ("are", (11, 14)), ("you", (15, 18)),
#  ("?", (18, 19)), ("I", (20, 21)), ("'", (21, 22)), ('m', (22, 23)), ("fine", (24, 28)),
#  (",", (28, 29)), ("thank", (30, 35)), ("you", (36, 39)), (".", (39, 40))]
```

- 여러개의 Pre-tokenizer를 합쳐 사용하는 것 또한 가능하다.

```python
from tokenizers import pre_tokenizers
from tokenizers.pre_tokenizers import Digits

pre_tokenizer = pre_tokenizers.Sequence([Whitespace(), Digits(individual_digits=True)])
pre_tokenizer.pre_tokenize_str("Call 911!")
# [("Call", (0, 4)), ("9", (5, 6)), ("1", (6, 7)), ("1", (7, 8)), ("!", (8, 9))]
```

- 위릐 normalizers처럼 tokenizer의 pre-tokenizer를 바꿀 수 있다.

```python
tokenizer.pre_tokenizer = pre_tokenizer
```

## The-model

- tokenizer가 normalize와 pre-tokenization을 수행했다면 이제 pre-token에 model을 적용해야 한다.
- 이 model의 role은 word를 미리 학습된 방법으로 "token"의 형태로 나누는 것이다. 나눠진 token들은 model 내의 vocabulary에 있는 동일한 token의 ID들로 mapping된다.
- 🤗 tokenizer에서 지원하는 model들은 아래와 같다.

```
* BPE
* WordLevel
* Unigram
* WordPiece
```

## Post-Processing

- post-processing 작업은 tokenizer의 마지막 작업이다. return 되기 전에 추가적인 token을 추가하는 등 transformation 작업을 더 해주는 것이다.

```python
from tokenizers.processors import TemplateProcessing

tokenizer.post_processor = TemplateProcessing(
    single="[CLS] $A [SEP]",
    pair="[CLS] $A [SEP] $B:1 [SEP]:1",
    special_tokens=[("[CLS]", 1), ("[SEP]", 2)],
)
```

- 위 예시는 BERT에 들어가는 input에 맞게 post-processing 작업을 해준 것이다.

---

### 출처

- [https://huggingface.co/docs/tokenizers/python/latest/pipeline.html](https://huggingface.co/docs/tokenizers/python/latest/pipeline.html)