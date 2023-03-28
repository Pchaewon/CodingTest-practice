def rank(n,a,b):
    for i in range(n):
        if 2**i >= a:
            A = i
            break
    
    for i in range(A, n):
        if 2**i >= b:
            B = i
            break
    
    if A==B:
        num = 2**(A-1)
        return rank(n-num,a-num,b-num)
    else:
        return B   
    
def solution(n, a, b):
    answer = 0
    if a > b:
        tmp = b
        b = a
        a = tmp
    answer = rank(n,a,b)  
    return answer