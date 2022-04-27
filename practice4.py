# # 표준 입출력
# print("python", "Java", sep =",")     # separation이 콤마로 됨
# print("python", "Java", sep =",", end ="?")   # 문장의 끝부분이 (줄바꿈) -> ? 로 바뀌면서 아래 문장이 연달아 출력
# print("무엇이 더 재밌을까요?")

# import sys   #sys 모듈 import
# print("python", "Java", file= sys.stdout)
# print("python", "Java", file= sys.stderr)  
# # Visual studio에서는 출력 차이 없지만 실제로는 stdout 은 표준출력으로 나오고 stderr은 에러로 나옴
# # stderr는 따로 logging해서 따로 확인하는 일을 함.

# scores = {"수학":0,"영어":50, "코딩":100}
# for subject, score in scores.items():    # key와 values를 쌍으로 하여 튜플 형태로 보여줌
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")      # 과목은 8개 공간만들고 왼쪽 정렬, score는 정렬을 위해 문자로 만들어줘야함

# # 은행 대기순번표
# # 001, 002, 003....
# for num in range(1,21):
#     print("대기번호:"+ str(num).zfill(3))            # zfill : 3자리로 만들고 zero 를 fill하는 것


# # 표준입출력 예시
# answer = input("아무 값이나 입력하세요: ")
# print("입력하신 값은 " + answer + "입니다")

# print(type(answer))  
# #사용자 input에 의해 입력되면 항상 문자 type

# # 다양한 출력 포맷
# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# print("{0: <10}".format(500))
# # 양수일 때는, + 로 표시 / 음수일 땐 - 로 표시
# print("{0: >+10}".format(+500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(1000000000))
# # 3자리 마다 콤마를 찍어주기,+_부호도 붙이기
# print("{0:+,}".format(1000000000))
# print("{0:+,}".format(-1000000000))
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 30자릿 수 확보하기
# # 돈이 많으면 행복하니까 빈자리는 ^로 채워주기
# print("{0:^<+30,}".format(1000000000))

# # 소수점 출력
# print("{0:f}".format(5/3))
# print("{0:.2f}".format(5/3))  #특정 자리수까지 .2f -> 2자리까지


# # # 파일 입출력
# # 파일을 열어서 점수 정보를 입력하는 것.

# score_file = open("score.txt", "w", encoding = "utf8")  
# # score.txt = 파일명 "w" = write 쓰기위한 목적(덮어쓰기)으로 열기  utf8 한글 문자 오류 방지

# print("수학 : 0 ", file=score_file)
# print("영어 : 50 ", file=score_file)    # 이 내용을 파일에 작성  # 자동 줄바꿈됨
# score_file.close()          # 파일을 열고나면 꼭 닫아줘야함

# #좌측에 score.txt 파일이 생성되고 위의 정보가 입력되어 있음.

# score_file= open("score.txt", "a", encoding ="utf8")  # a는 append(위와 다르게 덮어쓰지 않고 추가)
# score_file.write("과학 : 80")    # print에서는 자동 줄바꿈이지만 이 경우 줄바꿈 안함
# score_file.write("\n코딩 : 80")    # \n은 줄바꿈
# score_file.close

# # 파일 내용 읽어오기
# score_file = open("score.txt", "r", encoding= "utf8")   # r은 read
# print(score_file.read())  #모든 내용 읽어옴
# score_file.close()

# 한줄씩 작업하기
# score_file = open("score.txt", "r", encoding= "utf8")
# print(score_file.readline())        # 한 줄만 읽어오고 커서를 다음줄로 이동
# print(score_file.readline()) 
# print(score_file.readline()) 
# print(score_file.readline()) 
# score_file.close()                  # print에서는 자동으로 줄바꿈을 하므로 한 줄씩 띄워서 나옴

# print(score_file.readline(), end= " ") 
# print(score_file.readline(), end= " ") 
# print(score_file.readline(), end= " ") 
# print(score_file.readline(), end= " ") 
# score_file.close()

# # 총 몇 줄 있는지 모를 때

# score_file = open("score.txt", "r", encoding= "utf8")

# while True :
#     line = score_file.readline()
#     if not line :
#         break       # 바로 반복문 탈출
#     print(line)     # line이 있으면 해당 line 출력
# score_file.close()


# # list 활용
# score_file = open("score.txt", "r", encoding= "utf8")
# lines = score_file.readlines()    # 각 line을 list 형태로 저장
# for line in lines :
#     print(line, end = " ")
    
# score_file.close()

# # pickle
# # 프로그램 상 사용하는 데이터를 파일 형태로 저장 -> 전달하면 pickle을 데이터로 가져와서 사용 가능

# import pickle   # pickle 모듈 불러오기
# profile_file = open("profile.pickle", "wb")   # wb = 쓰기 binary /pickle 쓰려면 binary 해줘야함 # pickle은 encoding 설정 필요없음 
# profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구","골프", "코딩"]}  # 사전 형태 {}
# print(profile)
# pickle.dump(profile, profile_file)      # profile에 있는 정보를 file에 저장

# profile_file.close()

# # pickle 정보 불러오기
# profile_file = open("profile.pickle", "rb")   # rb : read binary
# profile = pickle.load(profile_file)             # pickle.load 이용하여 file의 내용 불러오기
# print(profile)

# profile_file.close()


# # with
# 파일 열고 닫기 편하게

# import pickle

# with open("profile.pickle", "rb") as profile_file:     # 파일을 열고 profile_file 변수로 지정
#      print(pickle.load(profile_file))

# 파일을 닫지 않아도 됨.

# # with로 파일 쓰고 불러오기
# with open("study.txt", "w", encoding= "utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt","r", encoding= "utf8") as study_file:
#     print(study_file.read())