def solution(num_list):
    sum_num = 0
    pro_num = 1
    
    for n in num_list:
        sum_num += n
        pro_num *= n
    
    if sum_num**2 > pro_num:
        return 1
    return 0