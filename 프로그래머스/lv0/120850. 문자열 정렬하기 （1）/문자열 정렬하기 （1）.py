def solution(my_string):
    answer = []
    for w in my_string:
        if '0' == w or '1'== w or '2'== w or '3'== w or '4'== w or '5'== w or '6'== w or '7'== w or '8'== w or '9' == w:
            answer.append(int(w))
        else:
            pass
    return sorted(answer)