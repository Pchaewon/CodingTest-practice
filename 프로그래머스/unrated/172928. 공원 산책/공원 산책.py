def solution(park, routes):
    r,c,R,C = 0,0,len(park),len(park[0])
    move = {"E":(0,1),"W":(0,-1),"S":(1,0),"N":(-1,0)}
    for i,row in enumerate(park):
        if "S" in row:
            r,c = i,row.find("S")
            break

    for route in routes:
        dr,dc = move[route[0]]
        new_r,new_c = r,c
        for _ in range(int(route[2])): 
            if 0<=new_r+dr<R and 0<=new_c+dc<C and park[new_r+dr][new_c+dc] != "X":
                new_r,new_c = new_r+dr,new_c+dc
            else: 
                new_r,new_c = r,c
                break
        r,c = new_r,new_c

    return [r,c]