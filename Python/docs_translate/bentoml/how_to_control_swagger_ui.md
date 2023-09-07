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

### Error Handling

api의 인자값으로 요구되는 “title”이 없을 경우 어떻게 에러를 처리할 수 있을까요? pydantic의 root_validator 데코레이터를 통해 처리를 할 수 있습니다.

```python
import bentoml
from bentoml.io import JSON
from pydantic import BaseModel, root_validator

class ExFeatures(BaseModel):
	# json key들을 선언
	title: str
	error_code: Optional[str] = None
	# 추가 옵션을 기입(example 등)
	
	@root_validator(pre=True)
	def check_key(cls, values):
		keys = values.keys()
		if "title" not in keys:
			values["error_code"] = "NOT_IN_TITLE"

		return values
	
  class Config:
		schema_extra = {
			"example": {
				"title" : "삼성전자, 삼성페이 서비스를 론칭하다."
			}
		}
```

check_key함수 내의 values는 endpoint에서 입력한 json을 dict로 변환한 값입니다. 따라서 key값을 추출할 수 있고 필요한 키가 keys에 들어있는지 확인이 가능합니다.
 

```python
import bentoml
import json
from bentoml.io import JSON
from pydantic import BaseModel, root_validator
from typing import Optional

class ExFeatures(BaseModel):
	# json key들을 선언
	title: str
	error_code: Optional[str] = None
	# 추가 옵션을 기입(example 등)
	
	@root_validator(pre=True)
	def check_key(cls, values):
		keys = values.keys()
		if "title" not in keys:
			values["error_code"] = "NOT_IN_TITLE"

		return values
	
  class Config:
		schema_extra = {
			"example": {
				"title" : "삼성전자, 삼성페이 서비스를 론칭하다."
			}
		}

@svc.api(input=JSON(pydantic_model=ExFeatures), output=JSON()) # pydantic_model인자에 위에서 선언한 ExFeatures 클래스를 넣어줍니다
def classify(input_data):
	try:
		if input_data.error_code == "NOT_IN_TITLE":
			raise ValueError("title인자가 입력되지 않았습니다")
		...
	except ValueError:
     return json.dump({"status" : -1, "detail" : "title 인자를 입력해 주십시오"}, ensure_ascii=False)
```

위와 같이 check_key함수를 통해 error_code의 값을 지정해 주고 classify 함수 내에서 error_code의 값이 특정 값일 경우 Error를 raise해 endpoint에 문제 상황을 전달 할 수 있습니다.

### 참고

- https://docs.bentoml.com/en/latest/reference/api_io_descriptors.html#structured-data-with-json