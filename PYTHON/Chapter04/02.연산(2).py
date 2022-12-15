# 1. 비교 연산
print('-비교연산')
print(2>3) #F
print(15<30) #T
print(1.5>=0) #T
print(3<=3) #T
print("팔팔팔"=="팔팔팔") #T
print("111111"!="11111") #T
print("111111"!="111111") #F


# 2. 논리 연산
print('-논리연산 문제')
print(4<6 and 10>=10) #T
print("포기하지말아요" != "포기하지말아요" or "나는 할 수 있다"=="나는 할수있다") #F
print("포기하지말아요" != "포기하지말아요" or "나는 할 수 있다"=="나는 할 수 있다") #T
print(not 5==5) #F

# 3. 멤버십 연산
print('-멤버십연산 문제')
print("a" in "abc") # T
print("b" not in "abc")
