# A comprehensive guide to memory usage in Pytorch

## DNN 학습 step별 memory 사용 상태
### steps
1. model loading
2. forward pass
3. backward ass
4. optimizer step
5. run next iterations

### 각 step 별 memory 사용 상태
**1. model loading**

model parameter를 GPU로 보낸다.

```
현재 memory : model
```

**2. forward pass**

input을 model에 보내고, 중간(intermediate) output(==activation)을 적재한다. gradient checkpointing 사용 시, 모든 activation을 저장하지 않고 필요한 activation만 저장할 수 있다.
```
현재 memory : model + actications
```

**3. backward pass**

network의 끝에서 시작부분까지 gradient를 연산한다. 이후 forward activation은 제거한다. activation을 제거하면 memory에는 model size의 2배의 memory가 저장되어 있다; 하나는 model weight의 복사본, 나머지 하나는 gradient의 복사본이다.
```
현재 memory : model + gradients
```

**4. optimizer step**
parameter를 업데이트, running optimizer parameter의 trak을 유지한다. 많은 optimizer들은 gradient의 first, second momentum을 측정함으로 parameter들의 track을 유지한다. Adam의 경우 2 momentum을 사용하므로 model size의 2배를 소모하고, RMSProp의 경우 1 momentum을 사용하므로 model size만큼의 memory 양을 소모할 것이다.
```
현재 memory : model + gradients + gradient moments
```

**5. run the next iterations**
처음 iteration이 끝나면 gradient와 moments가 남아있다. 따라서 2번째 step 이후부터는 maximum memory usage가 model + activations + gradients + gradient moments가 된다.

## Pytorch Memory 사용 관련 팁

### Mixed Precision Training
model weight, gradient들을 full 32-bit precision으로 저장하지만, 사용시에는 half precision으로 forward pass를 수행한다. 이는 forward pass 시 사용되는 memory 양을 절반으로 줄일 수 있다.

### Gradient Checkpointing
forward pass 시 사용되는 memory 양을 아낄 수 있는 또 다른 방법으로 학습시간을 조금 더 쓰는 대신 메모리를 아낄 수 있다. forward pass에서 산출되는 activation들을 모두 저장하는 것이 아니라 특정 값들만 저장 후 중간 gradient 연산을 다시 수행하면서 저장 하지 않은 값들을 복원하는 방법이다.

### Distributed Data Parallel(DDP) and memory usage
DDP 사용시, GPU들에 model을 load할 때, model size의 2배 만큼을 사용하는 것을 볼 수 있는데, 이는 "bucket"을 각 GPU에 만들어 다른 GPU로부터 gradient들을 모으는데 사용하기 때문이다. 따라서 DDP 사용시에는 gradient의 copy가 하나 더 사용된다.

### Loading a saved model and memory usage
* 저장된 checkpoint를 불러올 시, Pytorch는 "저장되었던" device에 불러온다. 만약 a checkpoint를 gpu1에서 저장했고 현재 gpu1으로 모델을 학습시키고 있을 때, a checkpoint를 load하면 gpu1로 load되어 OOM이 발생할 수 있다. **따라서 torch.load()시, map_location에 불러올 gpu device를 기입해주어 사용하도록 하자.**
* checkpoint를 불러온 후, model에 checkpoint를 load할 시, model에 load한 이후 checkpoint를 del해주어야 한다; checkpoint는 hang되어 계속 GPU memory를 잡아먹고 있을 것이기 때문이다.

### Saving memory at inference time
inference시에는, 학습때와는 다르게 activation, gradient, ...를 저장, 연산할 필요가 없다. 따라서 torch.no_grad()를 사용해 inference를 수행하도록 하자.

--------
## 출처
* https://medium.com/deep-learning-for-protein-design/a-comprehensive-guide-to-memory-usage-in-pytorch-b9b7c78031d3