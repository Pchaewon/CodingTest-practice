def solution(numbers):
    answer = []
    numbers = sorted(numbers)
    
    answer.append(numbers[0]*numbers[1])
    answer.append(numbers[-1]*numbers[-2])
    
    
    return sorted(answer)[-1]