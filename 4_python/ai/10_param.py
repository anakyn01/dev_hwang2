import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/mid-term-rss3.jsp"
values={
'stnId':'108'
}
params = urllib.parse.urlencode(values)

#요청 전용 url을 생성합니다
url = API + "?" + params
print("url=", url)

#다운로드
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
'''
RSS : 웹사이트나 블로그에 서 새로 올라온 글 뉴스, 콘텐츠를 자동으로 받아볼수
있게 해주는 기술
아래 예제에서는 기상청 rss를 사용해 봅니다
전국 : 108, 서울 경기도 :109
'''