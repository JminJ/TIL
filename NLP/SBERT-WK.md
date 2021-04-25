# SBERT-WK
---

> BERT의 layer들에서 나온 값들에는 각각 문장에 대한 특징이 담겨 있을 것이다!

## BERT model의 문제점

<img src = '/image/2021_04_25_01.png' width = '80%'>

 BERT는 여러 layer를 거친 뒤 맨 마지막 layer의 결과 값만을 사용한다. 위 그림에서 빨간 테두리로 감싸진 부분을 뜻한다. 하지만 이 논문의 저자들은 각 layer에서 나오는 결과 값마다 input으로 들어온 문장에 대한 특징들이 들어있을 것이며 이를 활용하면 더 좋은 임베딩을 만들 수 있을 것이라 말을 한다.

 위와 같은 이유도 있지만 기존에 있던 BERT는 sentence pair regression task들에 약한 모습을 보였다. Semantic search task를 예로 들어 설명하겠다.

- 문장 쌍들 중 가장 유사도가 높은 쌍을 찾아야 한다.
- 만약 문장이 충 10,000개라고 할때 추론에 필요한 연산 양은 49,995,000번을 수행해야 한다(Time Consuming)

따라서 BERT로 위와 같은 task를 처리할 때는 아래와 같은 방법을 사용해 해결한다.

- 마지막 layer에 포함되어있는 representation을 평균 낸다.
- CLS token의 output을 사용한다.

 그러나 논문의 저자는 이러한 방법들로는 나쁜 sentence embedding을 만든다고 말한다. 그리고 이에 대한 Key Problem은 **"어떻게 BERT를 기반으로 한 word model들에서 높은 퀄리티의 sentence representation을 만들어 낼 수 있나?"**이다. 

## 어떻게 좋은 sentence representation을 만들 것 인가?

 BERT는 여러 Transformer의 Encoder로 이루어져 있으며, 각 Encoder들은 그 output을 도출한다(사용하는 것은 오직 마지막 layer의 output). 앞서 말한대로 저자들은 이러한 output들이 각자 문장의 언어적인 특성들을 담고 있을것이라 주장하고 이를 활용해 보았다. 

### Evolving word representation patterns across layers

 처음으로 소개한 방법은 "Evolving word representation patterns across layers" 이다. Word2vec의 window처럼 i 번째 layer의 output이 있다고 할 때 **hop**의 수만큼 이전 layer들의 output과 이후 layer들의 output까지의 cosine similarity를 계산해 평균을 내는 방법이다.

<img src = '/image/2021_04_25_02.png' width = '80%'>

<img src = '/image/2021_04_25_03.png' width = '80%'>

<img src = '/image/2021_04_25_04.png' width = '80%'>

 위의 그림은 BERT와 BERT를 기반으로 구현된 여러 model들의 cosine similarity의 변화를 보여주는 그래프이다. XLNET을 제외한 세 개의 그래프는 중간 부분에서 되게 일정한 모습을 보이고 처음과 마지막 부분에서 오르거나 내려가는 모습들을 보인다. 저자들은 이와같은 모습은 model들이 중간 layer에서 되게 general한 언어적 특성들을 학습하기 때문이라고 말한다. 

 또한 중요한 특성은 위 세 개의 model의 마지막 부분이라고 할 수 있다.

- SBERT : + Siamese Network Structure, + Finetuning on SNLI and MNLI
- RoBERTa : - NSP, - Static Masking of Tokens, + Dynamic Masking of Tokens, + Byte Pair Encoding 50K, Large batch size, CC_NEWS dataset

 마지막 부분에서 값이 감소 하지 않는 RoBERTa는 NSP(Next Sentence Prediction)를 뺐고(즉 문장 level의 학습을 거의 하지 않았다.) 마지막 부분에서 값이 급격히 감소 하는 SBERT의 경우 기존 NSP에 Siamese Network Structure를 더해 더 많은 문장 level의 학습을 수행했다는 것을 알 수 있다. 

<img src = '/image/2021_04_25_05.png' width = '80%'>

방금까지 layer의 관점에서 변화를 봤다면 이번에는 단어를 기준으로 변화를 살펴보자. 위 Table은 각 단어별로 variance의 변화가 작았던, 중간이였던, 컸던 단어들을 묶어둔 것이다. 단어 아래에 밑줄이 쳐진 단어는 문장에서 별로 중요하지 않았던 단어들을 표현한 것이다. 한 눈에 볼 수 있듯 variance의 변화가 컸던 단어들은 밑줄이 거의 없는 것고, 이에 반해 변화가 적었던 단어들은 밑줄이 쳐진 단어가 대부분을 차지한다. 

