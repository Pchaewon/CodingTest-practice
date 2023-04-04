def solution(num, k):
    i=1
    
    for n in str(num):
        if n==str(k):
            return i
        else:
            pass
        i += 1
        
    return -1
    