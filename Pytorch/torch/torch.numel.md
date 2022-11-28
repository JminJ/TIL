# torch.numel #
--------
## 형태 및 설명 ##
* torch.numel(*input*) → int
* input tensor 안에 있는 모든 element의 number를 return 해준다.
>
## Parameters ##
* input(*Tensor*) - input tensor
>
## 예제 ##
```python
import torch

a = torch.randn(1, 2, 3, 4, 5)
torch.numel(a)
# 120

a = torch.zeros(4,4)
torch.numel(a)
# 16
```
-------
## 출처 ##
* <https://pytorch.org/docs/stable/generated/torch.numel.html>