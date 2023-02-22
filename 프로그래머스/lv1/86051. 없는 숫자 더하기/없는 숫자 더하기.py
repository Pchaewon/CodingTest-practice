def solution(numbers):
    answer = set([0,1,2,3,4,5,6,7,8,9])
    num = set(numbers)
    diff = answer - num
    sum_box = 0
    
    for n in diff:
        sum_box += n
    return sum_box