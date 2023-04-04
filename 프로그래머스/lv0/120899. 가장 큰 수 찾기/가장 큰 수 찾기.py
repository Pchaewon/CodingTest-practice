def solution(array):
    answer = []
    answer.append(sorted(array)[-1])
    arr_i = array.index(sorted(array)[-1])
    answer.append(arr_i)
    return answer