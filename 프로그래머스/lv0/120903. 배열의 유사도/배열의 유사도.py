def solution(s1, s2):
    answer = 0
    word_sum = []
    
    for i in s1:
        answer += s2.count(i)
    return answer