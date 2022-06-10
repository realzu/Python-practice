# Class 클래스
# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음 (스타크래프트의 캐릭터를 비유해 설명할 것)
name = '마린'   #유닛의 이름
hp = 40 #유닛의 체력
damage = 5  #유닛의 공격력

print('{0} 유닛이 생성되었습니다.'.format(name))
print('체력 {0}, 공격력 {1}\n'.format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드가 / 시즈 모드
tank_name = '탱크'
tank_hp = 150
tank_damage = 35

print('{0} 유닛이 생성되었습니다.'.format(tank_name))
print('체력 {0}, 공격력 {1}\n'.format(tank_hp, tank_damage))

def attack(name, location, damage):
    print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(name, location, damage))

attack(name, '1시', damage)
attack(tank_name, '1시', tank_damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{0} 유닛이 생성되었습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

marine1 = Unit('마린', 40, 5)   #self제외하고 매개변수 그대로넘겨야
marine2 = Unit('마린', 40, 5)
tank = Unit('탱크', 150, 35)



# __init__ : 생성자 (마린,탱크와 같은 객체(클래스로 부터 만들어짐. Unit클래스의 인스턴스)가 만들어질때 자동으로 생성)
# 멤버 변수 : 클래스 내에서 정의된 변수

# 레이스 : 공중 유닛, 비행기. 클로킹(상대방에게 보이지 않음)
wraith1 = Unit('레이스', 80, 5)
print('유닛 이름 : {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damage)) #외부에서 멤버 변수

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit('레이스', 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print('{0}는 현재 클로킹 상태입니다.'.format(wraith2.name))