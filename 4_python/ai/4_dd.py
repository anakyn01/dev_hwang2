import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(4.0, 1.0, 100000)
'''
결론 4에 표준편차1 3.0 5.0

(loc(평균(mean), : 생성될 숫자들의 중심값 평균 4.0

scale(표준편차), 데이터의 흩어짐 정도를 나타냅니다 1.0에 가까울수록 
평균에서 크게 벋어나지 않는 숫자들이 생성

size(생성할 데이터의 개수) 
'''

plt.hist(x, 100)
plt.show()

'''
Normal Data Distribution : 정규 데이터 분포
주어진 값을 중심으로 값이 집중되 배열을 만드는것
확률론에서 데이터 분포는 정규데이터분포 가우스데이터분포라 합니다
칼 프리드리히 가우스
'''