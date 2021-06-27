# Gradient_Clipping
---

## Gradient Clipping

<img src = '/image/2021_06_27_01.png'>

- gradient가 일정 threshold(threshold는 gradient가 가질 수 있는 최대 L2 norm을 뜻한다.)를 뛰어넘는다면 clipping을 해 준다.
- 이때 threshold는 사용자가 지정한 수(hyperparameter)이다.
- clipping은 gradient의 L2 norm으로 나눠주는 식으로 연산을 해줄 수 있다.

<img src = '/image/2021_06_27_02.png'>

gradient clipping을 통해 gradient가 더욱 잘 수렴하는 모습을 볼 수 있다.

---

### 출처

- [https://sanghyu.tistory.com/87](https://sanghyu.tistory.com/87)