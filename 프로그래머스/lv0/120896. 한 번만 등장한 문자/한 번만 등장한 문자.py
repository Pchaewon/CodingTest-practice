def solution(s):
    answer = ''
    set_s = list(set(s))
    set_s.sort()
    
    for a in set_s:
        if s.count(a)==1:            
            answer += a
    
    return answer