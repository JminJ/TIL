# torch.nn.Tanh #
---------

## 형태 및 설명

- torch.nn.Tanh
- element-wise 함수를 적용한다.

<img src = "/image/2021_02_24_02.png" width = '65%'>

## Shape

- Input(*N, **) - *의 뜻은 임의의 추가 차원 수.
- Output(*N, **) - input과 같은 차원 수.

<img src = "/image/2021_02_24_03.png" width = "80%">

## 예제

```python
import torch.nn as nn

m = nn.Tanh()
input = torch.randn(2)
output = m(input)
```

--------
### 출처 ###
* <https://pytorch.org/docs/stable/generated/torch.nn.Tanh.html>