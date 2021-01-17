# 'float' object has no attribute 'lower' #
------------------------------

## Why? ##
* pandas의 read_csv 파일을 읽었을 경우 에러가 발생
* read_csv는 datatype을 스스로 바꿀 수 있기 때문에 이러한 오류가 생김

## 해결 ##
* korean.iloc[:,1]=korean.iloc[:,1].astype(str)
* dataframe 중 사용할 열을 문자열로 바꿔주어서 이 오류를 해결하였다.

---------------
## 출처 ##
* <http://blog.naver.com/PostView.nhn?blogId=pica4star&logNo=221532459431&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView>
