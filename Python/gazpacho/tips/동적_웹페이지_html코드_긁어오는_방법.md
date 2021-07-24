# 동적 웹페이지 html코드 긁어오는 방법
------
## 문제 상황

> 어? 왜 내가 원하는  내용이 tag 안에 없지?

이런 경우는 tag 안의 내용이 동적으로 생성되는 부분이였기에 단순히 html 코드만 받아온 상태에서는 이를 긁을 수 없다. 

## 해결법

현재 방식으로는 데이터를 크롤링할 수 없어 나에게 익숙한 라이브러리 대신 생소한 라이브러리를 사용해야 하는 상황이다. 하지만 너무 시간이 없어 다른 라이브러리를 따로 공부해 사용할 수 없는 상황이라면, selenium으로 동적인 페이지를 읽어오고 나머지 작업은 기존 사용하던 라이브러리를 사용해 긁어올 수 있다.

```python
# option과 chrome_option은 자신의 상황에 맞게 사용하자
wd = webdriver.Chrome('chromedriver', options = options, chrome_options = chrome_options)
wd.get('크롤링 할 url')

# gazpacho의 경우 get('url')으로 받아오지만 이는 글의 문제 상황에 직면하게 된다.
# 대신 selenium으로 html 코드를 긁어오면 우리가 원하던 결과를 얻을 수 있게 될 것이다.
html = wd.page_source
soup = Soup(html)

wd.quit()
```

---

### 출처

- [https://conservative-vector.tistory.com/entry/파이썬으로-크롤링하는데-값이-안-읽어와질때-해결법](https://conservative-vector.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%ED%81%AC%EB%A1%A4%EB%A7%81%ED%95%98%EB%8A%94%EB%8D%B0-%EA%B0%92%EC%9D%B4-%EC%95%88-%EC%9D%BD%EC%96%B4%EC%99%80%EC%A7%88%EB%95%8C-%ED%95%B4%EA%B2%B0%EB%B2%95)