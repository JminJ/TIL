# torch.nn.init.normal_
-----
## 형태 및 설명

- torch.nn.init.normal_(tensor, mean=0.0, std=1.0)
- normal distribution에서 나온 값으로 input tensor를 채운다.

## Parameters

- tensor - n차원 torch.*Tensor.*
- mean - normal distribution의 평균.
- std - normal distrubution의 standard deviation.

## 예제

```python
w = torch.empty(3, 5)
nn.init.normal_(w)
```

---

### 출처

- [https://pytorch.org/docs/stable/nn.init.html](https://pytorch.org/docs/stable/nn.init.html)