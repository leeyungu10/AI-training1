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

import matplotlib.pyplot as mp
import pandas as pd

class Student():
    def __init__(self):
        self.name = ' '
        self.age = 0
        self.kor = []
        self.eng = []
        self.math = []
    # 평균 구하는 2가지
    # 입력 별로 구하는 평균
    # 최신 값을 포함해 한번에 구하는 평균값
    def calcAvg(self):
        index = len(self.kor) - 1
        average = int(self.kor[index] + int(self.eng[index]) + int(self.math[index]))
        return average
    
    def calcTotalAvg(self):
        average = []
        size = len(self.kor)
        for i in range(0, size):
            temp = 0
            temp += int(self.kor[i])
            temp += int(self.eng[i])
            temp += int(self.math[i])
            average.append(temp / 3)
        return average
# 96번줄에 dataframe을 panda가 처리하지 못함 
# 해결하기 위한 함수
def prepare_dataframe(student_array):
    keys = student_array.keys()
    dataframe = {}
    kor_array = []
    eng_array = []
    math_array = []
    average_array = []
    for k in keys:
        v = student_array[k]
        last_index = len(v.kor) - 1
        kor_array.append(int(v.kor[last_index]))
        eng_array.append(int(v.eng[last_index]))   
        math_array.append(int(v.math[last_index]))
        average_array.append(v.calcAvg())
    dataframe['name'] = keys
    dataframe['국어점수'] = kor_array
    dataframe['영어점수'] = eng_array
    dataframe['수학점수'] = math_array
    dataframe['평균 점수'] = average_array
    
    return dataframe


student_array = {}
while True:
    temp = input("1. 입력 2. 출력 3. 종료 \n")
    if(temp == 3):
        break

    if(temp == '1'):
        s = Student()
        s.name = input("이름을 입려해주세요: ")
        s.age = input("나이를 입력해주세요: ")
        kor = int(input("국어 점수: "))
        eng = int(input("영어 점수: "))
        math = int(input("수학 점수: "))

    # 여기서 이미 딕션에 사용자가 존재할 경우
    # student_array는 확실한 class 변수가 아닌 딕셔너리형식이기 때문에, 딕션이 존재하지 않을 경우 append가 실행이 안된다
    # 따라서, class의 append 색과 다르게 array는 변하지 않는다.
        
        if(s.name in student_array.keys()):
            student_array[s.name].kor.append(kor)
            student_array[s.name].eng.append(eng)
            student_array[s.name].math.append(math)
        
        else:
            s.kor.append(kor)
            s.eng.append(eng)
            s.math.append(math)
            student_array[s.name] = s
        
    if(temp == '2'):
        # 사용자가 temp에 a를 넣으면 프로그램 터짐 -> int 말고 숫자를 문자로 치환하는게 좋을 듯
        temp = input("1. 전체 학생 출력 2. 개별 학생 출력 3. 뒤로")

        if(temp == '3'):
            break
        if(temp == '1'):
            dataframe = pd.DataFrame(prepare_dataframe(student_array))
            print(dataframe)

        elif(temp == '2'):
            name = input("이름을 입력해주세요: ")
            if name in student_array.keys():
                length = len(student_array[name].kor)
            x = []
            for i in range(1, length+1):
                x.append(int(i))
            
            mp.plot(x, student_array[name].kor, label = 'korean')
            mp.plot(x, student_array[name].eng, label = 'english')
            mp.plot(x, student_array[name].math, label = 'math')
            mp.plot(x, student_array[name].calcTotalAvg(), label='average')
            mp.legend()
            mp.show()
        
# regular expression?
# 정규표현식이란?
# 내가 요구하는 형식이랑 입력 받는 값의 형식이 일치한지 대조해보는 표현식
# 알아서 한번 봐라!!
# 
            
