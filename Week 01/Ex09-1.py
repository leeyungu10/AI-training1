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

class Student():
    def __init__(self):
        self.name = " "
        self.age = 0
        self.kor = []
        self.eng = []
        self.math = []
student_array= {}
i = 0
# 나중에 뒤로 기능을 위해 첫번째 반복문은 계속 돌림
while True:
    i = input("1. 입력 2. 출력 3. 종료\n")
    if i == '3':
        break

    elif i == '1':
        s = Student()
        s.name = input("이름: ")
        s.age = input("나이: ")
        kor = int(input("국어: "))
        eng = int(input("영어: "))
        math = int(input("수학: "))

# 딕션안에 중복인지 확인
        # 중복이라면,
        if s.name in student_array:
            student_array[s.name].kor.append(kor)
            student_array[s.name].eng.append(eng)
            student_array[s.name].math.append(math)
        
        else:
            s.kor.append(kor)
            s.eng.append(eng)
            s.math.append(math)
            student_array[s.name] = s


        
