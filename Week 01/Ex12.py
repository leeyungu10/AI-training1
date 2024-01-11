#import tensorflow as tf
#import numpy as np
import keras

# keras 내부의 손글씨 데이터베이스 -> mnist
# 손글씨 이미지 데이터 전처리 과정
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train /= 255
x_test /= 255
# categorical은 결과값이 몇 가지로 나오는 거 -> 10으로 하면 0 - 9
# 손글씨는 왜 0 - 9까지일까? -> 내장된 데이터가 숫자로만 구성됨..!
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=(28, 28)))
# 이때, 128은 우리가 돌릴때 사용할 뉴런의 수를 지정
# 첫번째, 레이어에서 input값을 받고 1차 처리 담당
model.add(keras.layers.Dense(128, activation='relu'))
# softmax는 분류를 위해서 사용하는 활성화 함수랑 갯수
# 두번째 레이어에서 처리된 데이터를 가지고 분류를 해야될 때 softmax 사용
model.add(keras.layers.Dense(10, activation='softmax'))
# 최적화 함수는 SGD
model.compile(optimizer='SGD', loss='categorical_crossentropy', metrics=['accuracy'])

# validation_split은 퍼센트로 전체 데이터에서 퍼센트 비율만큼 짤라서 검증에 이용
# 즉, 0.2이면 80%는 훈련, 20%는 검증에 이용
model.fit(x_train, y_train, batch_size=64, epochs=400, verbose=1, validation_split=0.4)

test_loss, test_acc = model.evaluate(x_test,y_test)
print("정확도: ", test_acc)


