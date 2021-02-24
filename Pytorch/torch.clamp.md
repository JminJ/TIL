# torch.clamp #
-------
## 형태 및 설명

- torch.clamp(*input, min, max, *, out=None*) → Tensor
- 입력 중인 모든 요소를 [min, max] 범위로 고정하고 결과 텐서를 반환한다.

<img src = "/image/2021_02_24_01.png">

- 만약 input이 FloatTensor 혹은 DoubleTensor의 타입일 경우, 매개변수 min, max는 실수이어야 하고, 다른 경우는 정수여야 한다.

## Parameters

- input(*Tensor*) - the input tensor.
- min(*Number*) - 고정될 하계(주어진 집합의 어떤 원소보다 작거나 같은 원소)의 범위.
- max(*Number*) - 고정될 상계(주어진 집합의 어떤 원보다도 크거나 같은 값; 3과 4는 1,2,3을 원으로 하는 집합의 상계이다)의 범위.

## Keyword Arguments

- out(*Tensor, optional*) - the output tensor.

## 예제

```python
import torch

a = torch.randn(4)
print(a)
# tensor([-1.7120,  0.1734, -0.0478, -0.0922])
print(torch.clamp(a, min=-0.5, max=0.5))
# tensor([-0.5000,  0.1734, -0.0478, -0.0922])
```

출처 : [https://pytorch.org/docs/stable/generated/torch.clamp.html?highlight=clamp#torch.clamp](https://pytorch.org/docs/stable/generated/torch.clamp.html?highlight=clamp#torch.clamp)