import pandas as pd
from sklearn import linear_model

df = pd.read_csv("car.csv")

X = df[['Weight', 'Volume']] #입력값 특성 무게와 부피 두개의 특성
y = df['CO2'] #co2배출량
#CO2 = a x Wight + b x Volume + c

#선형회귀 모델 생성
regr = linear_model.LinearRegression()
regr.fit(X, y) #데이터를 사용하여 모델 학습
#모델이  Weight와 Volumn의 영향을 학습해서 CO2를 예측하는 식을 만듬

predictedCO2 = regr.predict([[2300, 1300]])
#기계학습 한걸로 새로운 데이터 예측
print(predictedCO2)
'''
Multiple Regression 다중 회귀(입력값에 따라 연속적인 숫자를 예측)
두개이상의 독립적인 값을 상요해 예측
1시간 40
2시간 55
3시간 70
4시간 ???점
- 선형회귀와 유사하지만 두개 이상의 독립적인 값을 사용합니다
'''