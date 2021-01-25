# EDA: Eady Data Argumentation Techniques for Boosting Performance on Text Classification Tasks #
----------------------------------------------------
## Abstract ##
EDA(easy data augmentation)은 text classification task의 성능을 올려줄 수 있는 기술이다. EDA는 네 가지의 간단하지만 강력한 방법으로 구성되어 있다.
구성은 다음과 같다 : synonym replacement(동의어 대체), random insertion(랜덤 삽입), random swap(랜덤 순서변환), random delection(랜덤 삭제). 다섯 개의 text classification task에서 EDA가 CNN과 RNN에서 성능을 향상시킬 수 있었다는 것을 보여주었다.
즉 EDA는 특히 아주 작은 dataset에서 강력한 결과를 보여준 것이다(5개의 dataset의 평균 정확도를 구할 때, 50%의 train set으로 full train set으로 학습한 것과 같은 정확도를 낼 수 있었다).

## Introduction ##
Text classification은 NLP에서의 근본적인 task이다. 머신러닝과 딥러닝은 topic classification에서 감정 분석에 이르기까지 매우 높은 정확도를 달성해 나가고 있지만 높은 성과는 training data의 크기와 질에 의해 결정되는 경우가 많다.
* 문장을 불어로 번역하고 다시 영어로 번역해 새로운 데이터를 얻어내는 방식
* 데이터에 노이즈를 가볍게 줌으로써 더욱 좋은 모델을 만드는 방식
* 유의어로 교체해주는 예측 언어 모델(synonym replacement)

이런 방법이 있었지만 성능을 얻기 위한 구현 비용이 너무나 크기에 잘 쓰이질 않았던 것이다.
따라서 이 논문에서 EDA라는 보편적인 data augmentation 기법들을 소개하고 계층적으로 다섯 개의 benchmark classification task를 통해 EDA가 다섯 task에 상당히 성능향상에 도움을 준다는 점과 특히 작은 dataset에서 도움이 된다는 것을 평가할 것이다.

## EDA ##
저자들은 여러 augmentation들을 computer vision에서 쓰이는 방식에 영감을 받아 실험 해보았고 그것들이 robust model을 학습시키는데 매우 도움이 된다는 것을 알게 되었다.
아래 EDA의 디테일한 설명을 적어 두었고, training set에 주어질 문장들 또한 적혀 있다. 우리는 설명에 적힌 방법 중 랜덤하게 하나를 고를 것이고, 적용시킬 것이다.
1. Synmonym Replacement(SR) : 문장에서 랜덤하게 stop word가 아닌 n개의 단어를 고른다. 고른 각 단어의 동의어를 랜덤하게 뽑아 그 단어와 교체한다.
2. Random Insertion(RI) : 문장에서 랜덤하게 골라진 단어의 동의어를 무작위로 뽑아 문장의 아무 위치에 집어 넣는다. 이 작업을 n번 반복한다.
3. Random swap(RS) : 문장에서 무작위로 고른 두 단어들을 서로 위치를 바꿔 재배치 시킨다. 이 작업을 n번 반복한다.
4. Random Delection(RD) : 문장에서 확률 p에 따라 랜덤하게 고른 단어를 삭제한다.

![image1](/image/2021_01_21_1.png)

짧은 문장보다 긴 문장은 당연히 문장 속에 단어를 많이 가지고 있을 것이기에 기존의 class label을 유지하면서 더 많은 noise를 담아낼 수 있을 것이다. 이를 보완하기 위해 변경된 단어 수를 조정 해 준다. SR, RI, DS를 위한 n은 문장의 길이 l과 공식 n = αl에 기반해 있다. α(알파)는 문장 내에서 단어의 백분율이 변화되었음을 표현하는 parameter이다(RD의 경우 p = α).
더 나아가 각각의 기존 문장은 n_aug라는 변경된 문장을 만들어낸다. 예시 문장은 Table 1에 표기되어 있다.
SR 방식은 이전에도 사용 되었지만 RI, RS, RD 방법은 이 논문에서 처음으로 사용한 방법이라고 한다.

