#리스트 : 순서를 가진 객체의 집합

#지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30
#list를 사용하여 하나로 묶음
subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호가 몇번째 칸에 타고 있는가
print(subway.index("조세호"))
# 하하 가 다음 칸에서 탔음
subway.append("하하")  #더하는 것(맨 뒤에)
print(subway)

#정형돈을 유재석/조세호 사이에 태우기
subway.insert(1,"정형돈") #1번 위치에 정형돈 넣기
print(subway)
#지하철에 있는 사람 뒤에서 한 명씩 꺼냄
print(subway.pop())  #누구를 빼는지 보는 것
print(subway)
print(subway.pop())  
print(subway)
print(subway.pop())  
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()  #sort가 정렬하는 것
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두 지우기(clear)
num_list.clear()
print(num_list)

# list는 다양한 자료형에 사용 가능
num_list =[5,2,4,3,1]
mix_list=["조세호", 20, True]
print(mix_list)

# 리스트 확장(두 리스트 합치기) :extend 함수
num_list.extend(mix_list)   #num_list를 확장
print(num_list) 

#사전(중괄호)
# 키의 중복이 허용되지 않음
cabinet ={3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5])  
print(cabinet.get(5))
print(cabinet.get(5,"사용가능")) #값이 없으면 "사용가능" 출력
print("hi")
#대괄호 출력 시 오류&프로그램 종료됨  
#get 함수를 쓰면 프로그램 종료되지 않음

#in 이용하여 자료 있는지 확인
print(3 in cabinet) #True

#정수 아닌 string 도 가능
cabinet={"A-3":"유재석", "B-100": "김태호"}
print(cabinet["A-3"])

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
#이미 사용 중인 키라면 value 업데이트됨
print(cabinet)

# 나간 손님(del함수)
del cabinet["A-3"]
print(cabinet)

#key 들만 출력
print(cabinet.keys())
#value 들만 출력
print(cabinet.values())
#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점(clear)
cabinet.clear()
print(cabinet)

#튜플(소괄호)
# 리스트와 달리 내용 변경이나 추가 안됨
# 속도가 리스트보다 빠름
# 변경되지 않는 목록 사용 시 활용 가능

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") #오류 남

# 쉽게 변수 선언 가능
name = "김종국"
age = "20"
hobby = "코딩"
print(name,age,hobby)

# 위의 변수 선언을 아래 처럼 쉽게 가능
(name, age, hobby) = ("김종국", 20, "코딩")
print(name,age,hobby)

# 집합(set)
# 중복 안됨, 순서 없음
my_set= {1,2,3,3,3}
#사전에서는 key 와 value를 썼지만 여기서는 나열만 하면됨.
print(my_set)

java={"유재석", "김태호","양세형"}
python = set(["유재석", "박명수"])  #set 설정 다른 방법

#교집합(java와 python모두 할 수 있음)
print(java & python) # & 사용
print(java.intersection(python)) #intersection

#합집합
print(java | python)
print(java.union(python)) #union : 합집합을 의미

#차집합(java는 할 줄 알지만 python은 하지 못하는 사람)
print(java - python)
print(java.difference(python)) # difference 함수 사용

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었어요 
python.remove("김태호")
print(java)

# 자료 구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"} # set 로 출력
print(menu, type(menu))  # 중괄호로 출력
# 자료의 type은 set이라고 표시됨 

menu = list(menu)
print(menu, type(menu)) #list로 변경됨 #대괄호

menu = tuple(menu)
print(menu, type(menu)) # 소괄호

menu = set(menu)
print(menu, type(menu))  # 중괄호로 출력(set)

# 퀴즈 #4
# 이벤트 진행. 댓글 작성자 중 추첨을 통해 1명은 치킨, 3명은 커피쿠폰
# 추첨 프로그램을 작성하시오.

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈과 shuffle 과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다--

from random import *
from traceback import print_exception
id = [1,2,3,]
print(id)
shuffle(id) # list를 섞기
print(id)
print(sample(id,2)) # list에서 무작위로 2개 뽑음

# [solution]
from random import *
users = range(1,21)  # 1부터 20까지 숫자 생성
# print(type(users)) # type이 range로 출력됨
users = list(users) # type을 list로 변경
# print(type(users))

