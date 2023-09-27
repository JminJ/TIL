# Tensors
* 배열, 행렬과 매우 유사한 특수한 자료구조를 가진다. -> pytorch에서는 텐서를 사용해 모델의 input, output, parameter를 encode한다.
* GPU나 다른 하드웨어 가속기에서 실행할 수 있다는 점을 제외하면 numpy의 ndarray와 유사하다. -> 실제로 tensor와 ndarray끼리 종종 동일한 내부 메모리를 공유할 수 있어 데이터를 복사할 필요가 없다.

## 속성(Attributes)
Tensor의 속성에는 1. shape, 2. dtype, 3. device가 있다.
```Python
tensor = torch.randn((2,3))

# 1. shape
print(tensor.shape)

# 2. dtype
print(tensor.dtype)

# 3. device
print(tensor.device)
```

## 연산(Operations)
Tensor 연산들은 GPU에서 이뤄질 수 있다. 기본적으로 tensor들은 CPU에 생성되고, .to를 통해 GPU로 Tensor들을 옮겨서 사용한다.
```Python
tensor = torch.randn((2,3))

# move to GPU
if torch.cuda.is_available()
    tensor = tensor.to("cuda")
```

### Standard numpy-like indexing and slicing
```Python
tensor = torch.ones(4, 4)
print(f"First row: {tensor[0]}")
print(f"First column: {tensor[:, 0]}")
print(f"Last column: {tensor[..., -1]}")
tensor[:,1] = 0
print(tensor)
```

### Joining tensors
torch.cat을 이용해 주어진 dimension으로 tensor의 sequence를 이어붙일 수 있다.
```Python
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)

# tensor([[1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.],
#         [1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.],
#         [1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.],
#         [1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.]])
```
또한 torch.stack을 통해서 torch.cat과는 다른 방식으로 이어붙이는 것도 가능하다.

### Arithmetic Operations
```Python
# 두 텐서의 matrix multiplication을 수행한다. y1. y2, y3은 모두 같은 값을 반환한다.
# tensor.T는 tensor의 transpose를 반환한다.
y1 = tensor @ tensor.T
y2 = tensor.matmul(tensor.T)

y3 = torch.rand_like(y1)
torch.matmul(tensor, tensor.T, out=y3)


# element-wise 곱을 연산한다. z1, z2, z3는 모두 같은 값을 반환한다.
z1 = tensor * tensor
z2 = tensor.mul(tensor)

z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)
```

### Single-element tensors
tensor내의 모든 값을 더한 것 처럼 tensor 내에 오직 한 값을 가진 경우, .item()을 사용해 Python numerical 값으로 변환시킬 수 있다.
```Python
agg = tensor.sum()
agg_item = agg.item()
print(agg_item, type(agg_item))

# 12.0 <class 'float'>
```

### In-place operations
연산 결과를 피연산자(operand)에 저장하는 연산을 in-place 연산이라고 부르며, \_를 붙인다. x.copy\_(y)나 x.t\_()는 x를 변경한다.
```Python
print(f"{tensor} \n")
tensor.add_(5)
print(tensor)

# tensor([[1., 0., 1., 1.],
#         [1., 0., 1., 1.],
#         [1., 0., 1., 1.],
#         [1., 0., 1., 1.]])

# tensor([[6., 5., 6., 6.],
#         [6., 5., 6., 6.],
#         [6., 5., 6., 6.],
#         [6., 5., 6., 6.]])
```

```
In-place 연산은 메모리를 일부 절약하지만, history가 즉시 삭제되어 derivative 연산에 문제가 생길 수 있으니 사용을 권장하지 않는다고 한다.
```

## Bridge with NumPy 
CPU상의 텐서와 NumPy 배열은 메모리 공간을 공유하기 떄문에, 하나를 변경하면 다른 하나도 변경된다.

### Tensor to NumPy array
```Python
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

# t: tensor([1., 1., 1., 1., 1.])
# n: [1. 1. 1. 1. 1.]
```

tensor의 값에 변화를 주면 NumPy 배열에도 동일하게 적용이 된다.
```Python
t.add_(1)
print(f"t: {t}")
print(f"n: {n}")

# t: tensor([2., 2., 2., 2., 2.])
# n: [2. 2. 2. 2. 2.]
```

### NumPy array to Tensor
```Python
n = np.ones(5)
t = torch.from_numpy(n)
```

NumPy 배열의 값에 변화를 주면 tensor에도 똑같이 적용된다.
```Python
np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")

# t: tensor([2., 2., 2., 2., 2.], dtype=torch.float64)
# n: [2. 2. 2. 2. 2.]
```


------
### 출처
* https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html
* https://tutorials.pytorch.kr/beginner/basics/tensorqs_tutorial.html