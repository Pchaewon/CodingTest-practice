def solution(my_string):
    answer = []
    for n in reversed(my_string):
        answer.append(n)
    result = ''.join(str(s) for s in answer)
    return result