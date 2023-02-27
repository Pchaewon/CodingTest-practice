def solution(arr):
    answer = []
    answer.append(arr[0])
    for n in arr:
        if answer[-1]==n:
            continue
        else:
            answer.append(n)
    return answer