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
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
