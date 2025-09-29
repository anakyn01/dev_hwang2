'''텍스트기반 다운로드 받아서 출력'''
import urllib.request

#데이터 읽기 인코드(코드화 암호화를)의미한다 한자로 부호화
#반대말은 디코딩(복호화)
#데이터를 컴퓨터가 이해할수 있는 바이너리형식으로 변환
#디코딩

url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

#바이너리를 문자열로 변환
text = data.decode("utf-8")
print(text)

