from collections import deque
import sys

len_element = int(sys.stdin.readline())
box = deque()

for i in range(len_element):
  command = sys.stdin.readline()
  if command.find('push')!= -1:
    command = command.replace('push ', '')
    box.append(int(command))

  elif command.find('pop')!= -1:
    if len(box) !=0:
      print(box[0])
      box.popleft() 
    else: 
      print(-1)

  elif command.find('size')!= -1:
    print(len(box))

  elif command.find('empty')!= -1:
    if len(box) != 0:
      print(0)
    else :
      print(1)

  elif command.find('front')!= -1:
    if len(box)!=0:
      print(box[0])
    else:
      print(-1)

  elif command.find('back')!= -1:
    if len(box) != 0:
      print(box[-1])
    else:
      print(-1)