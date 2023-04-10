def solution(lines):
    answer = 0
    box = [line for line in lines]
    b_box = []
    
    for b in box :
        for i in range(b[0]+1, b[1]+1):
            b_box.append('{0} {1}'.format(i-1,i))
    
    bb_box = list(set(b_box))
    
    for bb in bb_box:
        if b_box.count(bb)>1:
            answer += 1
    
    return answer