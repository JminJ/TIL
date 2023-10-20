# OverflowError: out of range integral type conversion attempted
- tokenizer로 trainer내에서 나온 labels를 decode 하던 도중 해당 에러가 발생하였다.
- 이는 trainer에서 labels pad작업을 수행할 때 pad id를 -100으로 주기 때문에 범위에 맞지 않는 값을 decode하려고 하기 때문에 에러가 발생한 것이다.
```Python
from transformers import AutoTokenizer

tokenzier = AutoTokenizer.from_pretrained("...")

try:
    converted_result = tokenizer.convert_ids_to_tokens(-100)
except Exception as E:
    print("error occur")
    print(E)
```
