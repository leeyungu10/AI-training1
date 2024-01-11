# 학생 성적 관리 프로그램
# 1. 입력 2. 출력 3. 종료
# >1
# 이름: ###
# 나이: ###
# 국어: ###
# 영어: ###
# 수학: ###
# 1. 입력 2. 출력 3. 종료
# >2
# # 1. 전체 학생 출력 2. 개별 학생 출력 3. 뒤로
# >1
# 전체 학생의 이름 나이 국어 영어 수학 평균이 표로 출력
# 단 이때에는 최신 정보를 기반으로 출력
# 1. 전체 학생 출력 2. 개별 학생 출력 3. 종료
# >2
# 출력할 학생의 이름을 입력해주세요
# 김철수
# 국어, 영어, 수학 점수가 그래프로 출력
# 1. 전체 학생 출력 2. 개별 학생 출력 3. 뒤로
# > 3
# 1. 입력 2. 출력 3. 종료
# > 3
# 사용해주셔서 감사합니다.
# 유의점: 똑같은 이름이면 무조건 동일 학생으로 판단
# 그래프 출력시 처음에는 평균 점수가 토대로 되고
# 심화 문제를 풀고 싶다면 한 그래프에 국영수 평균이 모두 나오는
# 그래프의 형태로 만든다.
import statistics
import matplotlib.pyplot as mp
import numpy as np

x = []
y1 = []
y2 = []
y3 = []
hangul_l = []
math_l = []
english_l = []

class Infor:
    def __init__(self, name = " ", age = 0, hangul= 0, english = 0, math = 0):
        self.name = name
        self.age = age
        self.hangul = hangul
        self.english = english
        self.math = math

    def user_print(self):
        print(self.name, self.age, self.hangul, self.english, self.math)

    def user_show(self):
        for i in range(0, 101):
            x.append(i)
            #y1.append(int(statistics.mean(self.hangul)))
            #y2.append(int(statistics.mean(self.english)))
            #y3.append(int(statistics.mean(self.math))))
        arr_x = np.array(x)
        arr_y1 = np.array(math_l)
        arr_y2 = np.array(english_l)
        arr_y3 = np.array(hangul_l)
        mp.plot(arr_x, arr_y1)
        mp.plot(arr_x, arr_y2)
        mp.plot(arr_x, arr_y3)
        mp.show()
a1 = " "
students = [Infor()]
c = 0
f1 = 0
count = 0
while f1 != 3:
    f1 = int(input("1. 입력 2. 출력 3.종료\n"))
    if f1 == 1:
            name1 = str(input("이름: "))
            age1 = input("나이: ")
            hangul = input("국어: ")
            english = input("영어: ")
            math = input("수학: ")
            a1 = Infor(name1, age1, hangul, english, math)
            students.append(a1)
            print(students[count])
            count += 1
    a1.user_print()
        

    if f1 == 2:     
        print_manual = int(input("1. 전체 학생 출력 2. 개별 학생 출력 3. 뒤로\n"))
        #if print_manual == 1:

        if print_manual == 2:
            print_name = str(input("출력할 학생의 이름을 입력해주세요: "))
            a1.user_show()
            # print_name.user_show()

print("사용해주셔서 감사합니다.")        