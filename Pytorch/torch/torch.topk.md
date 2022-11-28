# torch.topk #
--------------
## 형태 및 설명 ##
* torch.topk(*input, k, dim=None, largest=True, sorted=True, *, out=None) -> (Tensor, LongTensor*)
* 주어진 input Tensor의 주어진 dimension을 따라서 가장 큰 k개의 element들을 반환한다.
* dim이 주어지지 않았다면, input의 가장 마지막 dimension이 선택된다.
* largest가 False라면, k개의 가장 작은 값들이 반환된다.
* (values, indices)의 namedtuple이 반환된다. indices는 기존 input Tensor element의 색인이다.
* boolean 옵션 sorted가 True라면, 반환되는 k element들은 스스로 정렬된다.

## Parameters ##
* input(*Tensor*) - the input tensor.
* k(*int*) - 'top-k'의 k
* dim(*int, optional*) - 따라 정렬될 dimension
* largest(*bool, optional*) - 가장 큰 값을 반환할지 가장 작은 값을 반환할지 정한다.
* sorted(*bool, optional*) - 정렬된 순서로 element들을 반환할지 정한다.

## Keyword Arguments ##
* out(*tuple, optional*) - output buffer로 사용하기 위해 선택적으로 제공할 수 있는 (Tensor, LongTensor)의 output tuple.

## 예제 ##
```python
import torch

x = torch.arange(1., 6.)
print(x)
# tensor([ 1.,  2.,  3.,  4.,  5.])

print(torch.topk(x, 3))
# torch.return_types.topk(values=tensor([5., 4., 3.]), indices=tensor([4, 3, 2]))
```
-------------------------------
### 출처 ###
* <https://pytorch.org/docs/stable/generated/torch.topk.html>