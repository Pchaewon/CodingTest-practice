cash = int(input("현재 가진 금액을 입력>>> "))

if cash >= 20000:
    print("오늘 저녁은... 치킨!")
elif 20000>cash>=10000:
    print("오늘 저녁은... 떡볶이!")
else:
    print("오늘 저녁은... 편의점 김밥!")