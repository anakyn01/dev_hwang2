import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]]) #2, 4
print(arr.shape)

arr = np.array([[[1,2,3,4,5],[1,2,3,4,5]]], ndmin=6)

print(arr)
print(arr.shape) #(1,1,1,1, 2, 5)
#정답이 그렇게 나오는 이유는 원래배열[1,2,3,4] -> shape(4)
'''
Array Shape : 몇차원 배열인지 몇개의 요소가 있는지 확인
arr = np.array([[1,2,3,4],[5,6,7,8]]) (2,4)

'''