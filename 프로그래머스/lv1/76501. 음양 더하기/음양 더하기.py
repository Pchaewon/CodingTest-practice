def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i]==False:
            absolutes[i] = -absolutes[i]
        else:
            pass
    return sum(absolutes)
