import keras
import numpy as np
import matplotlib.pyplot as plt

# 주어진 훈련 데이터
data = np.array([
    [1, 1], [1, 0],
    [2, 1], [2, 0],
    [3, 1], [3, 0],
    [4, 1], [4, 0],
    [5, 1], [5, 0]
], dtype=int)

# 훈련 레이블
labels = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Keras 모델 정의
model = keras.Sequential([
    keras.layers.Input(shape=(2,)),
    keras.layers.Dense(len(labels), activation='softmax')
])

# 모델 컴파일
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 훈련 과정을 저장하기 위한 변수
history = model.fit(data, labels, epochs=700, verbose=1, validation_split=0.2)

# 훈련 과정 시각화
plt.figure(figsize=(12, 4))

# 훈련 손실과 검증 손실
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# 훈련 정확도와 검증 정확도
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()