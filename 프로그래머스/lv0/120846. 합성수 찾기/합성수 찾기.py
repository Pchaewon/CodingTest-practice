def solution(n):
    answer = 0
    count = 0
    num = []
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i%j==0:
                count += 1
        if count >= 3:
            answer += 1
        count = 0
    return answer