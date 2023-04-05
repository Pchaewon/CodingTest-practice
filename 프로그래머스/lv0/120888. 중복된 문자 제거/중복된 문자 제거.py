def solution(my_string):
    answer = ''
    
    word = ''.join(list(set(my_string)))
    
    for n in my_string:
        if word.find(n) != -1:
            answer += n
            word = word.replace(n, '')
    
    return answer