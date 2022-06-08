# 숫자형 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))



# 문자형 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋ")
print("ㅋ"*9)



# boolean 자료형 - 참/거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))



# 변수
# 애완동물을 소개해주세요
animal = '고양이'
name = '듀듀'
age = 4
hobby = '낮잠'
is_adult = age >= 3

'''이렇게
하면
여러문장이
주석처리
됩니다'''

print('우리집 ' + animal + '의 이름은 ' + name + '예요')
hobby = '공놀이'
# print(name + '는 ' + str(age) + '살이며 ' + hobby + '을 좋아해요') #정수형 출력시 str로 감싸줘야
print(name, '는 ', age, '살이며 ', hobby, '을 좋아해요') #빈칸 추가됌
print(name + '는 어른일까요? ' + str(is_adult)) #마찬가지

'''  Quiz) 변수를 이용하여 다음 문장을 출력하시오
변수명 : station
변수값 : '사당','신도림','인천공항' 순서대로 입력
출력문장 : xx 행 열차가 들어오고 있습니다. '''
station = '사당'
print(station + '행 열차가 들어오고 있습니다.')

station = '신도림'
print(station + '행 열차가 들어오고 있습니다.')

station = '인천공항'
print(station + '행 열차가 들어오고 있습니다.')



# 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) #2^3
print(5%3) #나머지
print(5//3) #몫

print(3 > 10)
print(4 <= 7)

print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)

print(1 != 3)
print(not(1 != 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))

print(5 > 4 > 3)
print(5 > 4 > 7)



# 간단한 수식
print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %= 5
print(number)



# 숫자처리함수
print(abs(-5)) #절댓값
print(pow(4, 2)) #4^2
print(max(5, 12))
print(min(5, 12))
print(round(3.14)) #반올림
print(round(4.99))

from math import * #math라이브러리 안의 모든것 이용
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근



# 랜덤함수
from random import *

print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) #0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) #0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10 이하의 임의의 값 생성

print(int(random() * 45) + 1) #1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46)) 
print(randint(1, 45))

'''Quiz) 코딩스터디 모임 날짜 정해주는 프로그램
월 4회 스터디 中 3번은 온라인 1번은 오프라인으로 진행
아래의 조건에 맞는 오프라인 모임 날짜 정하기
조건1 : 랜덤으로 날짜 뽑기
조건2 : 월별 날짜가 다르므로 최소 일수인 28일 이내
조건3 : 매월 1~3일은 스터디 준비를 위해 제외
'''
from random import *
day = randint(4, 28)
print('오프라인 스터디 모임 날짜는 매월 ' + str(day) + '일로 선정되었습니다.')



# 문자열
sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)



# 슬라이싱
jumin = '980501-1234567'

print('성별: ' + jumin[7])
print("연 : " + jumin[0:2]) #실제자리수-1까지 (= 0부터 2직전까지 = 0,1)
print('월 : ' + jumin[2:4])
print('일 : ' + jumin[4:6])

print('생년월일 : ' + jumin[:6]) #처음부터 6 직전까지
print('뒤 7자리 : ' + jumin[7:])
print('뒤 7자리 (뒤부터) : ' + jumin[-7:]) #맨 뒤 기준으로 7번째부터 끝까지 (맨뒤 인덱스는 -1)



# 문자열 처리 함수
python = 'Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python)) #문자길이 반환
print(python.replace('Python', 'Java')) #특정문자열 변환

index = python.index('n') #특정문자열 인덱스번호 확인 ♥
print(index)
index = python.index('n', index + 1) #두번째 n
print(index)

print(python.find('n'))
print(python.find('Java')) #찾는값없으면 -1 반환
# print(python.index('Java')) #찾는값없으면 에러
print('hi')

print(python.count('n')) #n이 총 몇개 ♥



# 문자열 포맷
print('a' + 'b')
print('a', 'b')

# 방법 1 --%
print('나는 %d살입니다.' % 20) #d는 정수
print('나는 %s을 좋아해요.' % '파이썬') #s는 문자열
print('Apple은 %c로 시작해요.' % 'A') #c는 charter(1글자)
# %s
print('나는 %s살입니다.' % 20) #s는 정수/하나의문자 모두 출력가능
print('나는 %s색과 %s색을 좋아해요' % ('파란', '빨간'))

# 방법 2 --format
print('나는 {}살입니다'.format(20))
print('나는 {}색과 {}색을 좋아해요'.format('파란', '빨간'))
print('나는 {0}색과 {1}색을 좋아해요'.format('파란', '빨간'))
print('나는 {1}색과 {0}색을 좋아해요'.format('파란', '빨간'))

# 방법 3 --변수
print('나는 {age}살이며, {color}색을 좋아해요'.format(age = 20, color = '빨간'))
print('나는 {age}살이며, {color}색을 좋아해요'.format(color = '빨간', age = 20))

# 방법 4 (v3.6 이상~) --f
age = 20
color = '보라'
print(f'나는 {age}살이며, {color}색을 좋아해요')



# 탈출 문자
# \n : 줄바꿈
print('백문이 불여일견 \n백견이 불여일타')

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩"입니다
print("저는 '나도코딩'입니다")
print('저는 "나도코딩"입니다')
print("저는 \"나도코딩\"입니다")
print("저는 \'나도코딩\'입니다")

# \\ : 문장 내에서 하나의 \
print("c:\\Users\\jinhh\\Desktop\\PythonWorkspace")

# \r : 커서를 맨 앞으로 이동
print('Red Apple\rPine') #\r이 다시 맨앞으로가서 거기서부터 워드작성

# \b : 백스페이스 (한 글자 삭제)
print('Redd\bApple')

# \t : 탭
print('Red\tApple')



'''Quiz) 사이트별 비밀번호 생성 프로그램 ★
예) http://naver.com
규칙1) http:// 부분 제외
규칙2) 처음 만나는 점(.) 이후 제외
규칙3) 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
'''

url = 'http://google.com'
my_str = url.replace('http://','') #빈칸으로 바꿈
my_str = my_str[:my_str.index('.')] #.의 인덱스번호 찾음
pwd = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
print("{0} 의 비밀번호는 {1} 입니다".format(url, pwd))



