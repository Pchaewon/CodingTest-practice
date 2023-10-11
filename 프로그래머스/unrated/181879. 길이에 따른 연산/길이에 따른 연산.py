def solution(num_list):
    answer = 0
    if len(num_list)>=11:
        for n in num_list:
            answer += n
    else:
        answer = 1
        for n in num_list:
            answer *=n
    return answer