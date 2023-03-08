def solution(array):
    count_list = []
    max_key_name = []
    
    for n in array:
        cnt = array.count(n)
        count_list.append([n, cnt])
    count_dic = dict(count_list)
    
    for k, v in count_dic.items():
        if max(count_dic.values())==v:
            max_key_name.append(k)    
            
    if len(max_key_name)!=1:
        return -1
    else: 
        return max_key_name[0]
    