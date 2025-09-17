#값이 42인 0차원 배열을 만듭니다
import numpy as np

#3차원 이상은 ndmin으로 차원수를 정의 할수 있습니다
newArr = np.array([1,2,3,4], ndmin=5)

print(newArr)
print('number of dimensions :', newArr.ndim)
'''
이 배열에는 가장안쪽차원(5번째 차원에는) 4개의 요소가 있고
4번째 차원에는 백터인 요소가 한개있고
3번째 차원에는 백터를 포함한 요소가 한개있고
2번째 차원에는 3차원 배열인 요소가 한개있고
1번째 차원에는 4차원 배열인 요소가 1개 있다
'''

#몇 차원인지 확인 하는것 .ndim
a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a.ndim, b.ndim, c.ndim, d.ndim)

arr = np.array(42)
print(arr)
#3차원 배열
arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)

#2차원 배열 ([[],[]]) x [],[] 이는 종종 행렬이나 텐서(Tensor)를 나타내는데 사용
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
'''
Creating Arrays
0 ~ 3차원 배열
'''