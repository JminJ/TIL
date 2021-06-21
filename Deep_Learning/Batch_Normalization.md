# Batch-Normalization
---

> Covariate Shift를 줄이기 위한 방법이다!

## Internal Covariate Shift

 학습하는 도중 이전 layer의 파라미터 변화로 인해 현재 layer의 입력 분포가 바뀌는 현상을 Internal Covariate Shift라고 한다. 

<img src = '/image/2021_06_21_01.png'>

 위 그림처럼 기둥이 휘어지는 현상을 막기 위해 특정한 작업을 해주는 것 처럼 layer 또한 특정한 작업을 통해 휘어지는 현상을 막을 수 있다.

## Covaiate Shift를 줄이는 Batch Normalization

<img src = '/image/2021_06_21_02.png'>

  위 절차를 통해 우리는 BN(Batch Normalization)을 수행할 수 있다. 

- mini-batch의 평균을 구해주고
- 앞서 구한 평균을 통해 mini-batch의 분산을 구해준다.
- 이후 기존 x_i에 평균과 분산을 통한 normalize를 수행하고
- 학습되어야 하는 parameter인 γ와 β를 통해 scale과 shift를 수행해준다.

추가로 몇 마디 더 붙여보자면, Normalization 부분에서 평균을 빼주고 그것을 분산으로 나눠주게 되면 결과의 분포는 -1 ~ 1의 범위로 나오게 된다.

---

### 출처

- [https://m.blog.naver.com/laonple/220808903260](https://m.blog.naver.com/laonple/220808903260)