import pay_module

#변수사용
print(pay_module.version)

#함수사용
pay_module.printAuthor()

#클래스
pay_info = pay_module.pay("A102030", 13000, "2021-06-13")
print(pay_info.get_pay_info())

print(pay_module.__name__)