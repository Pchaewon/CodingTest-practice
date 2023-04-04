def solution(n):
    answer = []
    re = ''
    for i in str(n):
        answer.append(int(i))
    answer.sort(reverse=True)
    
    for w in answer:
        re += str(w)
    return int(re)