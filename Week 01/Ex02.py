#올바른 라이브러리 올바르게 사용하기!
import random
# 숫자 맞추기 게임
# 사용자가 1~100 사이의 숫자를 입력하여
# 컴퓨터가 랜덤하게 뽑은 숫자를 맞춘다.
# 사용자가 입력한 숫자가 더 크면 DOWN!!
# 사용자가 입력한 숫자가 더 작으면 UP!!!
# 이 출력되어 사용자가 숫자를 몇번만에 마주는지 확인한다.

userNum = -1
#randint(1, 100) => 1~100 사이의 랜덤한 숫자를 하나 뽑는다.
randNum = random.randint(1, 100)
#사용자가 현재 몇번을 시도하는지 저장할 변수
score = 0
while userNum != randNum:
    print(score+1,"번째 시도")
    userNum = int(input("숫자 입력: "))
    if userNum > randNum:
        print("DOWN!!!")

    elif userNum < randNum:
        print("UP!!")    
    score += 1
print("정답입니다.", score,"번만에 맞췄습니다.")
