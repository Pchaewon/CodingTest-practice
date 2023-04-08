def solution(array, n):
    answer = []
    array.sort()
    for a in array:
            answer.append(abs(n-a))

    num = min(answer)
    indexes_of_min = []
    
    if answer.count(num)>1:
        for i in range(len(answer)):
            if answer[i] == num:
                indexes_of_min.append(i)
        index_of_min = min(indexes_of_min)
        return array[index_of_min]
    else:
        return array[answer.index(num)]
    