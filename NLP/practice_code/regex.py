import re

text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다. ########################## 58909708798798"

# '#'이 4개 이상이면 '#'으로 치환한다. - sub
regex = re.compile(r'#{4,}')
n_text = regex.sub('#', text)
print(n_text)

# 전화 번호 추출 - search
regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
n_text = regex.search(text)
n2_text = n_text.group()
print(n2_text)

# 문장에서 한글 텍스트만 추출
regex = re.compile(r'[가-힣]+')
n_text = regex.findall(text)
# n2_text = n_text.group()
n2_text = ''
for i in range(len(n_text)):
    n2_text += ' ' + n_text[i]

print(n2_text)