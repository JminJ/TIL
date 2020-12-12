# torch.stack #
------------------
## 형태 및 설명 ##
* torch.stack(*tensors, dim=0, *, out=None*) → Tensor
* 새로운 dimension에 따라 tensor의 sequemce를 잇는다.
* ***모든 tensor는 같은 size를 필요로 한다.***
>
## Parameters ##
* tensors(*sequence of Tensors*) - 이어질 tensor의 sequence.
* dim(*int*) - 삽입될 dimension. ***0부터 이어질 tensor의 dimension의 number까지의 값을 가져야 한다.***
>
## Keyword Arguments ##
* out(*Tensor, optional*) - the output tensor.
------------------
## 출처 ##
* <https://pytorch.org/docs/stable/generated/torch.stack.html>