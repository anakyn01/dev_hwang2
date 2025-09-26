#복사본을 만들고 원본 배열을 변경하고 두배열을 모두표시
import numpy as np
#배열이 데이터를 소유하고 있는지 확인 .base
'''
numpy에서 copy()와 view()의 차이는 메모리 공유 여부를 중심으로  보면됩니다

'''
arr = np.array([1,2,3,4,5])

x = arr.copy() # 원본을 완전히 복사(새 메모리) 자기자신이 데이터 주체 None
y = arr.view() # 원본과 메모리를 공유하는 뷰생성 원본배열을 참조 arr객체

print(x.base)
print(y.base)


#view에서 변경사항 만들기
arr = np.array([1,2,3,4,5])
x = arr.view()
x[1] = 31

#변수를 적용하고 바로 출력하느냐 아니면 변경사항 적용후 동시 출력하는냐에 따라 값은 다르다

print(arr)
print(x)
'''print(x)

x[1] = 31 #시간차를 두고 변경
print(arr)'''


#뷰를 만들고 원래 배열을 변경하고 두배열을 모두 표시합니다
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

arr = np.array([1,2,3,4,5]) #원본 어레이
x = arr.copy() #x는 원본 어레이 카피본
arr[0] = 42

print(arr)
print(x)

'''
Numpy Array Copy vs View
복사와 보기에 차이점
- 복사본은 새로운 배열
- 뷰는 단지 원본 배열의 뷰 입니다
- 뷰는 데이터를 소유하지 않고 뷰에 적용된 모든 변경사항은 원래 배열에 영향을
미치고 원래 배열에 적용된 모드 ㄴ변경 사항은 뷰에 영향을 미칩니다
'''