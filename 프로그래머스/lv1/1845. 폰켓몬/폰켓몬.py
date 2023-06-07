def solution(nums):
    same_num = list(set(nums))
    
    if len(nums)//2 <= len(same_num):
        return len(nums)//2
    else:
        return len(same_num)
