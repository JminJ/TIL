# T5는 max_token_length에 민감하지 않은가?
보통 pre_train된 모델은 pretrain 시 지정한 input의 max_token_length에 대해 매우 민감하다. 예를들어, 1024가 max_token_length로 pretrain된 모델이 있다고 하면 그 이상의 token길이를 가지는 input을 입력할 경우 높은 성능을 기대하기가 힘들다.

## T5의 pretrain max_token_length?
T5 논문에서 언급한 바로는 pretrain 시 512를 입력의 max_token_length로 지정하고 학습시켰다고 한다. 현재(2023.09.15) 나오는 pretrain모델들에 비해서는 매우 적은 token 수라고 생각이 든다(가령 문서 전체를 입력으로 넣어 요약이나 분류 문제를 해결해야 할 경우 매우 고민될만한 요소일 것이다).

## 그럼에도 T5를 문서요약 task에 사용하는 이유
그렇지만 많은 대회 사이트(dacon, kaggle 등)에 올라온 여러 대회후기 글에서는 심심찮게 T5를 파인튜닝하는 케이스를 볼 수 있다. 제목에서도 운을 띄웠듯이 T5는 타 모델들과는 달리 p_max_token_len(pre_train 시 지정한 input의 max_token_length를 해당 표현으로 지정하겠다)에 민감하지 않다. 이유는 transformer계열 모델들이 self-attention의 order independent한 특성 때문에 token에 position 정보를 더해주는데 사용하는 positional encoding 방식에 있다.

## T5의 Position Encoding 방식
T5는 positional encoding으로 relative position embedding을 사용한다. relative position embedding은 각 순서에 고정된 embedding 값을 사용하는게(0,1,2,3,4,5...,N까지 언제나 오름차순으로) 아니라 "key"와 "query"간의 차이를 embedding하는(가령 "I love you"에서 key가 I, query가 you일 때, I의 position은 0, you의 position은 2가 된다) 방법이다. 

이 때문에 T5는 학습 동안 보지 못했던 길이의(보통 512보다 훨씬 긴 상황일 것) input이 들어오더라도 relative position embedding을 사용해 유연하게 처리가 가능한 것이다. 

## 번외: Relative Position Embedding 추가 설명
offset을 지정해 position embedding을 수행한다. 가령 offset이 2라고 했을 때 relative position embedding의 index는 아래와 같을 것이다.
```
0: i번째 token의 왼쪽 2번째 token
1: i번째 token의 왼쪽 1번째 token
2: i번째 token
3: i번째 token의 오른쪽 1번째 token
4: i번째 token의 오른쪽 2번째 token
```
특히 T5는 position embedding을 벡터값으로 더해주는것이 아닌 스칼라값으로 더해주었다고 한다.

---------
### 출처
* https://arxiv.org/pdf/1910.10683.pdf
* https://soundprovider.tistory.com/entry/Exploring-Transfer-Learning-with-T5-the-Text-To-Text-Transfer-Transformer-2
* https://discuss.huggingface.co/t/does-t5-truncate-input-longer-than-512-internally/3602