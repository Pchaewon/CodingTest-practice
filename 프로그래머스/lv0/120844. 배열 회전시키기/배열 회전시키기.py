def solution(numbers, direction):
    answer = []
    if direction=="right":
        answer.append(numbers[-1])
        for n in numbers[:-1]:
            answer.append(n)
    elif direction == "left":
        for n in numbers[1:]:
            answer.append(n)
        answer.append(numbers[0])
            
    return answer