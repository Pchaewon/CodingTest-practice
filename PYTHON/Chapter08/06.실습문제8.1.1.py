# MMORPG
# 아이템 공통 : 이름, 가격, 무게, 판매하기, 버리기
# 장비 아이템 : 착용효과, 착용하기
# 소모품 아이템 : 사용효과, 사용하기
# 단, 버리기는 버릴 수 있는 아이템만 가능하다.

#부모 클래스
class Item():
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
        
    def sale(self):
        print(f"[{self.name}] 판매가격은 [{self.price}]")
        
    def discard(self):
        if self.isdropable:
            print(f"[{self.name}]을 버렸습니다.")
        else:
            print(f"[{self.name}]을 버릴 수 없습니다.")

# 자식 클래스1
class WearableItem(Item):
    # 오버라이딩
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
        
    def wear(self):
        print(f"[{self.name}]을 착용했습니다. {self.effect}")

# 자식 클래스2
class UsableItem(Item):
    # 오버라이딩
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
        
    def use(self):
        print(f"[{self.name}]을 착용했습니다. {self.effect}")


# 인스턴스 생성
sword = WearableItem("이가닌자의검", 30000, 3.5, True, "체력 5000 증가, 마력 5000 증가")
sword.wear()        
sword.sale()
sword.discard()

potion = UsableItem("신비한투명물약", 150000, 0.1, False, "투명효과 300초 지속")
potion.discard()
potion.use()        
