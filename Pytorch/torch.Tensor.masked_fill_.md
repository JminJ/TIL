# torch.Tensor.masked_fill_ #
-------
## 형태 및 설명 ##
* masked_fill_(mask, value)
* mask가 True인 부분을 self tensor의 value로 채운다. mask의 shape는 underlying tensor의 shape와 broadcastable할 수 있어야 한다.

## Parameters ##
* mask(*BoolTensor*) - boolean 타입의 mask
* value(*float*) - 채워질 value값
------
## 출처 ##
* <https://pytorch.org/docs/stable/tensors.html>