## Experimental Setup ##
다섯 개의 text classification task와 두 개의 network architecture들을 가지고 EDA를 평가해 볼 것이다.

| **Benchmark Datasets**
실험에 사용될 text classification task는 1. SST-2, 2. CR, 3. SUBJ, 4 TREC, 5. PC로 구성되어 있다. 통계를 정리한 자료는 Supplemental Materials의 Table 5에 있을 것이다. 
나아가서, 우리는 EDA는 작은 dataset에서 효과적일 것이라는 가설을 세웠고, 전체 training set에서 랜덤 부분 집합을 골라 Ntrain={500, 2,000, 5,000, all available data}이라는 데이터셋을 만들었다.

| **Text Classification Models**
저자들은 두 개의 유명한 모델들로 text classification 실험을 수행하였다. 첫 번째 모델은 sequence data에 잘 맞는 RNN이고(LSTM-RNN을 사용하였다) 두 번째는 text classification에서 높은 점수를 기록하고 있는 CNN이다. 모델들에 대한 detail들은 Syplementary Materials의 Section 9.1에서 확인하라.

## Result ##
저자들이 두 개의 모델로 다섯 개의 NLP task 테스트했다. 모든 실험에 대해, 저자들이 다섯 개의 각각 다른 random seed로부터 얻은 결과를 평균 내 결과를 적어두었다.

| **EDA Makes Gains**
CNN과 RNN을 EDA를 쓰냐 안쓰냐에 따라 모든 dataset들을 여러 training set size로 실행해 보았다. 평균 performance는 Table2에 기록되어 있다. 중요한 점은 전체 dataset을 사용했을 경우 0.8%의 성능 향상이 있었고, Ntrain이 500이였을 때 3%가 오르는 것을 볼 수 있었다.

![image2](/image/2021_01_21_2.png)

| **Training Set Sizing**
Overfitting은 training set이 작은 경우에 더 극심한 경향이 있다. 제한된 범위의 training set을 사용한 실험들을 합쳐 봤을 때 EDA는 작은 dataset일 경우 상당한 성능 향상을 보인다고 한다.
training set의 양을 {1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100} % 로 조정해 가며 일반 train과 EDA train을 수행했다. Figure 1은 각 dataset에 EDA를 사용했을 떄, 사용하지 않았을 때로 비교하며 보여준다.
(f) 그래프에서 EDA를 적용하지 않았을 때는 train set을 100% 사용했을 때 88.3%로 가장 높았고 EDA를 적용했을 때는 50%의 train set을 사용했을 때 88.6%로 EDA를 적용하지 않고 full train set을 사용하였을 때의 결과보다 0.3% 더 높았다.

![image3](/image/2021_01_21_3.png)

| **Does EDA conserve true labels?**
Data augmentation에서 input data는 class label이 보존된 상태로 변형된다. 만약 문장이 너무 많이 변경되면 더 이상 기존의 label이 유지되지 않을 수도 있다. 따라서 저자들은 시각화 접근법을 통해 EDA 작업이 변형된 문장의 뜻을 상당히 바꾸는지 평가해보기로 했다.
먼저, RNN을 pro-con classification task에 대해 훈련시킨다(EDA 적용 X). 그리고 EDA를 test set에 적용시킨다(한 문장당 9개의 문장을 생성). 이렇게 만든 문장을 기존 문장과 함께 RNN에 넣고, 마지막 레이어에서 결과물을 뽑아낸다. 나온 값에 t-SNE를 적용하고 2-D 그래프로 나타낸다.

![image4](/image/2021_01_21_4.png)

