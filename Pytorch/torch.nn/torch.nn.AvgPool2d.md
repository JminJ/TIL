# torch.nn.AvgPool2d #
----------
## 형태 및 설명 ##
* torch.nn.AvgPool2d(*kernel_size: Union[T, Tuple[T, T]], stride: Optional[Union[T, Tuple[T, T]]] = None, padding: Union[T, Tuple[T, T]] = 0, ceil_mode: bool = False, count_include_pad: bool = True, divisor_override: bool = None*)
* 몇몇의 input plane들로 구성된 input signal에 2D average pooling을 적용한다.
* 만약 padding이 non-zero라면, 그때는 input은 암묵적으로 양 side를 point의 number에 대해 padding zero-pad 된다. 
>
## Parameters ##
* kernel_size - window의 size.
* stride - window의 stride. 기본값은 kernel_size.
* padding - 양 side에 더해지기 위한 암시적 zefo padding.
* ceil_mode - True일 때, 평균 계산에 zero-padding을 포함한다.
* divisor_override - 만약 명시된 경우, 이는 divisor로 사용될 것이다. 다른 경우 kernel_size가 사용된다.
>
## 예제 ## 
```python
import torch
import torch.nn

# pool of square window of size=3, stride=2
m = nn.AvgPool2d(3, stride=2)

# pool of non-square window
m = nn.AvgPool2d((3, 2), stride=(2, 1))
input = torch.randn(20, 16, 50, 32)
output = m(input)
```
--------
## 출처 ##
* <https://pytorch.org/docs/stable/generated/torch.nn.AvgPool2d.html>