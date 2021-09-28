# tar
-------
## 설명

- 압축 파일이 아닌 여러개 파일을 하나로 묶는다
- 소비되는 시간이 적고 리소스가 상대적으로 적다
- 하지만 압축 후 용량이 거의 줄지 않는다

## 압축하기

> tar 압축하기
> 
- tar -cvf [파일명.tar] [폴더명]

> tar.gz 압축하기
> 
- tar -zcvf [파일명.tar.gz] [폴더명]

## 압축 풀기

> tar 압축풀기
> 
- tar -xvf [파일명 tar]

> tar.gz 압축 풀기
> 
- tar -zxvf [파일명.tar.gz]

## [추가] tar.gz

- 압축시 용량이 크게 줄고 리소스를 많이 쓰지 않는다. **다만 tar.bz2보다는 압축률이 떨어진다**

---

### 출처

- [https://devpouch.tistory.com/100](https://devpouch.tistory.com/100)