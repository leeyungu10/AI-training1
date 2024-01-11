# 케라스 중 가장 간단한 모델인 시퀀셜 모델을 로딩한다.
from keras.models import Sequential
# 내부 신경만을 구성할 레이더들을 로딩한다.
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense

# 우리는 케라스 모델중 시퀀셜 모델 사용
model = Sequential()
# 입력되는 데이터를 규정하는 코드
# 3차원 배열을 받아들일 것이고, 각 입력값은 [100][1] 배열이다.
# input_shape(100, 1) -> 
# activation -> Conv1D 함수를 쓸 때 사용할 모드를 지정하는데 주로 relu를 이용
# 입력이 끝난 후에는 해당 배열의 차수를 1개 줄인다. 즉 3차원에서 2차원 배열이 된다.
model.add(Conv1D(32, 3, activation='relu', input_shape=(100, 1)))
# 위에서 입력된 데이터를 필터링한다.
model.add(MaxPooling1D(2))
# 필터링 된 데이터를 최종적으로 1차원화 시킨다.
model.add(Flatten())
# 덴스 layer은 입력 뉴런과 출력 뉴런이 연결된 밀집 layer이다.
# 훈련된 데이터를 입력 뉴런에 넣어 출력 뉴런에 보내어 처리한다.
# 하지만 우리가 이 과정은 뇌의 깊은 영역에서 행해지듯
# 자세한 과정을 알 수 없기 때문에 "숨겨진 레이어", "히든 레이어"라고도 부른다.
model.add(Dense(1, activation='sigmoid'))
# 위에 설정 값들을 토대로 모델을 생성한다.
model.compile(optimizer='adam' , loss='binary_crossentropy', metrics=['accuracy'])

import numpy as np
# x_train과 y_train은 모델한테 학습을 시킬 데이터
# 지금의 데이터는 너무 랜덤해서 규칙이 없다는 문제점이 발생.. -> accuracy가 낮게 나옴

# x_train는 3차원 배열..? --> [1000, 100, 1]
x_train = np.random.randn(1000, 100, 1)
print('x_train \n', x_train, "------------------\n")
y_train = np.random.randint(2, size=(1000, 1))
print('y_rain: \n',y_train, "-----------\n")




