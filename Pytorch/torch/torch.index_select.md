# torch.index_select
## 형태 및 설명
* torch.index_select(*input, dim, index, *, out=None*) → Tensor
* *input*의 index를 *dim* 차원에 대해 *LongTensor*인 *index*의 값으로 변경한 새로운 tensor를 반환한다.
* 새롭게 반환되는 tensor는 original tensor(*input*)과 차원이 동일하다.
* *dim*번째 차원은 *index*의 길이와 동일한 크기를 갖는다; 다른 차원들은 original tensor와 동일한 크기를 갖는다.

```md
NOTE) 반환되는 tensor는 original tensor와 동일한 storage를 갖지 **않는다**. 만약 *out*이 예상된 shape와 맞지 않다면, 올바른 shape로 아무 말없이(silently) 변환하고, 필요한 경우 storage를 재 할당한다.
```

## Parameters
* input(*Tensor*) - input tensor.
* dim(*int*) - index를 변경할 차원.
* index(*IntTensor or LongTensor*) - 변경할 index를 담은 1-D tensor.

## Keyword Arguments
* out(*Tensor, optional*) - output tensor.

## 예제
```python
>>> x = torch.randn(3, 4)
>>> x
tensor([[ 0.1427,  0.0231, -0.5414, -1.0009],
        [-0.4664,  0.2647, -0.1228, -1.1068],
        [-1.1734, -0.6571,  0.7230, -0.6004]])
>>> indices = torch.tensor([0, 2])
>>> torch.index_select(x, 0, indices)
tensor([[ 0.1427,  0.0231, -0.5414, -1.0009],
        [-1.1734, -0.6571,  0.7230, -0.6004]])
>>> torch.index_select(x, 1, indices)
tensor([[ 0.1427, -0.5414],
        [-0.4664, -0.1228],
        [-1.1734,  0.7230]])
```