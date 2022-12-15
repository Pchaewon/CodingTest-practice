#로또 예상번호 추출 프로그램
## 복습,,,,!! 필요,,,,!!

import random 

def getRandomNumber():
    number = random.randint(1,45)
    return number

lotto_num = []

count = 0 #현재 뽑은 숫자 개수

while True:
    if count > 5:
        break
    random_number = getRandomNumber()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count += 1
        
lotto_num.sort()

for num in lotto_num:
    print(num, end=' ')
