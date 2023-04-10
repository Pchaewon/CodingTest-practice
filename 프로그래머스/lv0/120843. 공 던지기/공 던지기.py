def solution(numbers, k):
    index = 0
    while k > 1:
        index += 2
        index = index%len(numbers)
        k -= 1
    return numbers[index]