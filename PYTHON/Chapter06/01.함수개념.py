# 함수 사용이유
# 1. 재사용성이 좋아짐
# 2. 유지보수가 편리해짐
# 3. 가독성이 좋아짐

#함수를 사용하지 않은 경우
print("안녕하세요. ㅁㅁ님")
print("현재 프리미엄 서비스 사용기간이 7일 남았습니다.")

#함수를 사용하는 이유
def printMessage(name, date):
    print("안녕하세요.", name, "님")
    print("현재 프리미엄 서비스 사용기간이", date, "일 남았습니다.")

printMessage("동환", 100)

# 1. 매개변수가 없는 함수
# 정의하기
# def 함수이름():
#   명령블록
def printHello():
    print("Hello")

# 호출하기
# 함수이름()
printHello()

# 2. 매개변수가 있는 함수
# 정의하기
# def 함수이름(매개변수1, 매개변수2):
#   명령블록
def sum(a,b):
    print(a+b)
# 호출하기
# 함수이름(인자1, 인자2)
sum(3,4)

# 3. 반환값이 있는 함수
# 정의하기
# def 함수이름():
#   명령블록
#   return 반환값
import random
def getRandomNumber():
    number = random.randint(1,10)
    return print(number)
#호출하기
#함수이름()
getRandomNumber()

# 4. 매개변수와 반환값이 있는 함수
# 정의하기
# def 함수이름(매개변수1, 매개변수2):
#   명령블록
#   return 반환값
def sum(a,b):
    result = a+b
    return result
# 호출하기
print(sum(3,4))