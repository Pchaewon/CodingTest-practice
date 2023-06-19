import sys

len_element= int(sys.stdin.readline())
stack = []

for i in range(len_element):
  element = sys.stdin.readline()
  if element.find('push') != -1:
    x, y =map(str, element.split())
    stack.append(int(y))
  elif element.find('pop') != -1:
    if len(stack)==0:
      print(-1)
    else:
      print(stack[-1])
      stack.pop()
  elif element.find('top') != -1:
    if len(stack)==0:
      print(-1)
    else:
      print(stack[-1])
  elif element.find('size') != -1:
    print(len(stack))
  elif element.find('empty') != -1:
    if len(stack)==0:
      print(1)
    else:
      print(0)