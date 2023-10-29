## OverflowError: out of range integral type conversion attempted
- tokenizer로 trainer내에서 나온 labels를 decode 하던 도중 해당 에러가 발생하였다.
- 이는 trainer에서 labels pad작업을 수행할 때 pad id를 -100으로 주기 때문에 범위에 맞지 않는 값을 decode하려고 하기 때문에 에러가 발생한 것이다.
### 참고
- https://github.com/huggingface/transformers/blob/main/src/transformers/trainer.py#L3137C94-L3137C94