저자들은 생성된 문장의 잠재적 공간표현이 원래 문장의 잠재적 공간표현을 매우 밀접하게 둘러싸고 있다는 것을 발견했다. 즉, EDA는 원래 문장의 label을 보존하고 있다는 것을 알 수 있다.

| **Abalation Study: EDA Decomposed**
지금까지 고무적인 경험적 결과를 보아왔다. 이번 section에서는 EDA의 각 기법의 효능을 연구하는 abalation study를 수행해 볼 것이다.
SR 기법은 이전부터 사용이 되어오던 기법이였다. 하지만 다른 3개의 기법은 아직 연구되어지지 않았었다. 하나의 가설은 'EDA의 성능은 대부분 SR 기법을 통해 올라가고 있던 것이 아니였나? ' 이다. 따라서 EDA의 각 기법을 격리시키고 그것 각각의 성능을 올리는 능력을 평가해 볼 것이다.

![image5](/image/2021_01_21_5.png)

모든 4가지의 방법에 대해 다양한 augmentation parameter와 각각 기법 하나씩 사용해 모델을 실행한다. α={0.05, 0.1, 0.2, 0.3, 0.4, 0.5} (Figure 3) 이는 4개의 EDA 기법이 성능을 올리기 위해 기여하는 것이 나타나게 된다.
SR의 경우, α가 작을 시 성능 향상이 크게 나타났다. 하지만 α가 클 경우 성능이 저하되었다. 마치 문장에서 너무 많은 단어를 바꾸면 문장의 정체성이 바뀌는 것과 같다.
SI의 경우, 성능 향상은 다른 α 값에 따라 더욱 안정적이게 되어갔다. 이 기법에서는 기존 문장의 단어와 그와 관련된 문장의 순서가 유지되기 때문이다.
RS의 경우, α가 0.2% 보다 작거나 같은 경우에 가장 높은 성능 향상을 보였다. 그러나 α가 0.3% 보다 같거나 커질 경우 성능이 떨어졌다. 이유는 너무 많은 위치 변화(swap)가 일어나는 것은 문장의 모든 순서가 섞이는 것과 같기 때문이다.
RD는 α가 낮은 경우 높은 상향을 얻었다. 하지만 α가 높을 경우 심각한 성능 저하가 나타났다. 높은 α는 문장이 절반의 단어가 사라지는 것과 같이 정보가 없는 것과 같기 때문이다.
성능 향상은 dataset이 작은 경우 모든 기법들에서 뛰어난 효과를 보였다. 그리고 α가 0.1일 경우 전체적으로 "sweet spot"이였다.

| **How much augmentation?**
다음 step은 기존 문장에 대해 몇 개의 문장(n_aug)을 생성해야 하는지를 정한다. Figure 4에서 우리는 모든 dataset에 대한 n_aug={1, 2, 4, 8, 16, 32}의 평균 성능을  보여준다. 작은 training set에 대해 overfitting은 더 자주 일어난다. 따라서 많은 문장을 생성하게 되면 큰 성능 향상이 나타난다. 큰 training set에 대해서는 기존 문장 하나 당 4개 이상의 문장을 생성하는 것이 큰 도움이 되지 않는다. 이미 많은 양의 실제 데이터를 사용할 수 있을 때 모델이 적절히 일반화가 되는 경향이 있기 때문이다. 이와 같은 결과에 기반해 아래의 파라미터들을 추천한다.

![image6](/image/2021_01_21_6.png)

