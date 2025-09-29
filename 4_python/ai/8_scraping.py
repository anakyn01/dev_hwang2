import urllib.request

#2)url과 저장경로 지정
url = "http://uta.pw/shodou/img/28/214.png"
savename = "nobody_Help_Me.png"
#now.jpg

#3)다운로드
urllib.request.urlretrieve(url, savename)
print("저장 되었습니다")

'''
파이선에서는 데이터를 추출하기위해 urllib 라이브러리를 사용합니다
이를 사용하면 HTTP또는 ftp를 사용해서 데이터를 다운로드 할수 있습니다
urllib 은 url을 다루는 모듈을 모아 놓은 패키지 입니다
파일을 다운로드 할때는 urllib.request 모듈에 있는 urlretrieve()함수를
사용합니다 이를 통해 직접파일을 다운로드 합니다

스크레핑 크롤링 데이터가공
scraping : 웹사이트에 있는 특정정보를 추출하는 기술을 의미
웹에 공개된 정보는 대부분 html이다 이를 데이터로 사용하려면 
데이터 가공이 필요합니다 로그인한것과 하지 않은것을 둘다 사용해야됨

crawling : 웹사이트를 정기적으로 돌며 정보를 추출하는 기술
크롤러 또는 스파이더라 합니다

데이터가공 : 웹에서 내려받은 데이터를 곧바로 머신 러닝에 사용하지 못합니다
데이터 구조를 분석하고 필요한 부분만 추출합니다

머신러닝에 활용되는 대표적인 형식 pandas csv, json, xml, yaml[사람이 읽을수 있는 데이터 직렬화 언어]
'''