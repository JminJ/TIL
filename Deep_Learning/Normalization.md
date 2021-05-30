# Normalization
-----
> normalization : 정규화 - 다양한 측도의 데이터들을 공통의 스케일로 변환하는 작업

## Normalization

- 데이터 스케일링 관점
- 데이터의 범주를 바꾸는 과정
- 다양한 측도의 데이터들을 "공통의 스케일"로 변환하는 작업
- ex) z-score normalization

## Regularization

- 모델의 복잡도 관점
- 모델의 학습에 "패널티"를 부여해 모델의 복잡도를 낮추는 과정이다.
- Overfitting을 제어하는 역할을 가진다.
- ex) Regularizer(L1, L2), Dropout, Early-stopping, etc..

## Normalization의 효과

- data input을 정규화함으로써 Weight, bias의 학습을 안정적이고 빠르게 할 수 있다.

    <img src = '/image/2021_05_30_01.png' width='70%'>

- 위 그림을 보면 오른쪽의 경우 분포가 응집되어있는 것을 파악할 수 있다.
- 학습을 진행할 경우에도 normalization되지 않은 경우에는 learning rate의 변동에 따라 수렴이 되지 않는 경우가 존재한다.

    <img src = '/image/2021_05_30_02.png' width='70%'>

- normalization된 경우에는 learning rate의 변동에도 안정적이고 효율적으로 학습을 하는 모습을 볼 수 있다.

    <img src = '/image/2021_05_30_03.png' width='70%'>

---

### 출처

- [https://www.youtube.com/watch?v=fJ9U2zvp2Jk](https://www.youtube.com/watch?v=fJ9U2zvp2Jk)