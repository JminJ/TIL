# Learning rate Warmup
---

 모델 생성 시 learning rate를 초기화 할 때 랜덤으로 초기화 하기에 이때 큰 값으로 초기화 되면 학습이 잘 이루어 지지 않는다. 운동 하기 전 몸을 풀듯 모델도 본격적인 학습 전 몸을 풀어주는 개념이라 생각하면 된다. 

 학습 초반에 0에 가까운 값부터 천천히 우리가 원하는 learning rate값으로 올려주면 된다. 

---

### 출처

- [https://medium.com/curg/딥러닝-성능을-높이기-위한-다양한-꿀팁들-1910c6c7094a](https://medium.com/curg/%EB%94%A5%EB%9F%AC%EB%8B%9D-%EC%84%B1%EB%8A%A5%EC%9D%84-%EB%86%92%EC%9D%B4%EA%B8%B0-%EC%9C%84%ED%95%9C-%EB%8B%A4%EC%96%91%ED%95%9C-%EA%BF%80%ED%8C%81%EB%93%A4-1910c6c7094a)