# torch.randn ##
----------------

## 형태 및 설명 ##
* torch.randn(**size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False*) → Tensor
* 평균이 0이고 분산이 1인 normal distribution에서 random한 수를 가져와 채운 tensor를 반환한다.
* tensor의 shape는 size 변수에 의해 결정된다.

## Parameters ##
* size(*int...*) - output tensor의 shape를 결정하는 정수형의 sequence. list, tuple과 같은 collection일 수도 있고 argument의 다양한 number일 수 있다.
* out(*Tensor, optional*) - the output tensor.
* dtype(*torch.dtype, optional*) - return될 tensor의 정해진 data type. 기본값으로 global default를 사용한다.
* layout(*torch.layout, optional*) - return될 tensor의 정해진 layout. 기본값으로 torch.strided를 사용한다.
* device(*torch.device, optional*) - return될 tensor의 정해진 device. 기본값으로 default tensor type을 위한 현재 device를 사용한다. device는 CPU tensor type들을 위한 CPU, 현재 CUDA device를 위한 CUDA tensor type들이다.
* requires_grad(*bool, optional*) - return된 tensor에 autograd operation을 기록해야 한다. 기본값은 False.

## 예제 ##
```python
import torch

torch.randn(4)
# tensor([-2.1436,  0.9966,  2.3426, -0.6366])

torch.randn(2, 3)
# tensor([[ 1.5954,  2.8929, -1.0923],
#         [ 1.1719, -0.4709, -0.1996]])
```

-------------------
## 출처 ##
* <https://pytorch.org/docs/stable/generated/torch.randn.html>