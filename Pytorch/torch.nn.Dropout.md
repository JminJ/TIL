# torch.nn.Dropout #
--------
## 형태 및 설명 ##
* torch.nn.Dropout(*p: float = 0.5, inplace: bool = False*)
* training동안 무작위로 베르누이 분포의 sample을 사용하여 확률 p로 input tensor의 element를 0으로 바꾼다.
* 각 channel은 모든 forward call에 상관하지 않고 0점처리 될 것이다.
* 이는 regularization에 효과적인 기술이며 neuron의 co-adaptation을 방지한다.
* 이는 regularization에 효과적인 기술이며 neuron의 co-adaptation을 방지한다.
>
## Parameters ##
* p - 0으로 바뀔 element의 확률, 기본값은 0.5
* inplace - 만약 True로 설정될 경우, 이 operation을 in-place에서 실행한다. 기본값은 False.
>
## Shape ##
* Input - Input은 어느 형태든 가능하다.
* Output - Output은 input의 shape와 동일하다.
>
## 예제 ##
```python 
import torch.nn

m = nn.Dropout(p=0.2)
input = torch.randn(20, 16)
output = m(input)
```
-----------
## 출처 ##
* <https://pytorch.org/docs/stable/generated/torch.nn.Dropout.html#torch.nn.Dropout>