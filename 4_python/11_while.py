#4)else 문을 사용하면 조건이 더이상 참이 아닐때 코드블록을 한번 실행할수 있다
# 컴퓨터과학에서 특정형식에 데이터를 분석하여 컴퓨터가 이해할수 있는
# 구조화된 형식을 변환하는 과정
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("6 else를 쓰면 원하는 출력을 한번 더 할수 있습니다")
    
#3)continue를 사용하면 현재 반복을 중지하고 다음반복을 계속할수 있습니다
i = 0
while i < 7:
    i += 1
    if i == 3:
        continue #지정한 숫자나 문자를 건너뛰고 계속 실행
    print(i)

#2)break문을 사용하면 while조건이 참이더라도 루프를 중지할수 있습니다
i = 1
while i < 6:
#조건 추가
    print(i)
    if i == 3:
        break
    i += 1

#1)i가 6보다 작을때 까지 반복하세요(0,1,2,3,4,5)를 개별로 출력하세요
#start index 는 개발자가 정합니다
q = 0
while q < 6:
    print(q)
    #이표시를 하지 않으면 에러가 발생하고 무한루프가 됩니다
    q += 1 #q는 1씩 증가하라


'''
Python loop while, for
'''