## SBERT-WK Methods

### 1. Determine a unified word representation

<img src = '/image/2021_04_25_06.png' width = '80%'>

 Figure 2를 보면 우리의 model을 표현한 모습을 볼 수 있다. v^1_1부터 v^N_1까지가 첫 번째 단어에 대한 각 layer들의 output이다. 이렇게 모든 단어들은 값들을 가지고 있고 여기에 weight를 곱해 모두 더해줌(Alignment(⍺_a) & Novelty(⍺_n))으로써 v_1...v_6까지의 값을 구한다. 

- v^i_w : representation of word w at the ith layer
- ^v_w == v_w : the unified word representation

    <img src = '/image/2021_04_25_07.png' width = '80%'>

- **weight** ⍺(v^i_w)

마지막으로 Word Importance(w_i)를 거쳐 최종적으로 Sentence Representation을 구하게 된다. 아래 소챕터에서는 weight ⍺를 구하는 방법들에 대해 설명하겠다.

### 1) Inverse Alignment Measure

<img src = '/image/2021_04_25_08.png' width = '80%'>

 C는 i 번째 layer output의 neighboring window의 모음이고 d는 word embedding dimension이고 m은 neighboring window size다. 이때 v^i_w의 alignment(정렬) similarity score는 아래 수식으로 결정된다.

<img src = '/image/2021_04_25_09.png' width = '80%'>

 만약 layer의 neighboring word vector들의 word representation이 잘 align되어 있으면 이는 많은 additional information(정보)를 제공하지 않는다. 때문에 정보가 적을 수밖에 없고 더 적은 weight를 줄 수밖에 없다. 그러므로 word w의 i 번째 layer의 weight를 위해 alignment similarity score의 역수를 사용하기로 했다. 수식적으로는 아래와 같다.

<img src = '/image/2021_04_25_10.png' width = '80%'>

 K_a는 i 에 독립적인 normalization constant(정규화 상수)이고 weight들의 합을 normalize하기 위해 선택된다. 그리고 ⍺_a(v^i_w)는 inverse alignment weight라고 부른다.

<img src = '/image/2021_04_25_11.png' width = '80%'>

### 2) Novelty Measure

 우리는 v^i_w를 두 개의 component들로 분해할 수 있다: 하나는 subspace에 포함되었고 다른 하나는 subspace에 직교한다. 직교하는 것을 우리는 novel component라고 볼 수 있으며 이것의 크기를 novelty score로 사용할 수 있다. singular value decomposition(SVD)를 통해 m ⨯ n의 dimension의 **M**을 **M = UΣV**의 형태로 인수분해할 수 있다, **U**는 직교하는 column이 있는 m ⨯ n의 행렬이고, **Σ**는 n ⨯ n의 non-negative한 수들의 대각 행렬이다. **V**는 n ⨯ n의 직교 행렬이다. 먼저 (4)와 동일한 C를 분해해  **C =** **UΣV**로 만들어 neighboring word들의 orthogonal basis를 찾는다. C의 orthogonal column basis는 U matrix로 표현된다. 그러므로 C에 대한 v^i_w의 orthogonal component는 다음과 같이 계산할 수 있다. 

<img src = '/image/2021_04_25_12.png' width = '80%'>

그리고 v^i_w의 novelty score는 아래와 같이 계산된다. 

<img src = '/image/2021_04_25_13.png' width = '80%'>

K_n은 i 에 독립적인 normalization constant이고 이는 weight들의 합을 normalize하기 위해 선택된다. 또한 우리는 ⍺_n(v^i_w)를 novelty weight라고 부른다.

<img src = '/image/2021_04_25_14.png' width = '80%'>

### 3) Unified Word Representation

 위에서 설명한 두 가지 방법을 통해 얻은 weight들을 가중 평균(weighted average)한다.

<img src = '/image/2021_04_25_15.png' width = '80%'>

 ω는 0 ≤ ω ≤ 1의 범위를 가지고 있으며 ⍺_c(v^i_w, ω)는 combined weight라고 불린다. ω가 0일 때는 novelty weight라고 이름지었고, ω가 0.5일 때는 combined weight, ω가 1일 때는 alignment weight라고 했다. Unified word representation은 각 다른 layer들에서 이 representation들의 weighted sum(가중합) 을 통해 계산된다. 

