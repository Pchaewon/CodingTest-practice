def solution(my_string):
    answer = []
    my_string = my_string.lower()
    for i in my_string:
        answer.append(i)
    answer.sort()
    
    return ''.join(answer)