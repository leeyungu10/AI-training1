#기본적인 사칙연산
# +, -, *, / -> 앞 뒤의 값을 연산한다.
# // -> 몫만 계산한다.
# % -> 나머지만 계산한다.

# 변수
# 내가 필요한 값을 저장하고 언제든 접근 가능한 공간
a = 50 
b = 10
print(a+b)

b = 20
print(a+b)

# 함수
def printVars(a, b):
    print("a + b", a+b)
    print("a - b", a-b)
    print("a * b", a*b)
    print("a / b", (a/b))

printVars(a, b)

# 제어문
if a < b:
    print("b가 더 큽니다.")
else: 
    print("a가 더 큽니다.")

if a == 10:
    print("a는 10입니다.")
elif a == 20:
    print("a는 20입니다.")
elif a == 30:
    print("a는 30입니다.")
else :
    print("a는 그외의 숫자입니다.")

# 반복문은 지정한 횟수만큼 코드를 반복시킨다.
i = 1
for i in range(5, 10):
    print("i의 현재값:", i)

# 사용자로부터 숫자 입력받아보기

print("숫자를 입력해보세요.")
a = int(input())
print("사용자가 입력한 값: ", a)

print("*"*a)

#피라미드, 역피라미드 찍어보기
for i in range(1, a+1):
    space_length = a - i
    star_length = 2 * i - 1
    print(" " * space_length , "*" * star_length)

for j in range(1, a+1):
    space_length = j - 1
    star_length = 2 * (a - j + 1) -1
    print(" " * space_length , "*" * star_length)

while a >= 0:
    print(a)
    a -=1
