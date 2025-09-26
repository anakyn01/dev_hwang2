import numpy as np
import matplotlib.pyplot as plt #파이선 시각화

x = np.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()
#print(x)
'''
실제 생활에서도 그렇고 가상세계에서도 빅데이터를 얻는 법은 쉽지 않습니다
그러나 테스트나 실제 프로그래밍에서 필요하기에
그럴때 numpy를 사용합니다
아래에는 0 ~5 사이의 난수 250개를 포함하는 배열을 만듭니다
'''