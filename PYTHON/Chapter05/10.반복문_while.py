# 초기식
# while 조건식 : 
#   반복할 명령
#   증감식

# i=0
# while i<10:
#     print(i, "번째 다짐, 나는 할 수 있다!")
#     i+=1

# 무한루프와 break
# while True:
#     반복할 명령
#     if 조건식:
#         break

# while True:
#     x=input("종료하려면 exit을 입력하세요>>")
#     if x == 'exit':
#         break

# while
# : 보통 반복 횟수가 정해지지 않았을 때 사용한다.
i=5 #초기식
while i<9: #조건식
    print(i, "번째 다짐, 나는 할 수 있다!")
    i += 2 #증감식

# 무한 루프
# : 조건식에 True를 넣어서 항상 반복되게 만든 것.
while True:
    x = input("종료하려면 exit를 입력하세요 >>> ")
    if x == "exit":
        break
