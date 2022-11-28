# torch.nn.utils.rnn.pad_sequence #
-------------------
## 형태 및 설명 ##
* **torch.nn.utils.rnn.pad_sequence(*sequence, batch_first = False, padding_value = 0.0*)**
* 서로 길이가 다른 Tensor들을 padding_value에 맞게 길이를 동일하게 수정한다.

## Parameters ##
* Tensor들을 padding_value에 맞게 길이를 동일하게 수정한다
* batch_first(bool, optional) - 만약 True인 경우 output이 **B x T x \*** 로 나온다. 다른 경우는 **T x B x \***.
* batch_first(bool, optional) - 만약 True인 경우 output이 B x T x * 로 나온다. 다른 경우는 T x B x *.

## 예제 ##
```python
from torch.nn.utils.rnn import pad_sequence

a = torch.ones(25, 300)
b = torch.ones(22, 300)
c = torch.ones(15, 300)

print(pad_sequence([a,b,c]).size())
# torch.Size([25, 3, 300])
```
----------
## 출처 ##
* <https://pytorch.org/docs/stable/generated/torch.nn.utils.rnn.pad_sequence.html>