# register_buffer
------
## 형태 및 설명

```
Args:
    name (string): name of the buffer. The buffer can be accessed
        from this module using the given name
    tensor (Tensor): buffer to be registered.
```

- register_buffer는 **매개변수는 아니지만 상태로써 사용**할 수 있는 것을 의미한다.

## 예시

```python
self.register_buffer('running_mean', torch.zeros(num_features))
```

 위 예시는 batch normalization에서 running_mean은 매개변수는 아니지만 상태로써 사용할 수 있다는 것을 보여준다.

---

### 출처

- [https://velog.io/@nawnoes/pytorch-모델의-파라미터로-등록하지-않기-위한-registerbuffer](https://velog.io/@nawnoes/pytorch-%EB%AA%A8%EB%8D%B8%EC%9D%98-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0%EB%A1%9C-%EB%93%B1%EB%A1%9D%ED%95%98%EC%A7%80-%EC%95%8A%EA%B8%B0-%EC%9C%84%ED%95%9C-registerbuffer)