list = []

list.append(int(input("1일차 턱걸이 횟수>>>")))
list.append(int(input("2일차 턱걸이 횟수>>>")))
list.append(int(input("3일차 턱걸이 횟수>>>")))
list.append(int(input("4일차 턱걸이 횟수>>>")))
list.append(int(input("5일차 턱걸이 횟수>>>")))
list.append(int(input("6일차 턱걸이 횟수>>>")))
list.append(int(input("7일차 턱걸이 횟수>>>")))

result=(list[0]+list[1]+list[2]+list[3]+list[4]+list[5]+list[6])/len(list)

print(int(result))