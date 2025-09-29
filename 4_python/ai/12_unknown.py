import numpy as np

#배열을 평면화 하기
arr = np.array([[1,2,3],[4,5,6]])
newarr = arr.reshape(-1) #다차원이 1차원으로 변경
print(newarr)

arr = np.array([1,2,3,4,5,6,7,8])

newarr = arr.reshape(2, 2, -1)
#첫번째 차원 2개의 블록, 두번째 차원 :각 블록에 두개의 행,
# -1 남은 차원은 numpy내가 자동으로 계산해주라는 의미입니다
print(newarr)

'''
Unknown Dimension
알려지지 않은 차원은 하나 허용됩니다
배열을 재구성 할때 하나에 대한 정확한 숫자를 지정할 필요가 없다는 의미입니다
'''