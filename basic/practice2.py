# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway = ['유재석', '조세호', '박명수']
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index('조세호'))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append('하하')
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, '정형돈')
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append('유재석')
print(subway)
print(subway.count('유재석'))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort() #순서대로 정렬
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = ['조세호', 20, True]
# print(mix_list)

# 리스트 확장 --하나의 list로 합침
num_list.extend(mix_list)
print(num_list)



# 사전
cabinet = {3:'유재석', 100:'김태호'} #key:value
print(cabinet[3]) #[key]
print(cabinet.get(100))

# print(cabinet[5]) #5라는 key없어서 에러
print(cabinet.get(5)) #none 반환
print(cabinet.get(5, '사용 가능')) #문자 반환
print('hi')

print(3 in cabinet) #True
print(5 in cabinet) #False

# String도 가능 
cabinet = {'A-3':'유재석', 'B-100':'김태호'}
print(cabinet['A-3'])
print(cabinet['B-100'])

# 새 손님
print(cabinet)
cabinet['A-3'] = '이태민'
cabinet["C-20"] = '조세호' #추가 (기존값이 있다면 update)
print(cabinet)

# 간 손님
del cabinet['A-3']
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)



# 튜플
menu = ('돈까스', '치즈까스')
print(menu[0])
print(menu[1])
    # 값 추가는 불가 - ex) menu.add('생선까스) (X)

name = '이태민'
age = 20
hobby = '코딩'
print(name, age, hobby)

(name, age, hobby) = ('이태민', 20, '코딩')
print(name, age, hobby)



# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {'유재석','김태호','양세형'}
python = set(['유재석','박명수'])

# # 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# # 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# # 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
python.add('김태호')
print(python)

# # java 를 잊었어요
java.remove('김태호')
print(java)



# 자료구조의 변경
menu = {'커피','우유','주스'}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))



'''Quiz) 댓글 이벤트 추첨 프로그램
1명은 치킨, 3명은 커피 쿠폰
조건1: 댓글은 20명 작성, 아이디는 1~20으로 가정
조건2: 댓글 내용과 상관없이 무작위 추첨하되 중복 불가
조건3: random 모듈과 shuffle, sample 활용
'''
from random import *
users = range(1, 21) #1부터 20까지 숫자를 생성
print(type(users))
users = list(users)
print(type(users))
print(users)

shuffle(users)
print(users)

winners = sample(users, 4) #4명 뽑음

print('-- 당첨자 발표 --')
print('치킨 당첨자 : {0}'.format(winners[0]))
print('커피 당첨자 : {0}'.format(winners[1:]) )
print('-- 축하합니다 --')



# if
weather = '맑음'
if weather == '비':
    print('우산을 챙기세요') #조건에 맞으면 여기서 빠져나옴
elif weather == '미세먼지':
    print('마스크를 챙기세요')
else:
    print('준비물 필요 없어요')