a = int(input("국어>>>"))
b = int(input("수학>>>"))
c = int(input("영어>>>"))

mean = (a+b+c)/3

# # 방법 1
# if 100>=a>=0 and 100>=b>=0 and 100>=c>=0 :
#     if mean >= 80:
#         print("불합격")
#     else : 
#         print("합격")
# else:
#     print("잘못 입력하셨습니다.")
    
# 방법 2
if  a<0 or a>100 or b<0 or b>100 or c<0 or c>100 :
    print("잘못 입력하셨습니다.")
else : 
    if mean >= 80:
        print("불합격")
    else : 
        print("합격")