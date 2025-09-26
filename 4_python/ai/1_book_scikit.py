'''
아래 예제는 Support Vector Machine 을 이용해서 기계학습으로 해결하는 예제
N차원이라는 공간에서 각 클래스간의 거리를 최대화하는 최적의 선 또는 초평면을 
찾아 데이터를 분류하는 지도형 머신

N차원 공간을 (n-1) 차원으로 나눌수 있는 초평면

XOR 배타적 논리합 연산 두입력값이 다르면 1(true) 같으면 0(false)
단순해 보여도 선형분리가 불가능해 비선형으로 분리 합니다
'''

from sklearn import svm

#xor의 계산결과 데이터
#왜 2차원 배열인가?
'''
바깥쪽 리스트 4개의 요소가 있음 -> 행(row)
개별에 엘리먼트 수 -> 열(column)
'''
xor_data = [#총4개의 조합을 학습데이터로 사용합니다 4행 3열의 2차원 리스트
    #P, Q, result
    [0,0,0], #[0,1,2]
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

#2) 학습을 위해 데이터와 레이블을 분리하기
'''
학습시키기 위한 데이터 변수와 정답레이블 변수
이렇게 해주는 이유는 sckit-learn의 머신러닝을 수행할때 사용하는 fit()매서드의 매개변수를 맞추기 위함 입니다 

'''
data = []
label = []
for row in xor_data: #for 지정된 범위만큼 반복
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p,q]) #0, 1
    label.append(r)

#데이터 학습 하기
'''
svm객체를 만들고 fit()메서드를 사용해 데이터를 학습시킵니다
비선형때문에 Radial Basis Function
'''
clf = svm.SVC() #Radial Basis Function로 비선형 문제 해결
clf.fit(data, label) #주어진 입력값과 정답을 이용해 모델을 학습시킨다

# 데이터 예측하기
pre = clf.predict(data) #데이터를 넣어 예측시킨다 predict()
print(" 기계학습에 예측결과는 ", pre)

#결과 확인하기
ok = 0 #예측이 정답과 일치한 횟수를 저장합니다
total =0 #전체 테스트한 데이터의 수(전체 시도 횟수)를 저장

for idx, answer in enumerate(label):
    '''
    enumerate(label) label리스트의 인덱스와 값을 함께 꺼내옵니다
    label은 정답 리스트 예 [0,1,1,0]
    '''
    p = pre[idx] # p에다 예측결과 리스트 대입 예[0,1,1,0]
    #pre[idx] 예측한 값중에 idx번째 값을 꺼냅니다
    # 이 값(p)과 정답(answer)를 비교해서 맞았는지 확인합니다
    if p == answer: ok += 1
    # 예측값과 정답값 answer가 같으면 맞힌거니까 ok를 1 증가시킵니다
    
    total += 1
    #비교가 한번 끝났으니 전체 테스트 회수도 1증가 시킵니다
print("정답률 : ", ok, "/" , total, "=", ok/total)
'''
p q p xor q
0 0 0
1 0 1
0 1 1
1 1 0
이를 di하려면 머신러닝을 시켜줍니다

xor연산 학습하기
두입력 중에 하나만 참이고
다른한쪽이 거짓일때 참이 나옵니다

이를 제외한 모두 참이거나 모두 거짓인 경우는
거짓인 경우는 거짓이 나옵니다
'''