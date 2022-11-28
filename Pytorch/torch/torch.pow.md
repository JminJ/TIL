# torch.pow #
--------
## 형태 및 설명 ##
- torch.pow(*input, exponent, *, out=None*) → Tensor
- input에서 각 element를 exponent로 제곱한 값을 받고 결과값을 갖는 tensor를 반환한다.
- exponent는 하나의 float형 수일 수 있고, input의 element와 같은 수를 갖는 Tensor일 수도 있다.

## Parameters
- input(*Tensor*) - the input tensor.
- exponent(*float or tensor*) - 제곱 값.

## Keyword Arguments
- out(*Tensor, optional*) - the output tensor.

## 예제
```python
imrpot torch

a = torch.randn(4)
print(a)
# tensor([ 0.4331,  1.2475,  0.6834, -0.2791])
print(torch.pow(a, 2))
# tensor([ 0.1875,  1.5561,  0.4670,  0.0779])
exp = torch.arange(1., 5.)

a = torch.arange(1., 5.)
print(a)
# tensor([ 1.,  2.,  3.,  4.])
print(exp)
# tensor([ 1.,  2.,  3.,  4.])
print(torch.pow(a, exp))
# tensor([   1.,    4.,   27.,  256.])
```

---------
### 출처 ###
* <https://pytorch.org/docs/stable/generated/torch.pow.html>