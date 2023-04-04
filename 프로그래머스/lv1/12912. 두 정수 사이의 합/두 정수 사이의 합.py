def solution(a, b):
    answer = 0
    
    if b>a:
        c = b-a
        for i in range(c+1):
            answer += a+i
    else:
        c = a-b
        for i in range(c+1):
            answer += b+i
        
    return answer