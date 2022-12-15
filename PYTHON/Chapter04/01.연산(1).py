# 1. 대입연산
# 변수이름 = 데이터

# 2. 산술연산
# - 숫자 연산
x=5
y=2

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y) # 몫
print(x%y) # 나머지
print(x**y) # 제곱

# - 문자열 연산
tag1 = "#동동사랑해"
tag2 = "#평생같이살자"
tag3 = "#알콩달콩하게!"

tag = tag1+tag2+tag3
print(tag)

message = "동동이 너무너무 사랑해\n" * 5
print(message)

# 복합 할당 연산자
level =10 # (레벨 1 증가)
level += 1 # level = level+1

health=2000 # (체력 300 감소)
health -= 300 # health = health-300

attack=300 # (공격력 1.5배 증가)
attack *= 1.5 # attack = attack*1.5

speed=420 # (이동속도 50% 감소)
speed /= 2 # speed = speed/2

print(level, health, attack, speed)