# fire_mon_star.py

import random as rd

FMS_NAME = "ファイアもんすたー"
FMS_HP = 100

def fire_mon_star():
  if 40<= FMS_HP <=100:
    print(f"{FMS_NAME}はみなぎっている！")
  elif 0 < FMS_HP <40:
    print(f"{FMS_NAME}はじっと耐えている...")
  else:
    print(f"{FMS_NAME}をたおしました。")
    
  mon_fire = rd.randint(30,60)
  mon_atk = rd.randint(15,20)

  if FMS_HP >= 60:
    print(f"火の攻撃！{mon_fire}のダメージ！")
    return mon_fire
  elif 40 < FMS_HP <60:
    print(f"攻撃！{mon_atk}のダメージ！")
    return mon_atk
  else:
    return 0
  
if __name__ == "__main__":
  fire_mon_star()