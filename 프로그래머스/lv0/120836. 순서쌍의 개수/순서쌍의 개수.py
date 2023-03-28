def solution(n):
    answer = []
    for i in range(1, 1000000):
        a = 0
        if n%i==0:
            answer.append(f'{i}, {int(n/i)}')
            answer.append(f'{int(n/i)}, {i}')
        else:
            pass
    answer = list(set(answer))
    
    return len(answer)