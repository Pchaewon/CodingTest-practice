def solution(id_pw, db):
    count = [0,0,0]
    for i in range(len(db)):
        if db[i][0]==id_pw[0]:
            if db[i][1]==id_pw[1]:
                count[0] += 1
            else:
                count[1] +=1
        else:
            count[2] += 1
    
    if count[0]==1:
        return "login"
    elif count[1]==1:
        return "wrong pw"
    else: 
        return "fail"