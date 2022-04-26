# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

##전달값과 반환값
def deposit(balance, money):   # 입금 함수 생성
    print("입금이 완료되었습니다. 잔액은 {}원입니다.".format(balance+money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {}원입니다".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {} 원입니다.".format(balance))
        return balance
    
balance = 0 
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000) # 출금 안됨
balance = withdraw(balance,500) # 출력 가능

def withdraw_night(balance, money):
    commission = 100 # 수수료 100원
    return commission, balance - money - commission    # 튜플 형식으로 반환

commission, balance = withdraw_night(balance, 500)
print("수수료는 {}원이며, 잔액은 {}원 입니다.".format(commission, balance))  

# >> 함수의 기본값

def profile(name,age, main_lang):
    print("이름 : {0}\t나이: {1}\t주 사용 언어: {2}".format(name,\
        age,main_lang))   # 코딩 시 줄바꿈 할 때 역슬래쉬 사용, \t로 띄어쓰기
    
profile("유재석",20, "python")
profile("김태호",24, "Java")

# 같은 학교, 같은 학년, 같은 반, 같은 수업
def profile(name,age = 17, main_lang= "python"):
    print("이름 : {0}\t나이: {1}\t주 사용 언어: {2}".format(name,\
        age,main_lang))

profile("유재석")

# 키워드 값
def profile(name,age, main_lang):
    print(name, age, main_lang)

profile(name= "유재석",main_lang= "Java",age = 20)

# 순서가 달라도 해당 키 찾아서 value를 넣음.

# 가변 인자
def profile(name, age, *language):
    print("이름: {0}, 나이: {1}.".format(name,age), end=" ")  # end=" " ->줄바꿈 하지않고 이어서 출력
    for lang in language:
        print(lang,end=" ")
    print()

# lang 개수에 따라 출력 되는 개수 변동 가능

profile("유재석", 20, "python","Java","C+","C++")
profile("김태호", 24, "python")

# 지역변수와 전역변수
gun = 10

def checkpoint(soldiers) : # 경계근무
     gun = gun - soldiers
     print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 오류 발생.
print("남은총 : {0}".format(gun))

gun = 10

def checkpoint(soldiers) : # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) 
print("남은총 : {0}".format(gun))

# 가급적이면 지역변수 사용하기, 함수의 parameter로 던져서 사용 (아래)

def checkpoint_return(gun, soldiers):
    gun = gun - soldiers  # 지역 변수, 여기서 계산 이루어져도 외부에서 정의한 gun값 변화 x
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun   # return까지 실행해야 외부의 gun 값 변경됨.

print("전체 총 : {0}".format(gun))
gun = checkpoint_return(gun, 2)
print("남은총 : {0}".format(gun))



# # 퀴즈 6
# 표준 체중을 구하는 프로그램을 작성하시오

# *표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) X 키(m) x 22
# 여자 : 키(m) X 키(m) x 21

# 조건 1: 표준 체중은 별도의 함수 내에서 계산 
#             * 함수명 : std_weight
#             * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender is "남자" :   # is 또는 == 사용
        weight = (height/100) * (height/100) * 22
        weight_round = round(weight,2)
        print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight_round))
    else :
        weight = (height/100) * (height/100) * 21
        weight_round = round(weight,2)
        print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight_round))
    
std_weight(175, "남자")
std_weight(162, "여자")

# 풀이  # 함수를 weight 추출하는데만 사용
def std_weight2(height,gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight2(height/100, gender),2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))