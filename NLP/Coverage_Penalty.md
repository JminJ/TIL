# Coverage_Penalty
---
> "Coverage Penalty는 attention이 골고루 분배되어 있으면 있을수록 더욱 좋다"

 디코더의 각 time-step마다 attention이 다른 곳에 집중하면 집중할 수록 더 좋은 번역일 것이다.

<img src = "/image/2021_04_23_08.png">

수식을 보면 coverage penalty는 더해지는 것을 볼 수 있다(옆에 곱해지는 것은 [Length Penalty](https://www.notion.so/Length-Penalty-90793152ff104442a0e24ebbb67b72cc)). 아래에서 이 penalty를 어떻게 계산하는지 설명하겠다.

<img src = "/image/2021_04_23_09.png">

 w_i,j를 계산한 뒤 w_i,j의 총 합과 1을 비교해 더 작은 값을 log함수에 넣어주고 이 값을 더한다. 이를 m번 반복한다. 그 후 hyperparameter β를 곱해주면 coverage penalty를 계산할 수 있다. 

- i : encoder의 time-step
- j : decoder의 time-step
- w_i,j : decoder값에 transform을 하고 encoder에 곱한 값(encoder는 i 번째 time-step, decoder는 j 번째 time-step)에 softmax를 씌움

---

### 출처

- FastCampus - 김기현의 자연어 생성 All In One 패키지