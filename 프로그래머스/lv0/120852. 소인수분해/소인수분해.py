def solution(n):
    answer = []
    a =2
    while a <= n:
        if n%a == 0:
            if a not in answer:
                answer.append(a)
            n = n//a 
        else:
            a += 1
    return answer