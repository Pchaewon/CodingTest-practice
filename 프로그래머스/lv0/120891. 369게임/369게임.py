def solution(order):
    answer = 0
    for n in str(order):
        if n=='3' or n=='6' or n=='9':
            answer += 1
        else:
            pass
    return answer