# super (추가 파일)
class Unit:
    def __init__(self):
        print('Unit 생성자')

class Flyable:
    def __init__(self):
        print('Flyable 생성자')

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()  #2개이상의 부모클래스 다중상속시 super() 사용하면,  맨처음의 클래스만 init 호출
        Unit.__init__(super)
        Flyable.__init__(super) #각각 부모클래스 해줘야함

# 드랍쉽 (수송만 가능한 유닛. 공격x)
dropship = FlyableUnit()