def solution(my_string):
    answer = []
    
    for s in my_string:
        if s.isalpha():
            my_string = my_string.replace(s, ' ')
    my_string = my_string.split()
    answer = sum(map(int, my_string))
    return answer