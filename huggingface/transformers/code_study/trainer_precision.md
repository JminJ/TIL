# Trainer Precision

## Intro
LoRA를 사용해 T5를 학습시킬 때 Trainer에 들어가는 fp16/bf16인자가 어떻게 사용되는지 궁금해 살펴보게 되었다.
> transformers version : 4.33.2(2023.09.21)

## mixed_precision(fp16/bf16케이스)
Trainer class의 _wrap_model() 함수 내에서 진행되며 FullySharedDDP로 감싸게 되는데 이때 fp16 또는 bf16이 True일 시 FullySharedDDP의 mixed_precision 인자에 True가 들어가게 된다.
```Python
# Distributed training (should be after apex fp16 initialization)
        if self.sharded_ddp is not None:
            # Sharded DDP!
            if self.sharded_ddp == ShardedDDPOption.SIMPLE:
                model = ShardedDDP(model, self.optimizer)
            else:
                mixed_precision = self.args.fp16 or self.args.bf16 #### --> fp16 또는 bf16이 True일 시 mixed_precision을 True로
                cpu_offload = ShardedDDPOption.OFFLOAD in self.args.sharded_ddp
                zero_3 = self.sharded_ddp == ShardedDDPOption.ZERO_DP_3
                # XXX: Breaking the self.model convention but I see no way around it for now.
                if ShardedDDPOption.AUTO_WRAP in self.args.sharded_ddp:
                    model = auto_wrap(model)
                self.model = model = FullyShardedDDP(
                    model,
                    mixed_precision=mixed_precision, #### --> mixed_precision 값이 들어간다
                    reshard_after_forward=zero_3,
                    cpu_offload=cpu_offload,
                ).to(self.args.device)
...
```

## 8bit load
반면 model을 8bit로 로드할 경우는 DDP를 지원하지 않는다고 하며, nn.DataParallel을 사용해 model을 감싼다.
```Python
# Multi-gpu training (should be after apex fp16 initialization) / 8bit models does not support DDP
if self.args.n_gpu > 1 and not getattr(model, "is_loaded_in_8bit", False):
model = nn.DataParallel(model)
...
```