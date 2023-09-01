# Inverse Square Root Learning rate Schedule
## 수식
$$\alpha_t = \alpha_{0} / \sqrt{t}$$

* alpha : learning rate. t는 t시점(step)에서의 learning rate를 나타낸다.
* t : step을 나타낸다.

수식을 보면 현재 시점의 t값의 square root값으로 초기 learning rate 값을 나눠줌으로써 현재 t시점의 learning rate를 scheduling하는 것을 볼 수 있다.

-----
### 출처
* https://velog.io/@good159897/Learning-rate-Decay%EC%9D%98-%EC%A2%85%EB%A5%98
