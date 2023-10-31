# transformers의 RAG 구조
본 내용은 transformers github repository와 내부의 examples/research_projects/rag를 기준으로 작성되었습니다.

## RAG 구성 요소
1. generator
2. retriever
> 1. question_encoder
> 2. document_encoder

## 돌아가는 구조 정리
### Class 구조
RagSequenceForGeneration
> ㄴ  RagModel
>> ㄴ  question_encoder: AutoModel(Bert, ... etc)
>>
>> ㄴ  generator: AutoModelForSeq2SeqLM(t5, Bart, ... etc)
>>
>> ㄴ  retriever: RagRetriever

### RagModel
해당 class 내부에서 qustion_encoding, retrieval, generation 모두 일어난다.

 retrieval 중 document_encoding의 경우 미리 데이터셋에 대해 고정된 parameter의 document_encoder로 encoding을 시킨 뒤, ventor index로 저장해 둔 상태에서 question_encoding이 들어올 때 저장해 둔 index와 비교한다.

 이때, index를 저장하는 부분은 meta(구 facebook)의 faiss 라이브러리를 사용한다. 해당 부분을 자세히 알아보고 싶을 시 [use_own_knowledge_dataset.py](https://github.com/huggingface/transformers/blob/main/examples/research_projects/rag/use_own_knowledge_dataset.py) 코드를 참고하는 것을 추천한다.

---
### 참고
* https://github.com/huggingface/transformers/tree/main/examples/research_projects/rag