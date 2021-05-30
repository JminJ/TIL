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

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e813b8c8-64a4-49da-836f-5e5aecd01a68/_2021-05-30__6.45.40.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e813b8c8-64a4-49da-836f-5e5aecd01a68/_2021-05-30__6.45.40.png)

- 위 그림을 보면 오른쪽의 경우 분포가 응집되어있는 것을 파악할 수 있다.
- 학습을 진행할 경우에도 normalization되지 않은 경우에는 learning rate의 변동에 따라 수렴이 되지 않는 경우가 존재한다.

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/20cb0db3-063e-4755-99f4-35b358d3f401/_2021-05-30__6.52.56.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/20cb0db3-063e-4755-99f4-35b358d3f401/_2021-05-30__6.52.56.png)

- normalization된 경우에는 learning rate의 변동에도 안정적이고 효율적으로 학습을 하는 모습을 볼 수 있다.

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d86fd1e0-59ea-470e-bb5d-93471a01cff3/_2021-05-30__6.52.28.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d86fd1e0-59ea-470e-bb5d-93471a01cff3/_2021-05-30__6.52.28.png)

---

### 출처

- [https://www.youtube.com/watch?v=fJ9U2zvp2Jk](https://www.youtube.com/watch?v=fJ9U2zvp2Jk)