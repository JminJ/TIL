# Revnet #
-----

## Resnet

 Resnet은 기존 모델들이 가진 층을 깊게 쌓으면 되려 성능이 떨어진다는 단점을 해결하기 위해 Residual Block이라는 기법을 활용해 깊은 층을 쌓을 수 있게 만든 모델이다. 

### Residual Block

<img src = '/image/2021_03_31_01.png'>

 위 그림은 Residual block을 설명하는 그림이다. **input x가 있고 F안에 들어가 값이 나오게 되면 기존 input x를 F(x)에 더해주는 방식**이다. 하지만 **backpropagation의 네트워크의 activation들을 모두 메모리에 저장해야 하는 특성 때문에 네트워크가 깊어지고 넓어질 수록 메모리를 많이 사용**하게 되어 bottleneck 현상을 초래할 수 있다.

### Transformer에서의 Resnet

<img src = '/image/2021_03_31_02.png'>

 Transformer기법은 최근 NLP 분야에서 엄청난 성능의 향상을 불러일으킨 모델이다. 하지만 Transformer가 무조건 완벽한 것은 아니다. 위 그림을 보면 Residual block을 사용하는 것을 볼 수 있듯이 메모리를 많이 사용함으로써 bottlemeck 현상이 발생할 수 있기 때문이다.

## Revnet

Transformer에서 encoder와 decoder layer를 여러개 쌓을 시, Residual Network에서 역전파를 위해 gradient 값들을 저장하고 있다. 그러나 저장하는 값이 너무 많으므로, 앞서 말했듯 메모리 부족 현상이 너무나 쉽게 나타난다. 따라서 **gradient값들을 저장할 필요 없는 Revnet을 사용해 이 문제를 해결한다**.

### 구조

<img src = '/image/2021_03_31_03.png'>

Revnet은 layer의 unit들을 두 개의 그룹으로 나눠준다. 그리고 위 그림을 수식으로 나타내면 아래와 같다.

- y1 = x1 + F(x2)
- y2 = x2 + G(y1)

### Reset과의 차이

Resnet은 더해질 값들을 매 layer마다 저장해 두어야 했지만 Revnet은 저장을 하지 않는 대신 아래 식을 통해 다시 값들을 계산할 수 있다.

- x2 = y2 - F(y1)
- x1 = y1 - F(x2)

또한 알아 두어야 하는 점은 reversible block(Revnet)은 무조건 stride 1을 사용해야 한다. 1이 아닌 경우 layer의 정보를 완전히 유지하지 못하게 되므로 reversible하지 않게 된다.

---

### 출처-그림

- [https://towardsdatascience.com/residual-blocks-building-blocks-of-resnet-fd90ca15d6ec](https://towardsdatascience.com/residual-blocks-building-blocks-of-resnet-fd90ca15d6ec)
- [https://paul-hyun.github.io/transformer-03/](https://paul-hyun.github.io/transformer-03/)
- [https://hyeonnii.tistory.com/268](https://hyeonnii.tistory.com/268)

### 출처-내용

- [https://hyeonnii.tistory.com/268](https://hyeonnii.tistory.com/268)
- [https://velog.io/@nawnoes/리포머의-Reversible-Transformer](https://velog.io/@nawnoes/%EB%A6%AC%ED%8F%AC%EB%A8%B8%EC%9D%98-Reversible-Transformer)