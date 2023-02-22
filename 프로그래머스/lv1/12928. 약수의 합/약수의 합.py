def solution(num):
    answer = 0
    for n in range(1, num+1):
        if num%n==0:
            answer += n
    return answer