# 케라스 시퀀스 모델 로딩
from keras.models import Sequential
# 케라스 레이어 로딩
from keras.layers import Dense

# x: -100 ~ 100 까지의 정수 값들
import numpy as np

x_train = np.arange(-100, 101, 1)
y_train = 2*x_train + 1
# 지금까지의 데이터는 너무 100부터 0까지 순차적으로 이뤄짐 그래서 섞음
# 이를 통해 모델이 특정 순서에 의존하지 않고 다양한 패턴을 학습할 수 있게 됩니다.
index = np.arange(x_train.shape[0])
np.random.shuffle(index)

x_train = x_train[index]
y_train = y_train[index]

# 현재 x_train은 1차원 배열
# 훈련용은 세로로 길게 만들어줘야 됨(행렬의 형태)
# reshape(x, y) x는 왼쪽 행의 갯수 y는 열의 갯수
x_train = x_train.reshape(-1, 1)

# Sequential 모델 생성
model = Sequential()
# 생성된 모델에 댄스 레이어 추가
model.add(Dense(units=1, input_shape=(1,)))
# mse는 평균값 구해서 표준오차 벗어난 데이터를 패스함
model.compile(optimizer='adam', loss= 'mse', metrics=['accuracy'])
# batch_size는 훈련할때 데이터를 얼마 단위로 짤라서 학습을 시킬 건지 결정
# 너무 크게 짜르면 훈련 성립x
# 너무 작으면 훈련양이 극대화
model.fit(x_train, y_train, epochs= 100, batch_size=5)
# 결과가 정확한 지 확인 하기 위해 x값을 x_test로 생성
x_test = np.arange(1, 11, 1)
y_test = 2*x_test+1
print(model.predict(x_test))
print(y_test)


# 볼버스 값?

