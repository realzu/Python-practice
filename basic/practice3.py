# 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name='유재석', main_lang='파이썬', age=20)
profile(main_lang='자바', age=25, name='김태호') #키워드가 지정됐으면 순서달라도 ㄱㅊ



# 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print('이름 : {0}\t나이 : {1}\t'.format(name,age), end=' ') #end=' '란 출력이후 줄바꿈없이 한칸만띄어짐
    print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language): # *로 가변인자
    print('이름 : {0}\t나이 : {1}\t'.format(name,age), end=' ') #end=' '란 출력이후 줄바꿈없이 한칸만띄어짐
    for lang in language:
        print(lang, end=' ')
    print() #줄바꿈용

# profile('유재석', 20, 'Python', 'Java', 'C', 'C++', 'C#')
# profile('김태호', 25, 'Kotlin', 'Swift', '', '', '')
profile('유재석', 20, 'Python', 'Java', 'C', 'C++', 'C#', 'JavaScript')
profile('김태호', 25, 'Kotlin', 'Swift')



# 지역변수와 전역변수   -- 지역(함수내에서만) 전역(모든프로그램내에서)
gun = 10

def checkpoint(soldiers): #경계근무
    # gun = 20
    global gun  #전역 공간에 있는 gun 사용   --가급적 권장x(코드관리어렵)
    gun = gun - soldiers    #gun은 함수내변수라서 밖의 gun 인식(x) -> 초기화안됐으니 에러발생 -> 지역변수 초기화해줘야
    print('[함수 내] 남은 총 : {0}'.format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers    #들어온 gun=지역변수
    print('[함수 내] 남은 총 : {0}'.format(gun))
    return gun  #나간 이후론 전역변수

print('전체 총 : {0}'.format(gun))
# checkpoint(2) #2명이 경계근무 나감
gun = checkpoint_ret(gun, 2)
print('남은 총 : {0}'.format(gun))



'''Quiz) 표준 체중 구하는 프로그램
(성별에 따른 표준 체중 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21
조건1 : 표준 체중은 별도의 함수 내에서 계산
    * 함수명 : std_weight
    * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시
'''
def std_weight(height, gender):
    if gender == '남자':
        return height * height * 22
    elif gender == '여자':
        return height * height * 21

height = 175 #cm단위
gender = '남자'
weight = round(std_weight(height / 100, gender), 2) #round(x, 2)★
print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.'.format(height, gender, weight))



# 표준 입출력
print('Python', 'Java', sep=' vs ')   #sep로 구분값 지정
print('Python', 'Java', sep=',', end='?')  #end로 문장 끝부분 값 지정 + 줄바꿈 막음
print('무엇이 더 재밌을까요?')

import sys
print('Python', 'Java', file=sys.stdout)    #표준출력으로 찍힘
print('Python', 'Java', file=sys.stderr)    #표준에러 - 로그처리할때 에러는 확인해서 코드 수정 등 해야

scores = {'수학':0, '영어':50, '코딩':100}  #dictionry
for subject, score in scores.items():   #items는 키,밸류를 쌍으로 튜플로 보내줌
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=':')  #왼쪽정렬(값을 포함한 8칸확보) / 오른쪽정렬

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print('대기번호 : ' + str(num).zfill(3))    #3개만큼의 크기 확보(빈 공간은 0으로 채움)

answer = input('아무 값이나 입력하세요 : ') #사용자입력값은 string타입
print(type(answer))
print('입력하신 값은 ' + answer + '입니다.')



# 다양한 출력포맷

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print('{0: >10}'.format(500))   #' '(빈칸)+값 포함 10자리. >는 오른쪽정렬
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print('{0: >+10}'.format(500))
print('{0: >+10}'.format(-500))
# 왼쪽 정렬하고, 빈칸을 _로 채움
print('{0:_<+10}'.format(500))
# 3자리마다 콤마를 찍어주기
print('{0:,}'.format(1000000000))
# 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
print('{0:+,}'.format(1000000000))
print('{0:+,}'.format(-1000000000))
# 3자리마다 콤마를 찍으며, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기 - 영앤리치앤프리티걸
print('{0:^<+30,}'.format(100000000))
# 소수점 출력
print('{0:f}'.format(5/3))
# 소수점 특정 자리수 까지만 표시 (소수점 3째자리에서 반올림)
print('{0:.2f}'.format(5/3))



# 파일 입출력

score_file = open('score.txt', 'w', encoding='utf-8')   #쓰기 전용
print('수학 : 0', file=score_file)
print('영어 : 50', file=score_file)
score_file.close()

score_file = open('score.txt', 'a', encoding='utf-8')   #'w':이미 파일이 있다면 덮어쓰기라서 'a':누적쓰기
score_file.write('과학 : 80')
score_file.write('\n코딩 : 100')    #write는 줄바꿈기능없어서 \n해줘야
score_file.close()

score_file = open('score.txt', 'r', encoding='utf-8')   #파일읽어옴
print(score_file.read())
score_file.close()

score_file = open('score.txt', 'r', encoding='utf-8')
print(score_file.readline(), end='')    #줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
print(score_file.readline(), end='')  #print는 자체 한줄띔
print(score_file.readline(), end='')
print(score_file.readline(), end='')
score_file.close()

# 파일 내용이 몇줄일지 모를 때
# 방법1)
score_file = open('score.txt', 'r', encoding='utf-8')
while True:
    line = score_file.readline()
    if not line:
        break   #반복문 탈출
    print(line, end='')
score_file.close()
# 방법2)
score_file = open('score.txt', 'r', encoding='utf-8')
lines = score_file.readlines()  #list형태로 저장 (모든 값들을)
for line in lines:
    print(line, end='')
score_file.close()



# pickle
import pickle
profile_file = open('profile.pickle','wb')  #b=binary타입(피클에선 해주기)
profile = {'이름':'박명수', '나이':30, '취미':['축구','골프','코딩']}
print(profile)
pickle.dump(profile, profile_file)  #profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open('profile.pickle','rb')  #읽기전용이니 r+b
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()



# with

import pickle
with open('profile.pickle', 'rb') as profile_file:  #데이터를 as ~ 변수에 저장
    print(pickle.load(profile_file))    #파일내용 읽어옴
    # with문 탈출하면서 자동 close

with open('study.text', 'w', encoding='utf-8') as study_file:
    study_file.write('파이썬을 열심히 공부하고 있어요')

with open('study.text', 'r', encoding='utf-8') as study_file:
    print(study_file.read())



'''Quiz) 매주 1회 작성하는 보고서 파일 만들기 프로그램
1주차부터 50주차까지의 보고서 파일
조건 : 파일명은 '1주차.txt', '2주차.txt',..
'''
for w in range(1,2):
    report_file = open('{0}주차.txt'.format(w),'w',encoding='utf-8')
    print('- {0} 주차 주간보고'.format(w), file=report_file)
    print('부서 : ', file=report_file)
report_file.close()

for w in range(1,4):
    with open(str(w) + '주차.txt', 'w',encoding='utf-8') as report_file:
        report_file.write('- {0} 주차 주간보고 -'.format(w))
        report_file.write('\n부서 :')
        report_file.write('\n이름 :')
        report_file.write('\n업무 요약 :')