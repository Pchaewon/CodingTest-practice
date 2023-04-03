def solution(n, t):
    answer = 1
    for i in range(t):
        answer *= 2
    answer *= n
    return answer