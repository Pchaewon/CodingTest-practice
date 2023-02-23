def solution(s):
    p_sum = 0
    y_sum = 0
    for i in list(s):
        if i=='p' or i=='P': 
            p_sum += 1
        elif i=='y' or i=='Y': 
            y_sum += 1
    if p_sum==y_sum:
        return True
    else : 
        return False