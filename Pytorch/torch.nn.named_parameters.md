# torch.nn.named_parameters
---
## 형태 및 설명

- named_parameters(*prefix='', recurse=True*)
- 모든 module의 parameter의 iterator를 return한다, parameter 그 다체와 parameter의 이름 모두를 반환한다.

## Parameters

- prefix(*str*) - 모든 parameter의 이름 앞에 붙는 접두사
- recurse(*bool*) - True일 시, 이 module과 모든 submodule들의 parameter들을 반환한다. 그렇지 않을 경우, 이 module의 직접적인 member들의 parameter들만 반환한다.

## Yields

- (*string, Parameter*) - name과 parameter들을 포함하는 Tuple

## 예제

```python
for name, param in self.named_parameters():
	if name in ['bias']:
		print(param.size())
```

---

### 출처

- [https://pytorch.org/docs/stable/generated/torch.nn.Module.html](https://pytorch.org/docs/stable/generated/torch.nn.Module.html)