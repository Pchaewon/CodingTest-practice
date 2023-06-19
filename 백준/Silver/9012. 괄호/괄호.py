len_element = int(input())
right_num = 0
left_num = 0

for i in range(len_element):
  box = input()
  for s in box:
    if s == '(':
      right_num += 1
    else :
      left_num += 1
  
  if right_num == left_num:
    while box.find('()') != -1:
      box = box.replace('()', '')
    if box == '':
      print('YES')
    else:
      print('NO')
  else:
    print('NO')
  
  right_num = 0
  left_num = 0
