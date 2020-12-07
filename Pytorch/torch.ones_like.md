# torch.ones_like #
--------
## 형태 및 설명 ##
* torch.ones_like(*input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format*) → Tensor
* input과 같은 size의 scalar 1로 채워진 tensor를 return해준다.
* ***torch.ones_like(input)는 torch.ones(input.size(), dtype=input.dtype, layout=input.layout, device=input.device)와 동일하다.***
>
## Parameters ##
* input(*Tensor*) - output tensor의 크기를 결정할 input의 size. (input은 Tensor이다.)
* dtype(*torch.dtype, optional*) - return되는 Tensor의 원하는 dtype. 기본값은 None이며 None일 시, input의 dtype으로 결정된다.
* layout(*torch.layout, optional*) - return되는 Tensor의 원하는 layout. 기본값은 None이며 None일 시, input의 layer으로 결정된다.
* device(*torch.device, optoinal*) - return되는 Tensor의 원하는 device. 기본값은 None이며 None일 시, input의 device으로 결정된다.
* requires_grad(*bool, optional*) - 만약 autograd이면 return되는 tensor에 operations를 기록한다. 기본값은 False이다.
* memory_format(*torch.memory_format, optional*) - return되는 Tensor의 원하는 memory format. 기본값은 torch.preserve_format.
>
## 예제 ##
```python
import torch

input = torch.empty(2, 3)
torch.ones_like(input)
# tensor([[ 1.,  1.,  1.],
#         [ 1.,  1.,  1.]])
```
--------------
## 출처 ##
* <https://pytorch.org/docs/stable/generated/torch.ones_like.html>