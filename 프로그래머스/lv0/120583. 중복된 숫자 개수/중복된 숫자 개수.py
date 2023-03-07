def solution(array, n):
    count = 0
    for num in array:
        if num==n:
            count += 1
        else:
            continue
    return count