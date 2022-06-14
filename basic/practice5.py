# 10강 예외처리 -- 에러 발생시 에러 처리
try:
    print('나누기 전용 계산기입니다.')
    # num1 = int(input('첫 번째 숫자를 입력하세요 : ')) #정수형 int
    # num2 = int(input('두 번째 숫자를 입력하세요 : '))
    # print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))
    nums = []
    nums.append(int(input('첫 번째 숫자를 입력하세요 : ')))
    nums.append(int(input('두 번째 숫자를 입력하세요 : ')))
    # nums.append(int(nums[0] / nums[1]))
    print('{0} / {1} = {2}'.format(nums[0], nums[1], nums[2]))
except ValueError:
    print('에러! 잘못된 값을 입력하였습니다.')
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print('알 수 없는 에러가 발생하였습니다.')
    print(err)



# 에러 발생시키기
try:
    print('한 자리 숫자 나누기 전용 계산기')
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print('{0} / {1} = {2}'.format(num1, num2, int(num1 / num2)))
except ValueError:
    print('잘못된 값을 입력했습니다. 한 자리 숫자만 입력하세요.')


# 사용자 정의 예외처리 + # finally
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print('한 자리 숫자 나누기 전용 계산기')
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError('입력값 : {0}, {1}'.format(num1, num2))
    print('{0} / {1} = {2}'.format(num1, num2, int(num1 / num2)))
except ValueError:
    print('잘못된 값을 입력했습니다. 한 자리 숫자만 입력하세요.')
except BigNumberError as err:
    print('에러가 발생하였습니다. 한 자리 숫자만 입력하세요.')
    print(err)
finally:    #에러가 나도 무조건 실행
    print('계산기를 이용해 주셔서 감사합니다.')



# 10-5 Quiz)
class SoldOutError(Exception):  #★Exception 상속해야!
    pass

chicken = 10
waiting = 1
while(True):
    try:
        print('[남은 치킨 : {0}]'.format(chicken))
        order = int(input('치킨 몇 마리 주문하시겠습니까?'))
        if order > chicken:
            print('재료가 부족합니다.')
        elif order <= 0:    # ★
            raise ValueError
        else:
            print('[대기번호 : {0}] {1} 마리 주문이 완료되었습니다.'.format(waiting, order))
            waiting += 1
            chicken -= order
            
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print('잘못된 값을 입력하였습니다.')
    except SoldOutError:
        print('재고가 소진되어 더 이상 주문을 받지 않습니다.')
        break   # ★



# 모듈 (필요한 것끼리 부품처럼 만들어진 파일)
# 같은 폴더안에 있어야 사용 가능
import theater_module
theater_module.price(3) #3명이 영화보러 갔을 때
theater_module.price_morning(4) #4명 조조 할인 영화보러 갔을 때
theater_module.price_soldier(5) #5명 군인이 영화보러 갔을 때

import theater_module as mv #별명
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
# from random import *  --모듈의 모든걸사용하겠다
price(3)
price_morning(4)
price_soldier(5)

from basic.theater_module import price_soldier
from theater_module import price, price_morning #특정함수만 가져오도록 명시 가능
price(5)
price_morning(6)
# price_soldier(7) --x

from theater_module import price_soldier as price
price(5)



# 패키지 --모듈들을 모아놓은 집합
import travel.thailand  #모듈or패키지만 가능 (클래스, 함수는 바로 불가)
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage #import를 통해선 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()



# __all__ -- __init__파일에 __all__에 사용할 패키지써줌으로써 해당 파일 사용가능
# from random import *
from travel import *
# trip_to = vietnam.VietnamPackage()  
trip_to = thailand.ThailandPackage()
trip_to.detail()



# 모듈 직접 실행
# __name__ == "__main__" (thailand.py 확인)



# 패키지, 모듈 확인
import inspect
import random
print(inspect.getfile(random))  #랜덤 모듈의 파일 위치 확인
print(inspect.getfile(thailand))



# pip install   --패지키 설치 방법
# https://pypi.org/
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
# pip list  --설치된 패지키 리스트
# pip show 패지키명 --패지키정보
# pip install --upgrade 패키지명    --가장 최신의 패지키 버전으로 업그레이드
# pip uninstall 패키지명    --패키지 삭제



# 내장함수  --이미 내장되어 import필요없이 바로 사용가능한 함수
# input : 사용자 입력을 받는 함수
language = input('무슨 언어를 좋아하세요?')
print('{0}은 아주 좋은 언어입니다!'.format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장 함수
print(dir())
import pickle
print(dir())

print(dir(random))  #랜덤모듈에서 쓸수있는것들
lst = [1, 2, 3]
print(dir(lst))

name = 'Jin'
print(dir(name))
# list of python builtins
# https://docs.python.org/3/library/functions.html



# 외장함수
# https://docs.python.org/3/py-modindex.html
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py"))    #확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())  #현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):
    print('이미 존재하는 폴더입니다.')
    os.rmdir(folder)
    print(folder, '폴더를 삭제하였습니다.')
else:
    os.makedirs(folder) #폴더 생성
    print(folder, '폴더를 생성하였습니다.')

print(os.listdir())

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime
# print('오늘 날짜는 ', datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()   #오늘 날짜 저장
td = datetime.timedelta(days=100)   #100일 저장
print('우리가 만난지 100일은', today + td)  #오늘부터 100일 후


# Quiz
# byme.py 추가
import byme
byme.sign()