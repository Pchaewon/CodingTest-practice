def solution(hp):
    answer = 0 
    if hp>5:
        answer += hp//5 # 장군
        if hp%5!=0:
            answer += (hp%5)//3 # 병정
            if ((hp%5)%3)!=0:
                answer += ((hp%5)%3)//1
            else:
                return answer
    elif 5>hp>=3: 
        answer += hp//3
        if hp%3!=0:
            answer += (hp%3)//1 # 병정
    elif 3>hp>0:
        answer += hp//1 
    elif hp==0:
        answer = 0
    return answer