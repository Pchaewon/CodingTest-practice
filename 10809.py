## index(): list method 중 하나. list 중에서 특정한 원소가 몇 번째에 처음 등장하는지 알려줌. 
## 두 번 이상 원소가 중복되어 존재하는 경우 맨 처음 등장한 순간의 인덱스 출력.

s = list(input())
c='abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in s:
        print(s.index(i), end=' ')
    else : 
        print(-1, end=' ')

        
        
# find() : 찾는 문자가 없는 경우 -1 출력
# s=input()
# for x in 'abcdefghijklmnopqrstuvwxyz':
#     print(s.find(x), end=' ')