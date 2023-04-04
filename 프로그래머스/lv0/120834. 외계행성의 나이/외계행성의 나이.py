def solution(age):
    universe_age = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f', '6':'g', '7':'h'
                   ,'8':'i','9':'j'}
    answer = ''
    age = str(age)
    for i in age:
        answer += universe_age[i]
    
    return answer