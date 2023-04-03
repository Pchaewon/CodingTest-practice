def solution(cipher, code):
    answer = []
    word_list = list(cipher)
    
    index = code-1
    while index<len(word_list):
        answer.append(word_list[index])
        index += code
        
    return ''.join(answer)