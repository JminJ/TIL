# torch.matmul #
--------
## 형태 및 설명

- torch.matmul(*input, other, *, out=None*) → Tensor
- 두 개의 tensor의 행렬 곱(Matrix product).
- 이 작업은 아래 나열되어있는 tensor의 차원에 의해 정해진다.
- 이 연산자(operator) TensorFloat32를 지원한다.

1. 만약 양 tensor들이 1-dimensional이면, 내적(scalar)이 반환된다.
2. 만약 양 tensor들이 2-dimensional이면, matrix-matrix 연산이 반환된다.
3. 만약 첫 번째 argument가 1-dimensional이고 두 번째 argument가 2-dimensional이면, 행렬 곱셈을 위해 차원 앞에 1이 추가된다. 행렬 곱 이후, 추가된 차원은 제거된다.
4. 만약 첫 번째 argument가 2-dimensional이고 두 번째 argument가 1-dimensional이면, matrix-vector 연산이 반환된다.
5. 만약 양 argument들이 적어도 1-dimensional이고 적어도 한 argument가 N-dimensional (where N > 2)이면, batched matrix multiply가 반환된다. 만약 첫 번째 argument가 1-dimensional이면, 1은 batched martix multiply를 위해 차원 앞에 추가되고 이후에 제거된다. 두 번째 argument가 1-dimensional이면, 1은 batched martix multiply를 위해 차원 앞에 추가되고 이후에 제거된다. non-martix(i.e batch) 차원들은 broadcast 된다. 예를 들어 input이 (j X 1 X n X m) tensor이고 other이 (k X m X p) tensor이면, out은 (j X k X n X p) tensor가 된다.

## Parameters

- input(*Tensor*) - 곱해질 첫 번째 tensor
- other(*Tensor*) - 곱해질 두 번째 tensor

## Keyword Arguments

- out(*Tensor, optional*) - the output tensor.

## 예제

```python
import torch

# vector x vector
tensor1 = torch.randn(3)
tensor2 = torch.randn(3)
print(torch.matmul(tensor1, tensor2).size())
# torch.Size([])

# matrix x vector
tensor1 = torch.randn(3, 4)
tensor2 = torch.randn(4)
print(torch.matmul(tensor1, tensor2).size())
# torch.Size([3])

# batched matrix x broadcasted vector
tensor1 = torch.randn(10, 3, 4)
tensor2 = torch.randn(4)
print(torch.matmul(tensor1, tensor2).size())
# torch.Size([10, 3])

# batched matrix x batched matrix
tensor1 = torch.randn(10, 3, 4)
tensor2 = torch.randn(10, 4, 5)
print(torch.matmul(tensor1, tensor2).size())
# torch.Size([10, 3, 5])

# batched matrix x broadcasted matrix
tensor1 = torch.randn(10, 3, 4)
tensor2 = torch.randn(4, 5)
print(torch.matmul(tensor1, tensor2).size())
#torch.Size([10, 3, 5])
```

---

### 출처

- [https://pytorch.org/docs/stable/generated/torch.matmul.html](https://pytorch.org/docs/stable/generated/torch.matmul.html)