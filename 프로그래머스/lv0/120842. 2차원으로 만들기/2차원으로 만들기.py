def solution(num_list, n):
    answer = []
    num = len(num_list)
    a = num//n
    
    i=0
    while True:
        answer.append(num_list[i:i+n])
        if i+n==num:
            return answer
        else:
            pass
        i += n
    
    return answer