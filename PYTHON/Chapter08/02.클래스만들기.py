class Monster:
    def say(self):
        print("나는 몬스터다!")
        
goblin = Monster()
goblin.say()


# 파이썬에서는 자료형도 클래스다
a=10
b="문자열객체"
c=True

print(type(a))
print(type(b))
print(type(c))
print(b.__dir__()) # 메서드 확인 가능한 함수!