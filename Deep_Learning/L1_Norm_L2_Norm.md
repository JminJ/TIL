# L1 Norm | L2 Norm #
------

> Norm은 벡터의 길이 혹은 크기를 측정하는 방법이다. Norm이 측정한 벡터의 크기는 원점에서 벡터 좌표까지의 거리 혹은 **Magnitude**라고 한다.

## Intro

Overfitting이 발생했을 경우, 이를 해결하는 방법은 3가지가 있다.

1. 더 많은 데이터를 사용할 것
2. Cross Validation
3. Regularization

학습 데이터를 더 넣을 수 없거나 데이터를 늘려도 Overfitting이 해결되지 않을 경우에는 Regularization을 사용해야한다. 기존 Cost 함수에 L2 Regularization을 위한 새로운 항을 추가한 변형 Cost 함수를 사용한다.

<img src = '/image/2021_03_08_01.png' width = "75%">

## L1 Norm

### Norm

<img src = '/image/2021_03_08_02.png' width = "70%">

- p는 Norm의 차수를 의미한다. p가 1일 경우 L1 Norm이고, p가 2일 경우 L2 Norm이다.
- n은 대상 벡터의 요소 수이다.

### L1 Norm

위에서 설명 했듯, p가 1인 Norm을 L1 Norm이라고 한다.

<img src = '/image/2021_03_08_03.png' width = "75%">

(p는 1이기에 생략) L1 Norm은 각 벡터 요소의 절댓값에 대한 합이다. 따라서 요소의 값 변화를 정확히 파악할 수 있다고 한다. 아래에 예시를 보면서 이해를 같이 해보자.

<img src = '/image/2021_03_08_04.png' width = '75%'>

L1 Norm은 아래와 같ㅌ은 영역에서 사용된다.

- L1 Regularization
- Computer Vision

## L2 Norm

L2 Norm은 아마 감이 오겠지만 p가 2인 Norm이다. L2 Norm은 n 차원 좌표 평면에서의 벡터 크기를 계산하기에 유클리드 노름이라고도 불린다.

<img src = '/image\2021_03_08_05.png' width = "75%">

추가적으로 L2 Norm 공식은 각 x1, x2, . . ., xn을 두 번씩 곱한 식으로 표현이 가능하다.

<img src = '/image/2021_03_08_06.png' width = '75%'>

마찬가지로 아래에 예제를 추가한다.

<img src = '/image/2021_03_08_07.png' width = '75%'>

### 출처

- [http://taewan.kim/post/norm/](http://taewan.kim/post/norm/)