def solution(my_string):
    answer = 0
    words = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for w in words:
        my_string = my_string.replace(w, '')
    for i in my_string:
        answer += int(i)
    
    return answer