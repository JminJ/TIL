# swich #
----
## ReLU와 그 한계

<img src = '/image/2021_03_28_2.png'>

 ReLU는 0 이하의 값을 다음 레이어에 전달하지 않는 특징을 가지고 있다. 하지만 한 번 0으로 처리된 활성화 값을 다음 레이어에 전달하면 이후 뉴런들의 출력값이 모두 0이 되어버린다는 한계점을 가지고 있다. 이를 **dying ReLU**라고 부르고 이 한계점을 해결하기 위해 음수 출력값을 소량이라도 다음 레이어에 전달하는 방식으로 개선된 활성화 함수들이 만들어졌다.

## swish

<img src = '/image/2021_03_28_3.png'>

 ReLU의 한계를 해결하고 대체하기 위해 구글에서 고안한 함수로 sigmoid함수에 x를 곱한 매우 간단한 형태를 보인다. 깊은 레이어를 학습시킬 때 ReLU보다 더욱 뛰어난 성능을 보여준다. 특히 CNN architecture 중 하나인 mobilenet을 학습시키는데 사용된다.

---

### 출처

- [https://yeomko.tistory.com/39](https://yeomko.tistory.com/39)