def printSumAvg(x,y,z):
    sum = x+y+z
    avg = int(sum/3)
    #return print("합계:",sum, "평균:",avg)
    return print(f"합계:{sum} 평균:{avg}") # 문자열 포매팅 방법

printSumAvg(10,20,30)
