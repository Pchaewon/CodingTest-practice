def solution(emergency):
    important = emergency.copy()
    important.sort(reverse=True)
    answer = []
    
    for n in emergency:
        answer.append(important.index(n)+1)
    return answer