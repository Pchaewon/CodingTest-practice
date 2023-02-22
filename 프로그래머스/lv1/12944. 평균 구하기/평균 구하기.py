def solution(arr):
    answer=0
    for n in arr:
        answer += n
    return answer/len(arr)
