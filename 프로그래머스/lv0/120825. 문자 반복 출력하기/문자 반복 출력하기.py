def solution(my_string, n):
    answer = []
    for w in my_string:
        answer.append(w*n)
    return ''.join(answer)