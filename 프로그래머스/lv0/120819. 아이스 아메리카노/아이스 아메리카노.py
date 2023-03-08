def solution(money):
    answer = []
    
    coffee_num = money//5500
    change = money%5500

    answer.append(coffee_num)
    answer.append(change)
    
    return answer