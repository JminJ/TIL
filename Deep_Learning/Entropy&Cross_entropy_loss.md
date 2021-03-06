# Entropy & Cross_entropy #
--------------------
### Entropy ###
entropy 란 불확실성에 대한 척도이다. 가방에 빨간 공만 있다면 이 경우, 불확실성은 존재하지 않는다. 따라서 이 경우에는 entropy가 0이라고 말할 수 있다. 어떠한 사건이 같은 비율로 일어난다고 하고 사건의 개수가 n이라면 entropy는 log(n)이다.

하지만 각 사건이 발생할 확률은 제각각 다를 것이다. 이때 entropy를 아래 수식으로 풀어낸다.

![picture](/image/2021_01_10_2.png)

C는 범주의 수이고 q는 사건의 확률질량함수를 말한다. 가방 안에 빨간 공과 초록 공이 20 : 80의 비율로 들어있는 경우, H(q) = -(0.2*log(0.2) + 0.8*(log(0.8)) = 0.5이다.

***entropy는 예측하기 쉬운 일보다 예측하기 힘든 일에서 더 높게 나타난다.***

### Cross-entropy ###
Cross-entropy는 딥러닝에서 분류 모델에 대한 손실 함수이다. 수식은 아래와 같다.

![picture](/image/2021_01_10_3.png)

> n = 데이터 범주, C = 범주 갯수, L = 실제 값, P = 실제 값에 대한 확률 값

만약 L이 [0,0,1], P가 [0.1,0.2,0.7]이라고 가정한다면 cross entropy 값은 0 * log(0.1) + 0 * log(0.2) + 1 * log(0.7) = -log(0.7) = 0.35가 된다. 잘 결과를 예측하면 할 수록 cross entropy값은 적게 도출되고 예측을 잘 못한다면 cross entropy값은 크게 도출될 것이다. **즉 실제 값과 예측 값의 차이를 줄이기 위한 엔트로피이다.**

-------------
## 출처 ##
* <https://3months.tistory.com/436>
* <http://melonicedlatte.com/machinelearning/2019/12/20/204900.html>