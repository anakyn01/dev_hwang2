import re

txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)
'''
[a-m] : a와 m사이의 모든 소문자를 대문자를 제외하고 써진 순서대로 배열됩니다
\d
.
^
$
*
+
?
{}
|

'''

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
y = re.findall("ai", txt)
print(y)


if x:
    print("YES! match")
else:
    print("No match")

x = re.findall("Portugal", txt)
print(x)

x = re.split("\s", txt, 1)
print(x)

x = re.sub("\s", "+++", txt, 2)
print(x)

reg = '''
파이선 정규식 :
정규표현식은 (RegEx) 검색 패턴을 형성하는 문자 시퀀스..
정규표현식을 사용하면 문자열에 지정된 검색패턴이 포함되어 있는지 확인

정규식 함수 
- findall() : 모든 일치항목을 포함하는 목록을 리턴
- search() : 문자열에서 일치항목을 검색하고 일치항목이 있으면 매칭된 객체를
반환 합니다 그런데 일치항목이 두개 이상인 경우 첫번째로 나타난 일치항목
귤검색  귤귤귤
일치항목이 없으면 none리턴

- split () 각일치 항목에서 문자열이 분활된 목록을 리턴
- sub () : 매칭한 항목을 선택한 텍스트로 바꿉니다

'''