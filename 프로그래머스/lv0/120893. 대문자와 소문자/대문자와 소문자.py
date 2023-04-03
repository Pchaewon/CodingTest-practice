def solution(my_string):
    answer = ''
    for n in my_string:
        if n==n.lower():
            answer += n.upper()
        elif n==n.upper():
            answer += n.lower()
        else:
            pass
    
    return answer