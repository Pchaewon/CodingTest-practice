def a(num):
    return num//2
def b(num):
    return (num*3)+1

def solution(num):
    answer = 0
    
    if num==1:
        return 0
    
    while num != 1:
        # 1-1.
        if num%2==0:
            num = a(num)
            answer += 1
        # 1-2
        else:
            num = b(num)
            answer += 1
            
        if answer >= 500:
            return  -1
        else:
            pass
    return answer