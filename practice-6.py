# # < 메소드 오버라이딩 > - 앞에서 사용한 예시 사용
class Unit :
    def __init__(self, name, hp, speed) :    
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛을 나타내는 class 생성
class AttackUnit(Unit):             #일반 유닛의 정보 받아옴
    def __init__(self, name, hp,speed, damage) :    
        Unit.__init__(self, name, hp,speed)       # 일반 유닛 정보 받아오기 위해 넣어줌
        self.damage = damage                # 추가되는 것

# 아래의 AttackUnit 생성 방법을 위와 같이 Unit.__init__(self, name,hp,speed)로 간략하게 만들 수 있다.
        
# # 공격 유닛을 나타내는 class 생성
# class AttackUnit(Unit) :
#     def __init__(self, name, hp, speed, damage) :    
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         self.damage = damage

#     def attack(self,location) :                                 # 공격하는 함수 # class 내에서 self 변수 활용을 위해 self 를 적어줌
#         print("{0} : {1} 방향으로 적군을 공격합니다[공격력 {2}]"\
#             .format(self.name, location , self.damage))
        
#     def damaged(self, damage) :                                    # 공격 받은 함수
#         print("{0} :{1} 데미지를 입었습니다.".format(self.name, damage))           # 공격을 받으면 좌측 내용을 print 하고 
#         self.hp -= damage                                                        # self.hp = self.hp-damage 로 self.hp가 새로 정의
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))          # 새로운 self.hp 값을 가지고 좌측 내용 print
#         if self.hp <=0:                                                           # 새로 받은 self.hp 가 0보다 작거나 같으면 아래를 print
#             print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50,0,16)
# firebat1.attack("5시")              
# Class를 통해 생성된 Unit, 그리고 해당 unit에 대해 함께 정의된 함수 사용

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


# # < 다중 상속 >
# 부모가 둘 이상, 여러 곳에서 상속 받는다.
# 드랍쉽 : 공중 유닛, 수송기. 마린이나 파이어뱃 또는 탱크 등을 수송. 공격 불가

# 날 수 있는 기능을 가진 클래스
class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed            # 아래의 메소드를 정의하기 위해 self.flying_speed 정의

    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다 [속도 {2}]"\
            .format(name, location, self.flying_speed))
    

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable) :
    def __init__(self, name, hp, damage, flying_speed) :
        AttackUnit.__init__(self, name, hp,0, damage)         # 지상 speed 는 0으로 처리
        Flyable.__init__(self, flying_speed)
    
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name,location)            # 공중 유닛이면 fly 함수 적용되도록 함.



# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10,20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name,"9시")
# 지상 유닛은 move, 공중 유닛은 fly 써야함. 매번 유닛이 지상인지 공중인지 판단해야함

# # 지상 유닛 , 공중 유닛에 따라 처리될 수 있도록 하기
  # 공중 유닛이면 fly 함수 적용되도록 함.
battlecruiser.move("9시")
