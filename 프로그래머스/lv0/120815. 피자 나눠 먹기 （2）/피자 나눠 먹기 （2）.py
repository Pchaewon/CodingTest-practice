def solution(n):
    for i in range(6,1000000,6):
        if i%n == 0:
            answer = i/6
            break

    return answer