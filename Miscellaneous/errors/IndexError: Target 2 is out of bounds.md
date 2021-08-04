# IndexError: Target 2 is out of bounds.
-----
## 에러 이유

huggingface를 사용해 trainer로 모델을 학습시키려 하던 도중 에러가 발생하였다. 위 에러의 이유는 다음과 같다.

- 내 데이터의 label은 1, 2로 이루어져 있다. 따라서 from_pretrained()내의 인자인 num_labels를 2로 설정해 두었다.

## 해결법

해결법은 간단하다. pytorch를 사용해 구성되어있기에 num_labels를 내 끝 label개수 + 1로 설정해주면 된다.

- from_pretrained('...', num_labels = 2) → from_pretrained('...', num_labels = 3)

---

### 출처

- [https://stackoverflow.com/questions/60259836/cnn-indexerror-target-2-is-out-of-bounds](https://stackoverflow.com/questions/60259836/cnn-indexerror-target-2-is-out-of-bounds)