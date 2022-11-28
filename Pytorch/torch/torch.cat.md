# torch.cat #
-----

## 형태 및 설명

- torch.cat(*tensors, dim=0, *, out=None*) → Tensor
- 주어진 dimension에서 seq tensor들의 주어진 sequence들을 합친다.
- 모든 tensor들은 모두 같은 shape(합칠 dimension은 제외하고)거나 비어있어야 한다.
- torch.cat()은 torch.split()과 torch.chunk()와 반대되는 작업이라고 보여질 수 있다

## Parameters

- tensors(*sequence of Tensors*) - 같은 type의 tensor들의 python sequence. 제공된 Non-empty tensor는 cat 될 dimentsion을 제외하고 모두 같은 shape를 가져야 한다.
- dim(*int, optional*) - tensor들이 합쳐질 dimension

## Keyword Arguments

- out(*Tensor, optional*) - the output tensor.

## 예제

```python
import torch

x = torch.randn(2, 3)
print(x)
# tensor([[ 0.6580, -1.0969, -0.4614],
#         [-0.1034, -0.5790,  0.1497]])

print(torch.cat((x, x, x), 0))
# tensor([[ 0.6580, -1.0969, -0.4614],
#         [-0.1034, -0.5790,  0.1497],
#         [ 0.6580, -1.0969, -0.4614],
#         [-0.1034, -0.5790,  0.1497],
#         [ 0.6580, -1.0969, -0.4614],
#         [-0.1034, -0.5790,  0.1497]])

print(torch.cat((x, x, x), 1))
# tensor([[ 0.6580, -1.0969, -0.4614,  0.6580, -1.0969, -0.4614,  0.6580,
#          -1.0969, -0.4614],
#         [-0.1034, -0.5790,  0.1497, -0.1034, -0.5790,  0.1497, -0.1034,
#          -0.5790,  0.1497]])
```

-----
### 출처 ###

- [https://pytorch.org/docs/stable/generated/torch.cat.html](https://pytorch.org/docs/stable/generated/torch.cat.html)