<img src = '/image/2021_04_25_16.png' width = '80%'>

우리는 v_w를 word w에 대한 새로운 contextualized word representation으로 볼 수 있다.

### 2. Word Importance

 위에서 보았듯 높은 정보를 가지고 있는 단어(Word)는 보통 더 큰 variance를 가지고 있기 마련이였다. 조금 더 생각해 보면 우리는 이와 같은 variance를 단어의 중요도를 결정하는데 사용할 수 있고 문장 안의 여러 단어들을 모아 문장의 embedding vector를 정하는데도 사용할 수 있다. 나래에서 더 설명한다.

 문장 안의 j 번째 단어는 w(j)라고 표기한다, 먼저 (2)에서 본 대로 모든 layer로부터 얻은 word representation으로 cosine similarity matrix를 계산한다. 다음으로는, offset-1인 대각선 값(diagonal values)를 cosine similarity matrix에서 추출하고 offset-1 대각선 값들의 variance를 계산하고 𝜎^2_j를 j 번째 단어의 variance를 표기하기 위해 사용한다. 그러므로 최종 sentence embedding (v_s)는 다음과 같이 표현된다.

<img src = '/image/2021_04_25_17.png' width = '80%'>

^v_w(j)는 (10)과 같은 w(j) 단어의 새로운 contextualized word representaiton이다.

<img src = '/image/2021_04_25_18.png' width = '80%'>

각 단어의 weight는 (12)에서 볼 수 있듯 l1-normalized variance이다. 요약하자면, 문장 embedding scheme에서 layer간에 더 빠르게 진화하는 단어는 variance(분산)이 더 크기 때문에 가중치가 높아진다.

### 3. Computational Complexity

 SBERT-WK의 주된 부담은 novelty measure에서 보다 세밀한 분삭이 가능한 SVD decomposition에서 온다. context window matrix **C**는 **C = UΣV**의 세 가지 matrix들로 분해된다. orthogonal basis는 matrix **U**로 주어진다. context window matrix는  d ⨯ 2m의 size인데, d는 word embedding size이고 2m은 전체 window size를 뜻한다. 우리의 경우, d가 m에 비해 너무 크므로 SVD의 계산 복잡도는 O(8dm^2)가 되고, 몇 몇 term들은 무시된 상태다. 

 SVD decomposition을 적용하는 것 대신, 계산 효울성이 더 좋은 QR factorization을 대안으로 사용하였다. QR factorization을 할 때, 먼저 context window matrix **C**에서 2m+1 word representation을 갖는 새로운 matrix를 만들기 위해 center word vector representation v^i_w을 합친다.

<img src = '/image/2021_04_25_19.png' width = '80%'>

**C˜**에 QR factorization을 수행하고, **C˜ = QR**, non-zero columns인 matrix **Q** ∈ R^d×(2m+1)는 orthogonal basis이고 **R** ∈ R^(2m+1)×(2m+1)는 basis **Q** 아래의 word representation들을 위한 weight들을 포함하는 상부 삼각 행렬(upper triangular matrix)이다. 우리는 **Q**와 **R**의 i 번째 column을 각각 **q^i**, **r^i**라고 표기한다. QR factorization과 함께, **r**^2m+1은 matrix **Q**라고 구성된 orthogonal basis 아래 v^i_w의 representation이다. 이때, r^2m+1의 마지막 component는 새로운 direction의 weight가 되고, 이는 r^2m+1_-1로 표기된다. 그러므로, novelty weight는 아래처럼 파생될 수 있다:

<img src = '/image/2021_04_25_20.png' width = '80%'>

 K_n 은 normalization constant이다. inverse alignment weight는 또한 basis **Q** 아래서 계산될 수 있다. 

 QR factorization의 복잡도는 O(d(2m + 1)^2), 이는 SVD decomposition보다 두 배 더 빠르다. 예를 들어, 우리는 두 방법 사이에서 약간의 성능차를 볼 수 있다. 

---

### 출처

- [https://arxiv.org/pdf/2002.06652.pdf](https://arxiv.org/pdf/2002.06652.pdf)
- [https://www.youtube.com/watch?v=qXZ80xn8DDU](https://www.youtube.com/watch?v=qXZ80xn8DDU)