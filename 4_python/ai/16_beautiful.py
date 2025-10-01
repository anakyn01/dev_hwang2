from bs4 import BeautifulSoup #라이브러리 불러오기

#짭 데이터 만들기
html = """
<html><body>
<h1 id="title">스크래핑이란</h1>
<p id="body">웹페이지의 원하는 부분을 추출</p>
<p>난위에 있는 p에 형제요소 원장님 이름 최형제</p>
</body></html>
"""

#html분석하기
soup = BeautifulSoup(html, 'html.parser')

#원하는 부분 추출하기
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

title = soup.find(id="title")
body = soup.find(id="body")

print("h1 = " + h1.string)
print("p = " + p1.string)
print("p = " + p2.string)
print("#title = " + title.string)
print("#body = " + body.string)
'''
파이선으로 스크래핑을 할때 절때 빼놓을수 없는 라이브러리가
beautifulSoup입니다
이를 이용하면 html과 xml을 분석해 줍니다
설치
pip install beautifulsoup4
'''