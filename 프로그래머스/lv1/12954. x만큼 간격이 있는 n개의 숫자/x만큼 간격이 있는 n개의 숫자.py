def solution(x, n):
    answer = []
    sum = x
    for i in range(0, n):
        answer.append(sum)
        sum += x        
    return answer