# torch.bincount
----
## 형태 및 설명

- torch.bincount(*input, weights=None, minlength=0*) → Tensor
- non-negative int들의 array안 각 value들의 frequency를 계산한다.
- bins의 수는 입력이 비어 있지 않으면 입력에서 가장 큰 값보다 하나 더 크다.이 경우 결과는 크기가 0 인 텐서이다.
- 만약 minlength가 특정되어 있다면, bins의 수는 적어도 minlength이고, input이 비어있다면, result가 0으로 채워진 minlength 크기의 tensor이다.
- 만약 n이 position i의 value라면, 만약 weights가 특정되어 있다면 out[n] += weights[i]이고, 아닌 경우는 out[n] += 1을 해준다.

## Parameters

- input(*Tensor*) - 1차원 int tensor
- weights(*Tensor*) - optional, input tensor안의 각 value들의 weight. input tensor와 같은 size일 것이다.
- minlength(*int*) - optional, bins의 최소값. non-negative일 것이다.

## Returns

- 만약 input이 non-empty일 때 Size([max(input) + 1])의 shape tensor, 아닌 경우, Size(0).

## Return type

- output(Tensor)

## Example

```python
input = torch.randint(0, 8, (5,), dtype = torch.int64)
weights = torch.linspace(0, 1, steps = 5)
print(input, weights)
# (tensor([4, 3, 6, 3, 4]),
#  tensor([ 0.0000,  0.2500,  0.5000,  0.7500,  1.0000])
torch.bincount(input)
# tensor([0, 0, 0, 2, 2, 0, 1])
input.bincount(weights)
# tensor([0.0000, 0.0000, 0.0000, 1.0000, 1.0000, 0.0000, 0.5000])
```

---

### 출처

- [https://pytorch.org/docs/stable/generated/torch.bincount.html](https://pytorch.org/docs/stable/generated/torch.bincount.html)