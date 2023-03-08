def solution(numbers):
    numbers.sort(reverse=True)
    answer = int(numbers[0]*numbers[1])
    
    return answer