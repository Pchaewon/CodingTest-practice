def solution(arr):
    answer = []
    arr2 = arr.copy()
    arr2.sort()
    for a in arr:
        if arr2[0]==a:
            pass
        else:
            answer.append(a)
    
    if len(arr)==1:
        answer.append(-1)    
    
    return answer