def solution(dot):
    answer = [1,2,3,4]
    if dot[0]>0 and dot[1]>0:
        return answer[0]
    elif dot[0]>0 or dot[1]>0:
        if dot[0]<0:
            return answer[1]
        else:
            return answer[3]
    else:
        return answer[2]
        
    
    return answer