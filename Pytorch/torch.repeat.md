# torch.repeat #
--------
## 형태 및 설명 ##
* repeat(*\* sizes*) → Tensor
* 특정한 dimension을 따라 this tensor를 반복한다.
>
## Parameters ##
* sizes(torch.Size or int... ) - 각 dimension에 따라 this tensor를 반복할 횟수.
>
## 예제 ##
```python 
import torch

x = torch.tensor([1, 2, 3])
x.repeat(4, 2)
#tensor([[ 1,  2,  3,  1,  2,  3],
#        [ 1,  2,  3,  1,  2,  3],
#        [ 1,  2,  3,  1,  2,  3],
#        [ 1,  2,  3,  1,  2,  3]])

x.repeat(4, 2, 1).size()
#torch.Size([4, 2, 3])
```
--------
## 출처 ##
* <https://pytorch.org/docs/stable/tensors.html>