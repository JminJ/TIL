# torch.unsqeeze #
---------------
## 형태 및 설명 ##
* torch.unsqeeze(*input, dim*) → Tensor
* 특별한 position에 삽입된 한 개의 dimension과 함께 새로운 tensor가 return된다.
* return되는 tensor는 같은 underlying data를 this tensor와 공유.
>
## Parameters ##
* input(*Tensor*) - input tensor
* dim(*int*) - insert되어야 하는 단독 dimension의 index
>
## 예제 ##
```python
import torch

x = torch.tensor([1, 2, 3, 4])
torch.unsqueeze(x, 0)
# tensor([[ 1,  2,  3,  4]])

torch.unsqueeze(x, 1)
# tensor([[ 1],
#        [ 2],
#        [ 3],
#        [ 4]])
```
-------
## 출처 ##
* <https://pytorch.org/docs/stable/generated/torch.unsqueeze.html>