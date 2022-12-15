# 한국어 연습 프로그램 ver 2.0
# word_list = ["사랑해", "귀엽다", "고마워", "행복해"]

# print("Let's Learning Korean")
# correct = 0
# uncorrect = 0
# for word in word_list:
#     print(word)
#     data=input()
#     if data == word:
#         correct += 1
#     if data!=word:
#         uncorrect += 1
#         #break
    
# print("전체 문제 개수 :", len(word_list),"개")
# print("맞힌 문제 개수 :", correct,"개")
# print("틀린 문제 개수 :", uncorrect,"개")

## 방법 2
word_list = ["사랑해", "귀엽다", "고마워", "행복해"]

print("Let's Learning Korean")
score = 0
for word in word_list:
    print(word)
    data=input()
    if data == word:
        score += 1

print("전체 문제 개수 :", len(word_list),"개")
print("맞힌 문제 개수 :", score,"개")
print("틀린 문제 개수 :", len(word_list)-score,"개")
