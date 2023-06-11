def solution(my_string, n):
    answer = ''
    my_list = list(my_string)
    list_len = len(my_list)
    
    for s in range(list_len-n,list_len):
            answer += my_list[s]
    
    return answer
    