# Temperature
-----
## Soft label, Hard label?

<img src='/image/2021_06_01_01.png' width = '70%'>

 위 그림의 왼쪽은 Hard label을, 오른쪽은 Soft label을 표기했다. 그림에서 조금은 감을 잡을 수 있듯이 Hard label은 오로지 고양이면 고양이만 1로 표기하므로 곰, 고양이, 강아지의 유사한 점에 대한 정보는 모두 손실된다. 그러나 Soft label은 유사한 점들까지 보존이 가능하다.

## Temperature

 일반적인 Softmax 함수는 입력 값이 큰 부분은 매우 큰 값을, 작은 부분은 매우 작은 값을 주는 경향을 가지고 있다. Temperature는 이러한 성질을 완화해주는 담당을 하며 작은 부분은 더 크게, 큰 부분은 조금 작게 해준다.

<img src='/image/2021_06_01_02.png' width = '70%'>

- 왼쪽은 일반적인 softmax, 오른쪽은 temperature를 적용한 softmax이다.

<img src='/image/2021_06_01_03.png' width = '70%'>

- 간단한 예시

---

### 출처

- [https://light-tree.tistory.com/196](https://light-tree.tistory.com/196)