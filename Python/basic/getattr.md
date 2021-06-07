# getattr
---
## 기능

- getattr(object, 'name')이라는 함수는 object 내부의 name이라는 멤버를 반환한다.

## 활용

```python
import my_model as Mo

def build_neural_network(model_name):
  if model_name == 'googlenet':
    model = Mo.googlenet(args)
  elif model_name == 'vgg':
    model = Mo.vgg(args)
  elif model_name == 'resnet':
    model = Mo.resnet(args)
  ..
  ..
  return model
# model_name에 맞는 요소를 불러오기 위해 조건문을 여러번 사용해야 한다.
# 하지만 아래처럼 getattr를 사용하면 한 번에 원하는 model을 가져올 수 있다.
def build_neural_network(model_name):
  return getattr(Mo, model_name)(args)
```

---

### 출처

- [https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=siniphia&logNo=221796316521](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=siniphia&logNo=221796316521)