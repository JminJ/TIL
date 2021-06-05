# torch.where
-----
## 형태 및 설명

- torch.where(condition, x, y) → Tensor
- condition에 의존해 x 또는 y tensor를 return 한다.
- 작업은 아래와 같이 계산된다.

    <img src = '/image/2021_06_05_01.png'>

## Parameters

- condition(*BoolTensor*) - True라면 x를 반환하고 그렇지 않은 경우, y를 반환한다.
- x (*Tensor or Scalar*)
- y (*Tensor or Scalar*)

## 예제

```python
x = torch.randn(3, 2)
y = torch.ones(3, 2)
x
# tensor([[-0.4620,  0.3139],
#         [ 0.3898, -0.7197],
#         [ 0.0478, -0.1657]])
torch.where(x > 0, x, y)
# tensor([[ 1.0000,  0.3139],
#         [ 0.3898,  1.0000],
#         [ 0.0478,  1.0000]])
```

---

### 출처

- [https://pytorch.org/docs/stable/generated/torch.where.html](https://pytorch.org/docs/stable/generated/torch.where.html)