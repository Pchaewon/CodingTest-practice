def solution(before, after):
    answer = 0
    len_after = len(after)
    for n in before:
        if after.find(n) != -1:
            answer += 1
            after = after.replace(n,'',1)
        else:
            pass
    
    if len_after==answer:
        return 1
    else:
        return 0
        