# Pytorch num_workers

## 학습에 사용될 데이터가 위치할 수 있는 영역
1. 보조저장장치 메모리(HDD, SSD)
2. CPU의 RAM
3. GPU의 메모리

## GPU로 학습시
gpu로 학습시, torch의 Dataset의 \_\_getitem\_\_()에서 보조저장장치 메모리에 위치한 데이터를 CPU의 RAM으로 가져온다. 이후 .to("cuda")와 같은 방법으로 GPU의 메모리에 데이터를 보낸다.

```
그러나 GPU의 학습 속도와 CPU의 dataloader의 작업 속도가 서로 다르므로 dataloader는 이를 보완하기 위해 multiprocessing을 통해 이때 사용할 multiprocessing의 수가 num_workers이다.
```

## 적절한 num_workers
하지만 무조건 num_workers 값이 높다고해서 좋은 것은 아니다. 너무 적을 시 멀티프로세싱의 효과를 덜 보기에 느릴 것이고, 너무 많으면 프로세스끼리 합을 맞추기 위해 들어가는 오버헤드가 더 크기 때문에 오히려 느려질 것이다.

* 추천하는 num_workers 값 공식
> 1. num_workers = 4 * num_GPU(or 8, 16, 2 * num_GPU)
> 2. num_workers = entry * batch_size * num_worker = num_GPU * GPU_throughtput
> 3. num_workers = batch_size / num_GPU
> 4. num_workers = batch_size / num_CPU

--------
## 출처
* https://velog.io/@seokjin1013/PyTorch-numworkers%EC%97%90-%EA%B4%80%ED%95%98%EC%97%AC