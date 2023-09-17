# RMSNorm

## Intro
얼마 전, LLaMA를 둘러보다가 해당 모델에서 사용한 Normalization이 RMSNorm이라는 것을 알게 되었다. 사실 LLaMA에서 사용되었다는 것에 끌려 이렇게 정리하게 된 것 같다 ㅋㅎㅋㅎ.

## Formula

$x \cdot {1 \over \sqrt{{1 \over d}\sum_{i=1}^d{x^2_i + \epsilon}}}$

- $d$ : vector $x$의 length
- $\epsilon$ : $x_i$가 0일때를 방지하기 위한 아주 작은 값(hyperparameter)

## 설명

수식에서 볼 수 있듯, $x$의 인자에 제곱을 취해준 값에 $\epsilon$을 더해주고 이 값들의 평균에 루트를 취한 값으로 $x$를 나누어 줌으로써 정규화를 수행한다. 

## 사용처

Transformer 모델의 레이어 정규화에 사용될 수 있다. 특히 LLaMA모델에서 레이어의 input 값을 정규화하는데 사용되었다.

## code

```python
import torch
import torch.nn as nn

class RMSNorm(nn.modules):
	def __init__(self, dim:int, eps:float=1e-06):
		super().__init__()
		self.eps = eps
		self.weight = nn.Parameter(torch.ones(dim))

	def _norm(self, x):
		return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

	def forward(self, x):
		output = x * self._norm(x.float()).type_as(x)
		return output * self.weight
```

추가로 kakaobrain의 trident 라이브러리로도 RMSNorm을 사용 가능하다.

```python
import trident
import torch.nn as nn

class Net(nn.Module):
   def __init__(self):
       super().__init__()
       self.rms_norm = trident.RMSNorm(...)
```

---

### 출처

- [https://velog.io/@ludobico98/Llama-코드-분석-model.py](https://velog.io/@ludobico98/Llama-%EC%BD%94%EB%93%9C-%EB%B6%84%EC%84%9D-model.py)
- https://arxiv.org/pdf/1910.07467.pdf
- https://tech.kakao.com/2023/09/05/kakaobrain-trident/