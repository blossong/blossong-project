
# # < class >
# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
name = "마린"   # 유닛의 이름
hp = 40     #유닛의 체력
damage = 5   #유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))


# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반모드/ 시즈모드(탱크 고정, 공격력 큼)
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

tank2_name = "탱크2"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))


# attack 함수 정의
def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name,location,damage))


attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
 # 탱크가 하나 더 있다면 ?
attack(tank2_name, "1시", tank2_damage) 

# # 위 내용을 class로 해보기

# 일반 유닛
class Unit :
    def __init__(self, name, hp, damage) :    
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp,self.damage))

# __init__ :python에서 쓰이는 생성자. marine이나 tank와 같은 객체를 만들 때 사용. 
# 객체 : class로부터 만들어지는 것
# marine, tank : unit class의 instance
# 객체를 생성할 떄는 __init__함수에서 self 제외한 갯수만큼 값을 던져줘야함.

marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)
# marine3 = Unit("마린")  # 오류 :  hp, damage 정보 없음


# # < 멤버 변수 >
# self.name, self.hp 와 같은 것
# class 내에서 정의된 변수

# 레이스 : 공중 유닛, 비행기. 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))
# class 외부에서 멤버 변수 사용. wraith1. 까지 입력하면 입력가능한 변수가 나옴(name, damage,hp)

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("뺴앗은 레이스",80,5)
wraith2.clocking = True # clocking 이라는 기술이 개발되었다

if wraith2.clocking == True :
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# # 위처럼 외부에서 멤버변수 사용 가능하지만 위의 clocking 의 경우 wraith2에 대해서만
# 정의 되었으므로 다른 객체(wraith1, marine 등)에 대해서는 적용불가
# 아래의 경우 오류 발생
# if wraith1.clocking == True :
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith1.name))  

# < 메소드 >
# 공격 유닛을 나타내는 class 생성
class AttackUnit :
    def __init__(self, name, hp, damage) :    
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self,location) :            # 공격하는 함수 # class 내에서 self 를 적어줌
        print("{0} : {1} 방향으로 적군을 공격합니다[공격력 {2}]"\
            .format(self.name, location , self.damage))
        
    def damaged(self, damage) :             # 공격 받은 함수
        print("{0} :{1} 데이미즐 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")              
# Class를 통해 생성된 Unit, 그리고 해당 unit에 대해 함께 정의된 함수 사용

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)


# # < 상 속 >
# 부모 클래시, 자식 클래스
# 상속을 이용하여 위와 똑같이 결과 내기

# 메딕 : damage 없음
class Unit :
    def __init__(self, name, hp) :    
        self.name = name
        self.hp = hp

# 공격 유닛을 나타내는 class 생성
class AttackUnit(Unit):             #일반 유닛의 정보 받아옴
    def __init__(self, name, hp, damage) :    
        Unit.__init__(self, name, hp)       # 일반 유닛 정보 받아오기 위해 넣어줌
        self.damage = damage                # 추가되는 것

# # < 메소드 >
# 공격 유닛을 나타내는 class 생성
class AttackUnit :
    def __init__(self, name, hp, damage) :    
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self,location) :            # 공격하는 함수 # class 내에서 self 를 적어줌
        print("{0} : {1} 방향으로 적군을 공격합니다[공격력 {2}]"\
            .format(self.name, location , self.damage))
        
    def damaged(self, damage) :             # 공격 받은 함수
        print("{0} :{1} 데이미즐 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")              
# Class를 통해 생성된 Unit, 그리고 해당 unit에 대해 함께 정의된 함수 사용

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)


# # < 다중 상속 >
# 부모가 둘 이상, 여러 곳에서 상속 받는다.
# 드랍쉽 : 공중 유닛, 수송기. 마린이나 파이어뱃 또는 탱크 등을 수송. 공격 불가

# 날 수 있는 기능을 가진 클래스
class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다 [속도 {2}]"\
            .format(name, location, self.flying_speed))
    

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable) :
    def __init__(self, name, hp, damage, flying_speed) :
        AttackUnit.__init__(self, name, hp, damage)         # 상속 받아와서 초기화
        Flyable.__init__(self, flying_speed)


# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie  = FlyableAttackUnit("발키리", 200,6,5)
valkyrie.fly(valkyrie.name, "3시")
# Flyable 안의 함수 사용
