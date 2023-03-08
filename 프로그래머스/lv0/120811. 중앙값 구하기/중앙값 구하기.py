def solution(array):
    array.sort(reverse=False)
    arr_len = len(array)
    center_index = arr_len//2
    
    return int(array[center_index])