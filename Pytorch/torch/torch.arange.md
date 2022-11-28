# torch.arange #
--------
## 형태 및 설명 ##
* torch.arange(*start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False*) → Tensor
* 주어진 범위 내의 정수를 순서대로 생성한다.

## Parameters ##
* start(*Number*) - point의 set의 시작값. 기본값은 0.
* end(*Number*) - point set의 마지막 값.
* step(*Number*) - 인접 point 각 쌍 사이의 간격. 기본값은 1.

## Keyword Arguments ##
* out(*Tensor, optional*) - 출력 tensor.   
>

* dtype(*torch.dtype, optoinal*) - return되는 tensor의 원하는 data type. 기본값은 None이며 None일 경우 global default를 사용한다. 
만약 dtype이 주어지지 않으면 다른 input argument에서 date type을 추론한다. 또한 어느 start, end, stop이 floating-point일 경우 dtype은 default dtype일 것이라 추론한다. 
이 외의 경우, dtype은 torch.int64로 가정한다.
>

* layout(*torch.laypout, optional*) - return되는 Tensor의 원하는 layer. 기본값은 torch.strided.
> 
* requires_grad(*bool, optional*) - 만약 autograd면 operation을 return되는 tensor에 기록해야 한다. 기본값은 False.

## 예제 ##
```python
import torch

torch.arange(5)
# tensor([ 0,  1,  2,  3,  4])
torch.arange(1, 4)
# tensor([ 1,  2,  3])
torch.arange(1, 2.5, 0.5)
# tensor([ 1.0000,  1.5000,  2.0000])
```
--------------
## 출처 ##
* <https://pytorch.org/docs/stable/generated/torch.arange.html>
