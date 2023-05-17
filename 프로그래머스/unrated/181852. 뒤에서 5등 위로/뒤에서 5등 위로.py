def solution(num_list):
    answer = []
    num_list.sort()
    for a in num_list[5:]:
        answer.append(a)
    
    return answer
