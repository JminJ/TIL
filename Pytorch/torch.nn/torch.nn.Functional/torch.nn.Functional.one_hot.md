## torch.nn.Functional.one_hot
### 형태 및 설명
* torch.nn.functional.one_hot(*tensor, num_classes=- 1*) → LongTensor
* **(*)** shape의 index 값과 함께 LongTensor를 받아 input tensor의 값과 일치하는 last dimension의 index를 제외하고 모두 0을 가지는 **(\*, num_classes)** shape의 tensor를 반환한다.
### Parameters
* tensor(*LongTensor*) - 아무 shape의 class value들
* num_classes(*int*) - class들의 전체 개수. 만약 -1로 세팅되어 있으면, input tensor에서 가장 큰 class값 보다 1큰 값으로 추론한다.
### Returns
* 1보다 큰 dimension을 갖는 LongTensor를 갖는다. 이 LongTensor는 input이 가르키는 last dimension index는 1을 갖고 나머지 다른 index는 0을 갖는다.
### Examples
```python
>>> F.one_hot(torch.arange(0, 5) % 3)
tensor([[1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0]])
>>> F.one_hot(torch.arange(0, 5) % 3, num_classes=5)
tensor([[1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0]])
>>> F.one_hot(torch.arange(0, 6).view(3,2) % 3)
tensor([[[1, 0, 0],
         [0, 1, 0]],
        [[0, 0, 1],
         [1, 0, 0]],
        [[0, 1, 0],
         [0, 0, 1]]])
```