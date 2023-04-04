def solution(n):
    answer = 0
    num = int(n**(0.5))
    if n == 1:
        return 4
    else:
        if num!=1 and n%num==0:
            return (num+1)**2
        else:
            return -1