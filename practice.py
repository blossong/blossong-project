
# # #문자열
# # sentence = '나는 소년입니다'
# # print(sentence)
# # sentence2 = "파이썬은 쉬워요"
# # print(sentence2)
# # sentence3="""
# # 나는 소년이고, 
# # 파이썬은 쉬워요
# # """
# # print(sentence3)

# #슬라이싱 : 필요한 정보만 잘라서 사용하는 것
# # jumin= "940530-2114217"

# # print("성별 :" + jumin[7]) #세는 숫자는 0부터 시작
# # print("연 : " + jumin[0:2]) #0부터 2직전까지
# # print("월 :" + jumin[2:4])
# # print("일 : "+ jumin[4:6])

# # print("생년월일은 : "+jumin[0:6])
# # print("생년월일은 : "+jumin[:6]) #0을 생략해도됨
# # print("뒤 7자리 : "+ jumin[7:14])
# # print("뒤 7자리 : "+ jumin[7:14]) #끝까지이면 생략해도됨.

# # #맨 뒤에서 7번째부터 끝까지
# # print("뒤 7자리(뒤에서부터) :"+ jumin[-7:]) #맨뒤는 -1번쨰

# #문자열 처리함수
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())

# print(python[0]. isupper()) #첫번째글자가 대문자인지 확인
# #문자의 총 길이
# print(len(python))
# #Replace: python 이라는 문자만 찾아서 변환(Python->Java
# print(python.replace("python","Java"))
# #python에서 n의 위치가 어디인지 출력하라(index)
# index= python.index("n")
# print(index)
# #앞에서 찾은 n다음위치부터 n의 위치를 찾아라(다음 n)
# index = python.index("n",index+1)
# print(index)
# #find함수도 사용 가능. Python에서 "Java"를 찾아라 
# print(python.find("Java"))
# # -> -1 출력하고 종료하지 않음
# # print(python.index("Java"))
# #index는 위와 동일하게 처리하면 오류됨. 종료됨


# #python 함수에서 n이 총 몇 개인지 찾아라.(count)
# count = python.count("n")
# print(count)
# print(python.count("n"))

#문자열 포맷
#방법1
# print("나는 %d살입니다." % 20) #d는 정수값만 가능
# print("나는 %s을 좋아해요" %"파이썬") # %s 은 문자열, string값을 넣는다.
# print("Apple은 %c로 시작해요" % "A")  # %c 는 문자 하나만 가져오는 것.
# # %s 는 정수, 문자이든 상관없이 출력 가능
# print("나는 %s살입니다." % 20)

# #나는 파란색과 빨간색을 좋아해요(%s)

#방법2
# print("나는 {}살입니다." .format(20))
# # print("나는 {}색과 {}색을 좋아해요" .format("빨간", "파란"))
# # print("나는 {0}색과 {1}색을 좋아해요" .format("빨간", "파란"))
# # print("나는 {1}색과 {0}색을 좋아해요" .format("빨간", "파란"))

# #방법3
# #나는 20살이며 빨간색을 좋아해요 age, color
# print("나는 {age}살이며 {color}색을 좋아해요" .format(age = 20, color ="빨간"))

# #방법4
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")
# # f를 입력하고 쓰면 변수 입력됨.

# #탈출문자
# # \n: 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")

# #저는 "나도코딩"입니다.
# print("저는 '나도코딩'입니다.") 
# print('저는 "나도코딩"입니다.')

# print("저는 \"나도코딩\"입니다.") 
# print("저는 \'나도코딩\'입니다.")
# #\ 을 앞에 써줌으로써 " 또는 ' 나오게 가능

# #\\  : 문장 내에서 \
# #  C:\Users\song\Desktop\pythonworkspace> 을 출력
# print("C:\\Users\\song\\Desktop\\pythonworkspace>" )

# \r: 커서를 맨 앞으로 이동
# print("Red Apple\rPine")
# #\r을 통해 커서를 맨앞으로 이동하여 Pine을 덮어쓰기함.

# # \b : 백스페이스 역할
# print("Redd\bApple")

# #\t : 탭 역할 (여러 칸 띄우고 입력하여 출력)
# print("red\tApple")

#퀴즈 (오답)
# 예: http://naver.com
# 규칙1: http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 "e" 갯수
#   + "!"로 구성
#예> 생성된 비밀번호 : nav51!

#한번에 변수를 모두 지정하려 하지 말것. 순차적임을 기억하기
#동일한 형태의 변수라도 아래에서 새로 지정할 수 있다.
#print를 변수로 지정하면 재가공하기 어려움(안됨?)
#미리 출력물 확인하고 나서는 주석 처리 또는 삭제
url = "http://naver.com"
my_str = url [7:]  #규칙1
# print(my_str)
my_str= my_str.replace(".com", "") #규칙2
# print(my_str)
password = my_str[:3] + str(len(my_str))+ str(my_str.count("e"))+"!"

print("{0}사이트의 비밀번호는 {1} 입니다.".format(url,password))
















