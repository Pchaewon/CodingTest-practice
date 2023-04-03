def solution(my_string):
    Vowel = ['a','e','i','o','u']
    for i in Vowel:
        my_string = my_string.replace(i,'')
    return my_string