import random
# String
# String은 여러개의 문자가 모여있는 집합이다.

#String을 저장할 때에는 저장할 값을 '' 나 ""로 감싸주면 된다.

a = 'abcde'
b = "fghij"
print(a)
print(b)

# 여러개의 문자가 모여있는 것이기 때문에
# 우리가 특정 자리에 저장된 값을 불러올 수 있다.
# 단, 컴퓨터는 몇번째인지를 셀 때 인간과는 다르게 0부터 세므로
# 이점을 주의해야 한다.
print(a[3])
print(b[4])
# print(b[5]) ==> 존재하지 않는 인덱스의 접근으로 에러

#문자열이 몇글자인지 알아볼때에는
print(len(a))

# a[3] = 'c' --> String은 특정 자리에 글자를 바꾸는 것은 안된다.

# find는 특정 문자열의 시작 지점을 찾아준다.
# 단, 해당 무낮여링 없으면 -1이 나온다.
print(a.find('c'))
print(a.find('z'))

# String은 다른 String과 더하여 새로운 문자열을 만들 수 있다.
a += b
print(a)

# String은 특정 횟수만큼 반복시킬 때 *를 쓴다.
a *= 4
print(a)

# 특정 인덱스로부터 특정 인덱스를 뽑아낼 때에는?
c = a[3:10]
print(c)

# 함수의 경우, 그 안에서 무언가 출력을 해도 되지만
# 아무런 출력 없이 계산된 값을 돌려주는 역할을 할 수도 있다.

def makeStar(star_length):
    temp = "*" * int(star_length)
    return temp

c = makeStar(10)
print(c)

a = 10

# List
# 리스트는 같은 자료형이 여러개 모여있는 것을 리스트라고 한다.
cars = ["소나타", "그랜저", "제네시스", "포르쉐"]
print(cars)


for a in cars:
    print(a)
# 현재 리스트에 있는 요소들의 갯수
print(len(cars))

# str과 다르게 리스트는 특정 인덱스에 저장된 값을 다른 것으로 바꿀 수 있다.
cars[0] ="모닝"
print(cars[0])

# 리스트에 가장 마지막에 새로운 것을 추가할 수도 있다.
cars.append("페파리")
print(cars)

# 리스트에 특정 인덱스에 새로운 것을 끼어넣을 수 있다.
cars.insert(1, "소나타")
print(cars)

# 특정 인덱스에 저장된 요소를 빼낼때에는 pop이라는 것을 쓰는데
# 빼낸 요소는 사라지는 것이 아니라 return되는 형식이므로
# 다른 변수에 저장할 수 있다.   

temp = cars.pop(4)
print(cars)
print(temp)

# sort, reverse를 사용할 수 있다.
cars.sort() #오름차순 정렬
print(cars) 

cars.reverse() #내림차순 정렬
print(cars)

#index는 특정 요소의 인덱스 값을 찾는다.
# 단, 존재하지 않는 요소의 경우, 에러가 발생된다.
print(cars.index("소나타"))

# 특정 요소가 몇 개 등장하는지 셀 때에는
# 카운트를 사용한다.
print(cars.count("페라리"))

