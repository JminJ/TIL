# Machine reading comprehension 
-----
## Cloze Tests

Cloze Tests는 학생들의 언어 실력을 평가하는 시험에서 사용되는 방식이다. Question은 Passage에서 등장한 word나 entity들을 제거해 만들어진다. 여기에 Machine이 빈칸을 채워 넣는 Task이다.

### 특징

- answer A는 주어진 context C에서 등장하게 되는 word 또는 entity이다.
- question Q는 주어진 context C에서 word나 entity를 제거함으로써 만들어진다.

### 한계

- 질문의 답이 되기에 word나 entity만으로는 충분하지 않았다. 완전한 문장이 필요한 경우도 있었다.

## Multiple choice

제공된 context와 일치하는 정답을 정답 후보 사이에서 선택하는 방식이다. Cloze Tests와 비교해보면 Context의 word나 entity들이 제한되지 않으므로 answer 형식이 자유로운 편이다. 그러나 정답 후보가 제공되어야 한다.

### 특징

- answer의 후보가 answer을 예측할 때 제공된다.

### 한계

- 정답 후보가 없는 경우가 많이 있었다.

## Span Extraction

위 두 방법들의 한계점을 보완한 방법으로 context와 question으로 지문에서 text span을 추출해 답으로 하는 방법을 사용했다.

### 특징

- answer A는 context C에 연결된 부분 sequence가 되어야 한다.

### 한계

- context의 span만을 답으로 제한하는 것 또한 아직 현실적이지 못한다.

## Free answering

질문에 답하기 위해 machine은 여러 조각의 text를 종합해 추론해야 하고 evidence들을 요약해야 한다.

소개한 네 가지의 방법들 중 제일 복잡하다. 질문에 대해 답이 제한되어 있지 않기 때문이다. 하지만 이는 실제 적용 시나리오에 제일 적합하다.

## Compare 4 methods

<img src = '/image/2021_07_22_01.png' width = '70%'>

- Construction : 데이터셋 구축 난이도(쉬울 수록 점수가 높다)
- Understanding : 모델 이해도 테스트의 효율성(task가 높은 이해도와 추론을 요구할 수록 점수가 높다)
- Frexibility : answer의 유연성(answer이 자유로울 수록 점수가 높다)
- Evaluation : 평가/채점의 용이성(평가가 쉬울수록 점수가 높다)
- Application : 현실 적용 가능성(적용이 쉬울수록 점수가 높다)

---

### 출처

- [https://incheonkirin.medium.com/machine-reading-comprehension-dataset-19d7a3f51260](https://incheonkirin.medium.com/machine-reading-comprehension-dataset-19d7a3f51260)