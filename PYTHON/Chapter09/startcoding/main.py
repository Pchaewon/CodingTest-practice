# 1. import 패키지.모듈
# import unit.character
# unit.character.test()

# 2. from 패키지 import 모듈
# from unit import item
# item.test()

# 3. from 패키지 import *
# from unit import * # *를 쓸때는 init모듈을 수정해줘야함
# character.test()
# item.test()
# monster.test()

# 4. import 패키지
import unit
unit.character.test()
unit.item.test()
unit.monster.test()