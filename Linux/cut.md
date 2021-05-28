# cut
-----
> 문자열을 자르는데 주로 사용된다. 특정 구분자를 지정해줄 수도 있다

## 문법 & 옵션

- cut option filename
- -b (—byte) : byte를 기준으로 자른다
- -c (—character) : 문자수 기준으로 자른다
- -f (—fields) : field 수 기준으로 자른다
- -d (—delimiter) : field 기준자를 정한다

## 사용법

```bash
cut -f 1 -d ',' > ex.csv
```

- delimiter의 기본값은 tab이다.
- 여러 열을 뽑고 싶다면 -f 1,2,3,....으로 해주면 된다.

---

### 출처

- [https://jhnyang.tistory.com/145](https://jhnyang.tistory.com/145)