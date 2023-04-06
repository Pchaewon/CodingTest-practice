def solution(i, j, k):
    answer = 0
    
    for n in range(i, j+1):
        if str(n).find(str(k)) != -1:
            answer +=int(str(n).count(str(k)))
    return answer