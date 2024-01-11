# 절차지향적 언어의 관점으로
# 붕어빵을 만드는 기계를 구현해보자

#1세대 단순 코딩

print("무슨 붕어빵을 주문하시겠습니까?")
user_choice = input()
print("몇 개를 주문하시겠습니까?")
user_qnt = input()
print(user_choice,"를 ", user_qnt,"개 만듭니다.")

#2세대 절차지향적 코딩


def redbean(user_qnt):
    print("팥 붕어빵을 ", user_qnt, "개 만듭니다.")

def shucream(user_qnt):
    print("슈크림 붕어빵을 ", user_qnt, "개 만듭니다.")

def mintchoco(user_qnt):
    print("민초 붕어빵을 ", user_qnt, "개 만듭니다.") 

print("무슨 붕어빵을 주문하시겠습니까?")
print("1. 팥 2. 슈크림 3. 민초")
user_choice = input()
print("몇 개를 주문하시겠습니까?")
user_qnt = input()

if user_choice == 1:
    redbean(user_qnt)
elif user_choice == 2:
    shucream(user_qnt) 
elif user_choice == 3:
    mintchoco(user_qnt)

# 3세대 객체지향적 코딩
class bread:
    def __init__(self):
        self.type = ""
        self.qnt = 0
    def make(self):
        print(self.type, "을 ", self.qnt, "개 만듭니다.")


a = bread()
a.type = "초코 붕어빵"
a.qnt = 10
a.make

# numpy는 행렬 계산 -> AI 이용할 때 다차원의 데이터 행렬을 1차원으로 계산하여 주입

# 

