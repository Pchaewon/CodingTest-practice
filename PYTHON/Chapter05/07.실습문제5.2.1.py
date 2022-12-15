result = [33,40,12,63,52]
print('변화전:',result)

#문항1
result.append(9)
print('문항1:',result)

#문항2
result[1]=50
print('문항2:',result)

#문항3
result=result[2:6]
print('문항3:',result)

#문항4
result.sort()
print('문항4:',result)