import keras
import numpy as np
from keras.callbacks import ReduceLROnPlateau

data = np.array([
    [1, 1], [1, 0],
    [2, 1], [2, 0],
    [3, 1], [3, 0],
    [4, 1], [4, 0],
    [5, 1], [5, 0]
], dtype=int)
age_input = np.array(['10대 남성', '10대 여성', '20대 남성', '20대 여성', '30대 남성', '30대 여성', '40대 남성', '40대 여성', '50대 남성', '50대 여성'])
labels = np.array(['만화', '화장품', '게임', '의류', '건강식품', '애완동물 관련', '자전거', '골프', '낚시', '수험생'])

model = keras.Sequential([
    keras.layers.Input(shape=(2,)),
    keras.layers.Dense(len(labels), activation='softmax')
])  

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 검증 데이터 생성
validation_data = (data, np.arange(len(labels)))

# 학습률을 동적으로 조절하는 콜백 추가
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=0.0001)

# 모델 학습 (콜백 추가)
model.fit(data, np.arange(len(labels)), batch_size=1, epochs=7000, verbose=1, validation_data=validation_data, callbacks=[reduce_lr])

while True:
    age1 = int(input('나이를 입력하세요(229이하): '))
    age = age1 // 10
    gender = input('성별을 입력하세요 (남성 또는 여성): ')
    
    if gender == '남성' or gender == '남' or gender == 'ㄴ' or gender == '남자' or gender == 's':
        gender_code = 1 
    else:
        gender_code = 0
    predicted_label = np.argmax(model.predict(np.array([[age, gender_code]])))                                                                                                              
    print("%f가 가장 관심이 있을 것으로 예측되는 상품은 %f입니다."%(age_input[predicted_label], age_input[predicted_label] ))
