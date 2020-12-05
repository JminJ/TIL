# torch.matmul #
--------
## 형태 및 설명 ##
* torch.matmul(*input, other, *, out=None*) → Tensor
* 두 tensor의 Matric product연산을 수행한다
>
## Parameters ##
* input(*Tensor*) - 곱해질 첫 번째 tensor.
* other(*Tensor*) - 곱해질 두 번째 tensor.
>
## Keyword Arguments ##
* out(*Tensor, optional*) - output tensor.
>
## 예제 ##
```python
import torch

# vector x vector
tensor1 = torch.randn(3)
tensor2 = torch.randn(3)
torch.matmul(tensor1, tensor2).size()
# torch.Size([])

# matrix x vector
tensor1 = torch.randn(3, 4)
tensor2 = torch.randn(4)
torch.matmul(tensor1, tensor2).size()
# torch.Size([3])

# batched matrix x broadcasted vector
tensor1 = torch.randn(10, 3, 4)
tensor2 = torch.randn(4)
torch.matmul(tensor1, tensor2).size()
# torch.Size([10, 3])

# batched matrix x batched matrix
tensor1 = torch.randn(10, 3, 4)
tensor2 = torch.randn(10, 4, 5)
torch.matmul(tensor1, tensor2).size()
# torch.Size([10, 3, 5])

# batched matrix x broadcasted matrix
tensor1 = torch.randn(10, 3, 4)
tensor2 = torch.randn(4, 5)
torch.matmul(tensor1, tensor2).size()
# torch.Size([10, 3, 5])
```
----------
## 출처 ##
* <https://pytorch.org/docs/stable/generated/torch.matmul.html>