import numpy as np

ar = np.array([1,2,3,4,5,6,7,8])
newTop = ar.reshape(2,4)
print(newTop)

ar = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newar = ar.reshape(2, 3, 2)
#(첫번째 차원 깊이, 두번째 차원(행), 세번째 차원(열))
#전체 원소개수는 2 X 3 x 2 = 12 기존 원소 수와 같아야 reshape가 가능합니다
print(newar)




arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
#1차원 배열(벡터)arr를 만든다
newarr = arr.reshape(3, 4)
print(newarr)

'''
배열 재구성 [배열의 모양{각 차원의 요소수}을 바꾸는 것을 의미합니다]
Array Reshaping
재구성을 통해 차원을 추가하거나 제거할수 있고
각차원의 요소갯수를 변경할수 있습니다
'''