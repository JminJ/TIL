# torch.expand #
----------
## 형태 및 설명 ##
* expand(*\*size*) → Tensor
* 개체 dimension이 더 크게 확장된 self tensor의 새로운 view를 return한다.
* -1이 dimension의 size로 들어올 경우 이는 dimension의 사이즈를 바꾸지 말라는 의미를 뜻한다.
* ***이 함수를 사용해 새로운 tensor를 만들고 싶다면 대상 tensor를 복사한 후 그 tensor를 이용해 만들어야 한다.***
>
## Parameters ##
* *size(*torch.Size or int...*) - 확장되기 원하는 size
>
## 예제 ##
```python
import torch

x = torch.tensor([[1], [2], [3]])
x.size()
# torch.Size([3, 1])
x.expand(3, 4)
# tensor([[ 1,  1,  1,  1],
#        [ 2,  2,  2,  2],
#        [ 3,  3,  3,  3]])

x.expand(-1, 4)   # -1 means not changing the size of that dimension
# tensor([[ 1,  1,  1,  1],
#        [ 2,  2,  2,  2],
#        [ 3,  3,  3,  3]])
```
------------
## 출처 ##
* <https://pytorch.org/docs/stable/tensors.html>