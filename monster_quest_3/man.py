# man.py

from random import *
import fire_mon_star as fms

MAN_NAME = "man"
MAN_HP = 150

def yusha():
  if MAN_HP <= 0:
    print(f"{MAN_NAME}はたおれました・・・")
    return 0
  
  answer = input("attack or flee or bye ? \n>>>")
  if answer == "attack":
    man_atk = randint(15,30)
    print(f"{MAN_NAME}の攻撃！{man_atk}のダメージ！")
    return man_atk
  elif answer == "bye":
    print(f"{fms.FMS_NAME}は喜んでかえりました♪")
    return "bye"
  else:
    print(f"{MAN_NAME}は逃げきりました。")
    return "flee"
  
if __name__ == "__main__":
  yusha()