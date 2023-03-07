def solution(array, height):
    count=0
    
    for n in array:
        if int(n)>height:
            count += 1        
        else:
            continue
            
    return count