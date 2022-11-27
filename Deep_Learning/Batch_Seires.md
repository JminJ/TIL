# Batch 시리즈 설명
## Batch란
* 모델을 학습할 때 한 Iteration 당(반복 1회 당) 사용되는 example의 set 모임이다.
## Batch들의 종류 및 소개
### Batch
* 전체 데이터셋을 한 번의 step에 보고 파라미터를 업데이트 한다.
* 전체 샘플을 전부 계산해야 하기에 시간이 많이 소요된다.
* 대용량 데이터의 경우 해당 방법을 사용하기 힘들다(메모리에 모든 데이터를 올릴 수 없기 때문에).

### SGD
* 데이터를 한 개씩 추출해 처리해 보고 이를 전체 데이터에 대해 반복 수행한다. 
* 오차율이 매우크다(수렴은 빠를 수 있으나 global minimum을 찾지 못할 가능성이 있다).
* GPU 성능을 제대로 발휘할 수 없기에 비효율적이다.

### Mini-Batch
* 전체 학습 데이터를 특정 수(batch-size)로 등분해 각 배치 셋을 순차적으로 수행한다.
* batch보다 빠르며 SGD보다 낮은 오차율을 가진다.
----
### 출처
* https://nonmeyet.tistory.com/entry/Batch-MiniBatch-Stochastic-%EC%A0%95%EC%9D%98%EC%99%80-%EC%84%A4%EB%AA%85-%EB%B0%8F-%EC%98%88%EC%8B%9C
