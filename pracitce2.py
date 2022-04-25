# #리스트 : 순서를 가진 객체의 집합

# #지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30
# #list를 사용하여 하나로 묶음
# subway = [10,20,30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# #조세호가 몇번째 칸에 타고 있는가
# print(subway.index("조세호"))
# # 하하 가 다음 칸에서 탔음
# subway.append("하하")  #더하는 것(맨 뒤에)
# print(subway)

# #정형돈을 유재석/조세호 사이에 태우기
# subway.insert(1,"정형돈") #1번 위치에 정형돈 넣기
# print(subway)
# #지하철에 있는 사람 뒤에서 한 명씩 꺼냄
# print(subway.pop())  #누구를 빼는지 보는 것
# print(subway)
# print(subway.pop())  
# print(subway)
# print(subway.pop())  
# print(subway)

# #같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()  #sort가 정렬하는 것
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# #모두 지우기(clear)
# num_list.clear()
# print(num_list)

# # list는 다양한 자료형에 사용 가능
# num_list =[5,2,4,3,1]
# mix_list=["조세호", 20, True]
# print(mix_list)

# # 리스트 확장(두 리스트 합치기) :extend 함수
# num_list.extend(mix_list)   #num_list를 확장
# print(num_list) 

# #사전(중괄호)
# # 키의 중복이 허용되지 않음
# cabinet ={3: "유재석", 100: "김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5])  
# print(cabinet.get(5))
# print(cabinet.get(5,"사용가능")) #값이 없으면 "사용가능" 출력
# print("hi")
# #대괄호 출력 시 오류&프로그램 종료됨  
# #get 함수를 쓰면 프로그램 종료되지 않음

# #in 이용하여 자료 있는지 확인
# print(3 in cabinet) #True

# #정수 아닌 string 도 가능
# cabinet={"A-3":"유재석", "B-100": "김태호"}
# print(cabinet["A-3"])

# #새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# #이미 사용 중인 키라면 value 업데이트됨
# print(cabinet)

# # 나간 손님(del함수)
# del cabinet["A-3"]
# print(cabinet)

# #key 들만 출력
# print(cabinet.keys())
# #value 들만 출력
# print(cabinet.values())
# #key, value 쌍으로 출력
# print(cabinet.items())

# #목욕탕 폐점(clear)
# cabinet.clear()
# print(cabinet)

# #튜플(소괄호)
# # 리스트와 달리 내용 변경이나 추가 안됨
# # 속도가 리스트보다 빠름
# # 변경되지 않는 목록 사용 시 활용 가능

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스") #오류 남

# # 쉽게 변수 선언 가능
# name = "김종국"
# age = "20"
# hobby = "코딩"
# print(name,age,hobby)

# # 위의 변수 선언을 아래 처럼 쉽게 가능
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name,age,hobby)

# # 집합(set)
# # 중복 안됨, 순서 없음
# my_set= {1,2,3,3,3}
# #사전에서는 key 와 value를 썼지만 여기서는 나열만 하면됨.
# print(my_set)

# java={"유재석", "김태호","양세형"}
# python = set(["유재석", "박명수"])  #set 설정 다른 방법

# #교집합(java와 python모두 할 수 있음)
# print(java & python) # & 사용
# print(java.intersection(python)) #intersection

# #합집합
# print(java | python)
# print(java.union(python)) #union : 합집합을 의미

# #차집합(java는 할 줄 알지만 python은 하지 못하는 사람)
# print(java - python)
# print(java.difference(python)) # difference 함수 사용

# # python을 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었어요 
# python.remove("김태호")
# print(java)

# # 자료 구조의 변경
# # 커피숍
# menu = {"커피", "우유", "주스"} # set 로 출력
# print(menu, type(menu))  # 중괄호로 출력
# # 자료의 type은 set이라고 표시됨 

# menu = list(menu)
# print(menu, type(menu)) #list로 변경됨 #대괄호

# menu = tuple(menu)
# print(menu, type(menu)) # 소괄호

# menu = set(menu)
# print(menu, type(menu))  # 중괄호로 출력(set)

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

# from random import *
# from traceback import print_exception
# id = [1,2,3,]
# print(id)
# shuffle(id) # list를 섞기
# print(id)
# print(sample(id,2)) # list에서 무작위로 2개 뽑음

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