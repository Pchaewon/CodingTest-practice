# try : 예외가 발생할 수 있는 코드
# except : 예외 발생시 실행할 코드
# else : 예외 발생하지 않은 경우 실행할 코드
# finally : 항상 실행할 코드

# 원화를 입력, 환률 입력 -> 달러 값

won = input("원화 금액을 입력 하세요 >>>")
dollar = input("환율을 입력 하세요 >>>")

try: # 예외가 발생할 수 있는 코드
    print(int(won)/int(dollar))
except ValueError as e: # 예외가 발생했을 때 실행되는 코드
    print("예외가 발생했습니다.", e)
except ZeroDivisionError as e:
    print("예외가 발생했습니다.", e)
else:
    print("예외가 발생하지 않았을 때 실행되는 코드")
finally: # 파일 닫기
    print("예외가 발생하던지, 발생하지 않던지 항상 실행되는 코드")