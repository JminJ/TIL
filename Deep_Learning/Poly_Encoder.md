# Poly_Encoder
-----
> "Poly Encoder는 Cross-Encoder와 Bi-Encoder의 강점을 합친 것"

## Bi-Encoder

---

 Bi-Encoder의 이름을 보면 해당 Encoder에 대한 느낌을 대충 알 수 있다. Bi-Encoder는 context(문장)과 candidate(후보 답변)으로 구성된 데이터를 context를 처리하는 Encoder 하나, candidate를 처리하는 Encoder 하나 즉 두 개의 Encoder로 구성된 Encoder다. 

<img src = "/image/2021_04_23_01.png">

이제 수식을 살펴보면서 세세한 내용을 알아보고 이 Encoder의 장점을 알아보자.

### 수식

<img src = "/image/2021_04_23_02.png">

 y_ctxt는 그림 (a)의 Ctxt Emb를 뜻하고 y_cand는 Cand Emb를 말한다. 이 두 수식에 중복되는 요소는 red(·)이며 이는 T(x)라고 하는 Transformer Encoder의 output sequence를(Context Encoder의 output) 하나의 벡터로 변환하는 것을 의미한다(**Out_x 1...Out_x N_x → Ctxt Emb**).

 그리고 최종 Score는 이 두 값의 내적을 통해 구해진다.

<img src = "/image/2021_04_23_03.png">

### 장점

 위와 같은 방법으로 주어진 n개의 후보 문장들에 대해 점수를 계산하고 가장 높은 점수의 Score를 가진 후보 문장을 context 다음에 오는 문장이라고 판단할 수 있다.

 Bi-Encoder는 BERT가 사용한 Cross-Encoder 형식보다 속도 면에서 훨씬 빠른 모습을 보여준다. 하지만 당연히 Cross-Encoder보다 성능이 떨어지는 것은 감수해야 한다. 

 Cross-Encoder에 비해 Bi-Encoder 속도가 빠른 이유는 Cross-Encoder의 경우 context-candidate 데이터를 같이 넣고 하나의 Encoder로 학습시키므로 둘 간의 관계를 훨씬 잘 학습할 수 있다. 하지만 하나의 Query로 context가 들어오면 하나의 Query를 처리하기 위해 Transformer Encoder의 inference(추론)를 수 백, 수 천번 계산해야 하므로 실제 서비스 차원에서 사용하기가 매우 어렵다.

 Bi-Encoder는 context, candidate를 따로 따로 Encoder로 계산하므로 Query로 들어오는 context를 한 번만 처리하고 설령 candidate 문장이 매우 많더라도 미리 Encoding을 수행 해 문장 별 Candidate Encoding을 계산해 둘 수 있기 때문이다. 이후 준비된 Encoding들로 내적 계산만 하면 되므로 속도면에서 큰 차이를 보이는 것이다(Encoding을 최대한 하지 않는 것이 속도 차이의 요인).

## Cross-Encoder

---

 Cross-Encoder는 BERT의 방법론과 유사하다. context와 candidate를 연결해 하나의 Encoder에 넣은 뒤 regression을 통해 다음 문장으로 적절한 가에 대한 점수를 계산한다. 

<img src = "/image/2021_04_23_04.png">

 Bi-Encoder와는 달리 Encoding 과정에서 context(ctxt)와 candidate(cand)간의 self-attention을 적용할 수 있기 때문에 둘 간의 관계를 깊게 파악할 수 있다는 장점이 있다. 이 때문에 성능 또한 Bi-Encoder 방식에 비해 더 좋다.

 학습의 경우 Bi-Encoder와 마찬가지로 batch 내의 샘플을 사용해 cross entropy loss를 최소화 시키는 방식이다.

## Poly-Encoder

---

Poly-Encoder는 앞서 설명한 Bi-Encoder와 Cross-Encoder의 장점을 살리고 단점을 보완하고자 제안되었다. 

<img src = "/image/2021_04_23_05.png">

그림(c)를 보면 Bi-Encoder처럼 context와 candidate를 Encoder 두 개를 사용해 Encoding하고 Cross-Encoder처럼 Attention을 사용해 계산하였다. 

 하나 하나 설명해 보자면, 

- input을 Context Encoder, Candidate Encoder에서 계산을 한다.
- 앞 연산의 output들인 Out_x 1...Out_x N_x와 Query로 주어지는 Code 1...Code m들로 Attention 연산을 해 Emb 1...Emb m을 만든다.
- 이 순간 Candidate Encoder의 output들인 Out_y 1...Out_y N_y로 Candidate Aggregator연산을 수행한 결과인 Cand emb를 Query로 해 Emb 1...Emb m로 Attention 연산을 수행한다.
- Attention연산의 결과인 Ctxt Emb와 Cand enb를 내적해 Score를 계산한다.

### 수식

 Context Encoder를 통해 연산된 Out_x 1...를 연산하는 부분까지는 Bi-Encoder와 동일하므로 생략했다. 

<img src = "/image/2021_04_23_06.png">

 h_1...h_N은 Context Encoder의 output(Out_x 1...)를 의미한다. c_i는 Code 1...Code m 중 i 번째 요소를 뜻한다. 

- 이제 c_i * h_1...c_i * h_N의 연산을 softmax 함수에 넣어 (w^ci_1...w^ci_N)를 계산한 뒤
- w^ci_j와 h_j값을 곱한 뒤 모두 더해 y^i_ctxt 값을 계산한다.

 이후 최종 Score를 위에서 구한 Context Embedding과 Candidate Embedding의 내적을 통해 계산한다.

### 장점

 Poly-Encoder는 기존 Cross-Encoder처럼 context와 cadidate 간의 관계를 보다 깊게 파악할 수 있으면서, Bi-Encoder처럼 문장들의 Embedding을 일정 부분 미리 계산이 가능해 inference(추론) 상황에서 매우 빠르고 효과적이다.

---

### 출처

- [https://roomylee.github.io/poly-encoder/](https://roomylee.github.io/poly-encoder/)