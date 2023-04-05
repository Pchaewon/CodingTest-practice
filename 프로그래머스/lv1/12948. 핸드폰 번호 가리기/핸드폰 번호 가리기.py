def solution(phone_number):
    n = len(phone_number)
    phone_neber = str(phone_number)
    for i in range(n-4):
        phone_number = phone_number.replace(phone_number[i],'*',1)
    
    return phone_number