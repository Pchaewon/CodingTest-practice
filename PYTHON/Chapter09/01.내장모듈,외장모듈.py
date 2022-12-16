# (22.12.16) 코딩 너무 재밌당. 오늘도 화이팅!!!
# 모듈 : 프로그램 기능별로 파일을 나누어서 관리하면 유지보수가 편리.

# 1. 내장 모듈 사용
#  : 파이썬 설치 시 자동으로 설치되는 모듈
# import 모듈이름
# 모듈이름.변수
# 모듈이름.함수()
import math

print(math.pi)
print(math.ceil(2.7))

from math import pi, ceil as c

print(pi)
print(c(2.7))

# 2. 외부 모듈 사용
#  :  다른 사람이 만든 파이썬 파일 pip로 설치해서 사용
# pyautogui
# pip install 모듈이름

import pyautogui as pg

pg.moveTo(500, 500, duration=2)

