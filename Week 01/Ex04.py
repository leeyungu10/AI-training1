# 로또 번호 추첨기를 만들어보세요.
import random

# 로또 번호를 저장할 리스트
lottoNum = []
# 1~45 사이의 랜덤한 숫자를 뽑고 리스트에 저장한다.
for i in range(0, 6):
    temp = random.randint(1, 45)
    if lottoNum.count(temp) == 0:
        lottoNum.append(temp)        
    lottoNum.sort()
print(lottoNum)

# 객체는 class 데이터 형식을 가진 변수
# 작은 프로그램들이 모여서 만들어진 것
# 3시간 남았다. 파이팅!!
