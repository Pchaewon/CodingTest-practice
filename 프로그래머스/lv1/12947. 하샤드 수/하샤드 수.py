def solution(x):
    num = 0
    str_x = str(x)
    
    for w in str_x:
        num += int(w)
    if x%num==0:
        return True
    else:
        return False
        