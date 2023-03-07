def solution(my_string, num1, num2):
    my_list = list(my_string)
    
    word1 = my_list[num1]
    word2 = my_list[num2]
    my_list[num2] = word1
    my_list[num1] = word2

    return ''.join(my_list)    
    
