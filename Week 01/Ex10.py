# 케라스 중 가장 간단한 모델인 시퀀셜 모델을 로딩한다.
from keras.models import Sequential
# 내부 신경만을 구성할 레이더들을 로딩한다.
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense

model = Sequential()
model.add(Conv1D(32, 3, activation='relu', input_shape=(100, 1)))
model.add(MaxPooling1D(2))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam' , loss='binary_crossentropy', metrics=['accuracy'])

import numpy as np
# x_train과 y_train은 모델한테 학습을 시킬 데이터
# 지금의 데이터는 너무 랜덤해서 규칙이 없다는 문제점이 발생.. -> accuracy가 낮게 나옴
 
x_train = np.random.randn(1000, 100, 1)
#print('x_train \n', x_train, "------------------\n")
y_train = np.random.randint(2, size=(1000, 1))
#print('y_rain: \n',y_train, "-----------\n")

# 훈련시작
# epochs는 훈련 횟수
# 훈련 횟수를 높이면 정확도는 상승 손실률은 감소
# accurary가 1이 넘어가는 순간 그 뒤에 훈련은 의미X
model.fit(x_train, y_train, epochs=500, batch_size=32)
x_predict = np.random.randn(10, 100, 1)
y_predict = model.predict(x_predict)
results = model.evaluate(x_predict, y_predict)
print("\n\nresults: \n\n", results)




