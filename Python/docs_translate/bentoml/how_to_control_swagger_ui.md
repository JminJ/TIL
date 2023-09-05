# How to control swagger ui in bento service.py?
```
해당 가이드는 LTS버전이 아닌 latest 버전 기준입니다(23.09.05)
```
## JSON input/ output 사용

```python
import bentoml
from bentoml.io import JSON

svc = bentoml.Service("...", runners=[...])
@svc.api(input=JSON(), output=JSON())
def classify(input_data:JSON):
	...
```

위와 같은 예제 service.py파일이 있다고 할 때, classify 엔드포인트에 대한 swagger ui를 편집하기 위해서는 pydantic library의 BaseModel을 활용한 class를 선언해 주어야 한다; **단 현재(23.09.05)의 경우 bentoml-cli에서 pydantic버전이 2이상일 경우 호환이 되지 않으므로 1점대의 버전을 설치해 주어야 합니다.**

```python
import bentoml
from bentoml.io import JSON
from pydantic import BaseModel

### adding part
class ExFeatures(BaseModel):
	# json key들을 선언
	title: str
	
	# 추가 옵션을 기입(example 등)
  class Config:
		schema_extra = {
			"example": {
				"title" : "삼성전자, 삼성페이 서비스를 론칭하다."
			}
		}

###
svc = bentoml.Service("...", runners=[...])
@svc.api(input=JSON(pydantic_model=ExFeatures), output=JSON()) # pydantic_model인자에 위에서 선언한 ExFeatures 클래스를 넣어줍니다
def classify(input_data:ExFeatures):
	...
```