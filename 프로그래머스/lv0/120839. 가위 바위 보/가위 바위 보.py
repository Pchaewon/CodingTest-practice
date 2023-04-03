def solution(rsp):
    # 2 가위, 0 바위, 5 보
    rsp = str(rsp)
    answer = ''
    
    for m in rsp:
        if m == '2':
            answer += "0"
        elif m == '0':
            answer += "5"
        else:
            answer += "2"
    
    return answer