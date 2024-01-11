# 훈련용 데이터 만들기
import random
import numpy as np
import keras
x_train = []
x_test = []
for i in range(1, 10000):
    age = random.randint(10, 59)
    gender = random.randint(0, 1)
    if i < 9000:
        x_train.append((age, gender))
    else:
        x_test.append((age, gender))
x_train = np.array(x_train)
x_test = np.array(x_test)
#print(x_train.shape)
#print(x_test.shape)
y_train = []
y_test = []
for x in x_train:
    if x[1] == 0:
        y_train.append(2*((x[0] // 10)-1))
        # if x[0] // 10 == 1:
        #     y_train.append(0)
        # elif x[0] // 10 == 2:
        #     y_train.append(2)
        # elif x[0] // 10 == 3:
        #     y_train.append(4)
        # elif x[0] // 10 == 4:
        #     y_train.append(6)
        # elif x[0] // 10 == 5:
        #     y_train.append(8)

    elif x[1] == 1:
        y_train.append(2*((x[0] // 10)-1) + 1)
        # if x[1] // 10 == 1:
        #     y_train.append(1)
        # elif x[1] // 10 == 2:
        #     y_train.append(3)
        # elif x[1] // 10 == 3:
        #     y_train.append(5)
        # elif x[1] // 10 == 4:
        #     y_train.append(7)
        # elif x[1] // 10 == 5:
        #     y_train.append(9)

print(len(y_train))
for x in x_test:
    if x[1] == 0:
        y_test.append(2*((x[0] // 10)-1))
        # if x[0] // 10 == 1:
        #     y_test.append(0)
        # elif x[0] // 10 ==2:
        #     y_test.append(2)
        # elif x[0] //10 ==3:
        #     y_test.append(4)
        # elif x[0] // 10 == 4:
        #     y_test.append(6)
        # elif x[0] // 10 == 5:
        #     y_test.append(8)

    elif x[1] == 1:
        y_test.append(2*((x[0] // 10)-1) + 1)
        # if x[1] // 10 == 1:
        #     y_test.append(1)
        # elif x[1] // 10 == 2:
        #     y_test.append(3)
        # elif x[1] // 10 == 3:
        #     y_test.append(5)
        # elif x[1] // 10 == 4:
        #     y_test.append(7)
        # elif x[1] // 10 == 5:
        #     y_test.append(9)

# 데이터의 실수화 왜..?
# 컴퓨터 처리 속도를 올리기 위함!
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)
model = keras.models.Sequential()
#model.add(keras.layers.Flatten(input_shape=(2,0))) -> 평면 모델이라서 Flatten 필요 없음
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))
model.compile(optimizer='SGD', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=100, epochs=300, verbose=1, validation_split=0.1)

test_loss, test_acc = model.evaluate(x_test, y_test)

print('정확성: ', test_acc)

user_age = int(input("나이: "))
user_gender = input("성별 (0: 남자 1: 여자): ")
user_data = [(user_age // 10, int(user_gender))]
user_data = np.array(user_data)
print(model.predict(user_data))




