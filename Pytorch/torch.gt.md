# torch.gt #
--------------
## 형태 및 설명 ##
* torch.gt(*input, other, *, out=None*) → Tensor
* input, other의 텐서에서 input값이 other값보다 큰 element를  True로 계산한다.
* 두 번째 argument는 number 혹은 tensor가 될 수 있다. (첫 번째 인자에 따라서)
>
## Parameters ## 
* input(*Tensor*) -비교할 tensor.
* output(*Tensor or float*) - 비교할 tensor 혹은 number.
>
## Keyword Arguments ##
* out(*Tensor, optional*) - output tensor.
>
## Returns ##
* boolean tensor는 input값이 output값보다 클 경우 True를 반환하고 이것이 아닐 경우 False를 반환한다.
>
## 예제 ##
```python
import torch

torch.gt(torch.tensor([[1, 2], [3, 4]]), torch.tensor([[1, 1], [4, 4]]))
# tensor([[False, True], [False, False]])
```
------
## 출처 ##
* <https://pytorch.org/docs/stable/generated/torch.gt.html>