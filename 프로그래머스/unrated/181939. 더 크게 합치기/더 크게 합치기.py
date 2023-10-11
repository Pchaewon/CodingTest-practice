def solution(a, b):
    sum_str1 = str(a)+str(b)
    sum_str2 = str(b)+str(a)
    
    if int(sum_str1)>int(sum_str2):
        return int(sum_str1)
    elif int(sum_str1)<int(sum_str2):
        return int(sum_str2)
    else:
        return int(sum_str1)
    