## Comparison with Related Work ##
관련된 연구들은 창의적이긴 하나 종종 어렵다. Back translation, translational data augmentation 그리고 nosing 이 세 가지 방법들은 기계 번역 BLEU 측정에서 성능 향상을 보였다. 다른 과제의 경우, 이전 접근법에는 task specific heuristic과 back translation이 포함된다.
SR에 관하여, 한 연구는 word embedding을 사용한 k-nearest neibors로 동의어를 찾아 tweet classification을 수행했는데 F1 score가 1.4% 증가하는 것을 보여주었다.  또 다른 연구는 동의어로 headword를 바꿀 때 temporal analysis의 어떤 개선도 발견하지 못했으며 character level text classification에서 SR을 사용한 혼합 결과가 보고되었지만, 두 작업 모두 광범위한 ablation study를 수행하지 않았다.
대다수의 연구는 특별한 작업 context에서 또는 번역을 위한 상호 보완적인 결과를 연구하기 때문에 이전의 문헌과 직접적으로 비교하는 것은 어렵다.
그러나 다중 dataset에서 augmentation 기술을 평가하는 방법이 비슷한 두 개의 비슷한 연구가 있다. Hu는 VAE와 속성 판별기를 합쳐 fake data를 생성하는 모델을 제안하였고 두 개의 데이터셋에 대해 3%의 성능 증가를 증명하였다. Kobayashi는 단어 교체를 양방향 언어 모델을 사용해 문맥에서 예측한 단어와 하는 것을 보여줬고 다섯 개의 dataset에서 0.5%의 성능 향상를 보여주었다.
하지만 VAE와 양방향 LSTM 언어모델은 너무 많은 작업이 필요하다. EDA는 같은 규모의 작업을 더욱 쉽게 결과를 낼 수 있다. 언어 모델은 training을 하지 않아도 되고, 타 dataset을 사용하지 않아도 된다. Table 4는 EDA가 다른 기술들에 비해 쉬운 이유를 보여준다.

![image7](/image/2021_01_21_7.png)

## Discussion and Limitations ##
이 논문은 향후 이루어질 조사에 기준이 될 수 있는 간단한 기술들을 소개함으로써 아직 부족한 NLP의 표준 data augmentation을 해소하는 것을 목표로 하였다.
최근 들어 NLP 연구의 비율이 많이 늘어났으며, 연구자들이 사용하기 쉽고 더 좋은 성능의 augmentation 기술을 찾아낼 것이라고 기대한다. 특히 최근 많은 연구들은 크고 더 복잡한 neural model을 만드는데 집중하고 있지만 이 연구는 정 반대의 접근법을 수행한다. 
저자들은 어떻게 문장들의 true label을 바꾸지 않고 변형된 문장을 생성할 수 있을까? 라는 근본적인 질문의 답을 간단한 기술들로 소개했다. 미래에 NLP를 위한 데이터 증강 기법이 EDA가 될 것이라 예상하지는 않지만, 보편적인 작업별 데이터 증강에 대한 새로운 접근법에 대한 영감을 주었기를 저자들은 희망한다.
이제 EDA의 한계점에 대해 말해보겠다. 우선 data가 충분할 때 평균 성능 향상은 매우 미미하다. 다섯 개의 classification task에서 data가 충분히 있을 때 성능 향상은 1%보다 적었다고 한다. 그리고 모든 성능 향상은 작은 dataset일 때 선명하게 관찰된다. 그러나 사전 훈련된 모델을 사용하는 경우에는 상당한 개선 효과를 거두지 못할 수 있다. ULMFit, ELMo, BERT같은 모델에서는 무시할 수 있는 수준이다. 마지막으로 다섯 가지의 benchmark testset에서 평가했지만, NLP의 데이터 증강에 대한 다른 연구는 다른 모델과 다른 데이터 셋을 사용하므로 관련 작업과의 공정한 비교는 매우 비현실적이다.

## Conclusion ###
저자들은 간단한 data augmentation 기법이 test classification에서 성능을 향상시킬 수 있다는 것을 보여줘 왔다. 무조건 모든 순간에 효과가 있다고는 말 할수 없지만 작은 train set에 대한 학습을 진행할 때 성능을 향상시키고 overfitting을 감소시킨다.

------------------
## 출처 ##
* <https://arxiv.org/pdf/1901.11196.pdf>
### 참고 ###
* <https://catsirup.github.io/ai/2020/04/21/nlp_data_argumentation.html>