# Deploy a Transformer model with BentoML

## bentoml service 작업 flow 정리
1. Transformer framework model을 불러오고, `bentoml.transformers.save_model(...)` 함수를 통해 bento_model로 저장한다.
```Python
import transformers
import bentoml

model= "sshleifer/distilbart-cnn-12-6"
task = "summarization"

bentoml.transformers.save_model(
    task,
    transformers.pipeline(task, model=model),
    metadata=dict(model_name=model),
)
```
2. api의 endpoint 함수를 작업하는 service.py에서 1번 작업에서 저장한 bento_model을 `bentoml.models.get(...)` method를 통해 runner로 가져온다(아래 코드에서는 summarizer_runner).
```Python
summarizer_runner = bentoml.models.get("summarization:latest").to_runner()
```

3. `bentoml.Service()`로 runner를 감싸 Service를 생성한다(아래 코드에서의 svc); 이때, 여러개의 runner를 가질 수 있다.
```Python
svc = bentoml.Service(
    name="summarization", runners=[summarizer_runner]
)
```

4. 3번 작업에서 생성한 Service instance decorator를 사용해 endpoint 함수를 생성한다. 이 endpoint에서 우리는 bento_model으로 summarization 작업을 수행할 것이다.
```Python
@svc.api(input=bentoml.io.Text(), output=bentoml.io.Text())
async def summarize(text: str) -> str:
    generated = await summarizer_runner.async_run(text, max_length=3000)
    return generated[0]["summary_text"]
```

------
### 출처
* https://docs.bentoml.com/en/latest/quickstarts/deploy-a-transformer-model-with-bentoml.html