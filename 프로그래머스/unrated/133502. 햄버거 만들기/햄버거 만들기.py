def solution(ingredient):
    num_stack = []
    count = 0
    for i in ingredient:
        num_stack.append(i)
        if num_stack[-4:] == [1, 2, 3, 1]:
            count += 1
            for j in range(4):
                num_stack.pop()
    return count


