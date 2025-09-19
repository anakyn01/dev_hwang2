import numpy as np
#데이터유형을 정수에서 불리언으로 변경
arr = np.array([1,0,3])
newT = arr.astype(np.int8)
print(newT)
print(newT.dtype)
print(newT.dtype.char)

#기존데이터 유형을 변환
arr = np.array([1.6, 2.6, 3.6]) #실수를 정수로 바꿀 .astype('i')
newarr = arr.astype('i')
print(newarr)

#정의된 데이터 유형으로 배열 만들기
arr = np.array([1,2,3,4], dtype='S')
print(arr)

#상황에 따른 변환오류 Nan or value에러
a = np.array(['2','3'], dtype='i')
print(a)

'''넘버인 숫자가 바이트타입인 ASCII코드로 표현된 1byte 문자열로 바뀜'''


arr = np.array([1,2,3,4])
a = np.array([True, False])
b = np.array([1.0, 2.5])
c = np.array([1+2j, 3+4j])
d = np.array(['Hello'])
print(arr.dtype, a.dtype, b.dtype, c.dtype, d.dtype)

#시간 간격
delta = np.timedelta64(5, 'D')
print(delta)
#두날짜 차이

d1 = np.datetime64('2025-09-19')
d2 = np.datetime64('2025-09-24')

print(d2-d1)

'''
NumPy 데이터유형
String : 텍스트 데이터를 나타냄
integer : 정수
float : 실수
boolean : 참 거짓
complex : 복소수[실수 + 허수]1.0 + 2.0j 1.5 + 2.5j
공학,전자,물리학,신호처리,제어,프랙탈 이미지 생성

넘파이에 추가 데이터 유형
dtype : 데이터유형을 리턴

i : integer 음수와 양수를 포함한 정수 
보통 int8, int16, int32, int64등과 비트크기를 명시할수 잇다
b : boolean

u : unsigned integer(부호 없는 정수)
음수가 없는 정수 0이상의 수만 표현이 가능합니다 0, 5, 255 
uint8, uint16등으로 표현됩니다

f : 부동소수점 실수형데이터, 소수점을 표함한 숫자
3.14 -0.001 float32, float64 비트 수에 따라 정밀도가 달라집니다
c : complex float(복소수)
실수부 + 허수부를 가지는 수 예1.0 + 2.0j
complex64, complex128등으로 크기를 명시할수 있다

m : timedelta(시간 간격) 날짜또는 시간의 차이 3일, 2시간 15등
시간 간격계산에 사용됩니다

M : datetime : 절대적인 날짜와 시건을 나타냄 2025-09-19T13:45:00
O : object : 다양한 파이선 객체를 배열에 저장할수  있으나 느리고 메모리를 더사용함
s : string
U : 유니코드 문자열 : 다양한 언어와 특수문자를 표현할수 있음
V : void(raw data) : 다른 유형에 대한 고정 메모리
구조체나 사용자 정의 복합자료형을 표현할때 사용되고 일종의 빈틀로 다른 구조체 타입을 
정의 할수 있습니다
'''