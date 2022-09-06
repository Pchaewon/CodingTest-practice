n = int(input())
a= list(map(int, input().split()))
# print(a)
# print(len(a))

if len(a)>n:
    print("error1")
elif len(a)<n:
    print("error2")
else : 
    print(min(a))
    print(max(a))