# 중복없이 4명을 뽑는다.
# 뽑기 전에 shuffle
shuffle(users)
winners = sample(users,4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다--")

# >>>if문(분기?)

#weather = "맑음"
weather = input("오늘 날씨는 어때요?")  
 # input은 사용자가 입력하는 곳
 # terminal에 물음표 다음에 cursor가 답을 기다리고 있음
 # cursor 위치에 비, 미세먼지 등을 입력하면 아래의 조건문에 따라 출력됨
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:  #나머지 모든 경우
    print("준비물이 필요 없어요.")

temp = int(input("기온은 어때요?"))  # 기온은 숫자이므로 int함수 사용하여 변환
if 30 <= temp :
    print("너무 더워요")
elif 10 <= temp and temp <30 :
    print("괜찮은 날씨에요")
elif 0 <= temp <10:
    print("외투를 챙기세요")
else :
    print("너무 추워요. 나가지 마세요")

# 반복문
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")
#여러 번 찍을 때 필요한 게 For 문

for waiting_no in [0,1,2,3,4] :
    print("대기번호 : {0}".format(waiting_no)) # 차례대로 들어가고 for문 끝남
for waiting_no in range(5) : #0,1,2,3,4
    print("대기번호 : {0}".format(waiting_no))
for waiting_no in range(1,6) : #1,2,3,4,5
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))


# while 문
# rule: 5번 손님 불렀는데 나타나지 않으면 버리는 정책
customer = "토르"
index = 5
while index >=1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer, index))
    index -= 1 # index = index-1
    if index == 0 :
        print("커피는 폐기처분되었습니다")
    # index = 0 이 되면서 while문 빠져나옴

# 손님이 올 때까지 계속 호출한다면,
customer = "아이언맨"
index = 1
while True :
    print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index))
    index +=1  ##무한루프 발생함. terminal에서 Ctrl +C  눌러서 강제종료

# 손님이 찾아와서 물어서
customer = "토르"   # 음료가 준비된 사람
person = "Unknown"  # 찾아온 사람, while문에 들어갈 변수들은 일단 정의해야함. 임의 지정 가능

while person != customer :  # 찾아온 사람이 customer과 일치하지 않으면 while 문 실행
    print ("{0}, 커피가 준비되었습니다".format(customer))
    person = input("이름이 어떻게 되세요?")

# while~print 작성 후, 뒤에 아무런 조건이 없으면 while문 무한 루프. 꼭 빠져나오는 조건 붙이기

# >>continue와 break
absent = [2,5]
no_book = [7]
for student in range(1,11): 
    if student in absent:
        continue        # continue : student 가 absent 에 있으면 실행하지 않고 다음 진행
    elif student in no_book:
        print("오늘 수업은 여기까지. {0}는 교무실로 따라와".format(student))
        break       # break는 더이상 진행하지 않고 while문을 끝냄
    print("{0}. 책을 읽어봐".format(student))

# >> 한줄 For
# 출석번호 1,2,3,4 -> 앞에 100을 붙이기로 함 -> 101,102,103...
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

# 학생 이름을 문자길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i  in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]    # upper() 로 써야함!
print(students)

# # 퀴즈 5
# 당신은 택시기사. 50명의 승객과 매칭 기회가 있을 떄, 총 탑승승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분~ 50분 사이의 난수(random)로 정해진다.
# 조건2 : 당신은 소요시간 5분 ~ 15분의 승객만 매칭해야 한다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 10분)
# [ ] 4번째 손님 (소요시간 : 17분)
# ...
# [O] 50번째 손님 (소요시간 : 13분)

# 총 탑승 승객 : 3 분


# 풀이
from random import *
cnt = 0                     #초기값을 아는 것은 처음에 정의
for i in range(1,51):
    time  = randrange(5,51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님(소요시간 : {1}분)".format(i,time))
        cnt+=1
    else:
        print("[ ] {0}번째 손님(소요시간 : {1}분)".format(i,time))

print("총 탑승 승객 : {} 분".format(cnt))


# 이렇게는 왜 안되는지?
from random import *
customer = 0
time = range(5,51)
working_time = "unknown"

while customer <51:
    print("[{0}] {1}번째 손님(소요시간 : {2}분)".format("O", customer, working_time))
    customer += 1
    working_time = sample(time,1)
    # if int(working_time) < 5 :
    #     print("[{0}] {1}번째 손님(소요시간 : {2}분".format(" ", customer, working_time))