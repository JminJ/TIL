# torch.mm #
-----
## 형태 및 설명

- torch.mm(*input, mat2, *, out=None*) → Tensor
- input, mat2 matrix들의 matrix multiplication(행렬 곱)을 수행한다.
- input이 (n X m) tensor이고, mat2가 (m X p) tensor일 때, out은 (n X p) tensor이다.
- 이 연산자(operator)는 TensorFloat32를 지원한다.

## Parameters

- input(*Tensor*) - 곱해야 할 첫 번째 matrix
- output(*Tensor*) - 곱해야 할 두 번째 matrix

## Keyword Arguments

- out(*Tensor*) - the output tensor.

## 예제

```python
import torch

mat1 = torch.randn(2, 3)
mat2 = torch.randn(3, 3)

print(torch.mm(mat1, mat2))
# tensor([[ 0.4851,  0.5037, -0.3633],
#         [-0.0760, -3.6705,  2.4784]])
```

---

### 출처

- <https://pytorch.org/docs/stable/generated/torch.mm.html>