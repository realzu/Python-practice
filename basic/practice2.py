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
# weather = '맑음'
weather = input('오늘 날씨는 어때요? ')
if weather == '비' or weather == '눈':
    print('우산을 챙기세요') #조건에 맞으면 여기서 빠져나옴
elif weather == '미세먼지':
    print('마스크를 챙기세요')
else:
    print('준비물 필요 없어요')

temp = int(input('기온은 어때요? '))
if 30 <= temp:
    print('너무 더워요. 나가지 마세요')
elif 10 <= temp and temp < 30 :
    print('괜찮은 날씨에요')
elif 0 <= temp < 10:
    print('외투를 챙기세요')
else:
    print('너무 추워요. 나가지 마세요')

print('대기번호 : 1')
print('대기번호 : 2')
print('대기번호 : 3')
print('대기번호 : 4')



# for

# for waiting_no in [0,1,2,3,4]:
# randrange()
# for waiting_no in range(5): # 0~4
for waiting_no in range(1, 6): # 1~5
    print('대기번호 : {0}'.format(waiting_no))

starbucks = ['아이언맨', '토르', '아이엠 그루트']
for customer in starbucks:
    print('{0}, 커피가 준비되었습니다.'.format(customer))



# while
customer = '토르'
index = 5
while index >= 1: #조건만족할때까지
    print('{0}, 커피가 준비되었습니다. {1} 번 남았어요.'.format(customer, index))
    index -= 1
    if index == 0:
        print('커피는 폐기처분되었습니다.')

customer = '아이언맨'
index = 1
while True:
    print('{0}, 커피가 준비되었습니다. 호출 {1} 회'.format(customer, index))
    index += 1
# 터미널에서 ctrl+c 누르면 종료

customer = '토르'
person = 'Unknown'
while person != customer :
    print('{0}, 커피가 준비되었습니다.'.format(customer))
    person = input('이름이 어떻게 되세요? ') #토르가 아닐땐 계속 반복(맞으면 반복문 탈출)



# continue와 break
absent = [2, 5] #결석
no_book = [7] #책을 깜빡했음
for student in range(1, 11): #1~10 출석번호
    if student in absent:
        continue #포함되면 밑문장 실행하지않고 스킵 (다음 반복 진행)
    elif student in no_book:
        print('오늘 수업 여기까지. {0}는 교무실로 따라와'.format(student))
        break #반복문 포함해서 모두 종료
    print('{0}, 책을 읽어봐.'.format(student))

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ['Irom man', 'Thor', 'I am groot']
students = [len(i) for i in students] #i라는 변수는 students라는 리스트안에있는 값 하나씩 가져온것
print(students)

# 학생 이름을 대문자로 변환
students = ['Irom man', 'Thor', 'I am groot']
students = [i.upper() for i in students]
print(students)



''' Quiz) 50명의 승객 중 조건에 맞는 택시 탑승 승객 수 구하는 프로그램
조건1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
'''
from random import *
cnt = 0 #총 탑승승객 수 ★
for persons in range(1, 51):
    min = randrange(5, 51) #5~50 ★
    if 5 <= min <= 15:
        print('[O] {0}번째 손님 (소요시간 : {1}분)'.format(persons, min))
        cnt += 1 #카운트 증가 ★        
    else: #매칭 실패니 카운트 증가x
        print('[ ] {0}번째 손님 (소요시간 : {1}분)'.format(persons, min))

print('총 탑승 승객 : {0} 분'.format(cnt)) #★for문 밖



# 함수
def open_account():
    print('새로운 계좌가 생성되었습니다') #함수는 호출 전까지 실행 안됌

open_account() #함수 호출



# 전달값과 반환값
def deposit(balance, money): #입금
    print('입금이 완료되었습니다. 잔액은 {0} 원 입니다.'.format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money: #잔액이 출금액보다 많으면
        print('출금이 완료되었습니다. 잔액은 {0} 원입니다.'.format(balance - money))
        return balance - money
    else:
        print('출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.'.format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금
    commission = 100 #수수료 100원
    return commission, balance - money - commission #여러 개의 값 반환 가능(튜플 형식)

balance = 0 #잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
# print(balance)
commision, balance = withdraw_night(balance, 500)
print('수수료는 {0}원이며, 잔액은 {1}원입니다.'.format(commision, balance))



# 기본값
def profile(name, age, main_lang):
    print('이름 : {0}\t 나이 : {1}\t주 사용 언어 : {2}' \
        .format(name, age, main_lang)) #줄바꿈시 한칸띄고\후 엔터

profile('유재석', 20, '파이썬')
profile('김태호', 25, '자바')

# 같은 학교/학년/반/수업
def profile(name, age=17, main_lang='파이썬'):
    print('이름 : {0}\t 나이 : {1}\t주 사용 언어 : {2}' \
        .format(name, age, main_lang)) #줄바꿈시 한칸띄고\후 엔터

profile('유재석')
profile('김태호')