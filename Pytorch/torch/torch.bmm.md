# torch.bmm #
--------------
## 형태 및 설명 ##
* torch.bmm(*input, mat2, *, deterministic=False, out=None*) → Tensor
* 적재된 input과 mat2 matrix들의 batch matrix-matrix 연산을 수행한다. (행렬곱)
* input과 mat2는 서로 같은 matrice들의 number를 포함하고 있는 3-D tensor이어야 한다.
* 만약 input이 (b × n × m) tnesor이고, mat2가 (b × m × p) tensor 이면, out은 (b × n × p)tensor가 될 것이다.
* 이 연산은 TensorFloat32를 지원한다.

## Parameters ##
* input(*Tensor*) - 첫 번째 곱해질 matrice들의 batch.
* mat2(*Tensor*) - 두 번째 곱해질 martice들의 batch.

## Keyword Arguments ##
* deterministic(*bool, optional*) - 더 빠른 non-deterministic 연산 또는 느린 deterministic 연산 사이에서 고른 신호. 이 argument는 오직 sparse-dense CUDA bmm에서 사용할 수 있다. 기본값은 False.
* out(*Tensor, optional*) - the output tensor.

## 예제 ##
```python 
import torch

input = torch.randn(10, 3, 4)
mat2 = torch.randn(10, 4, 5)

res = torch.bmm(input, mat2)

res.size()
# torch.Size([10, 3, 5])
```

------------------
## 출처 ##
* <https://pytorch.org/docs/stable/generated/torch.bmm.html>