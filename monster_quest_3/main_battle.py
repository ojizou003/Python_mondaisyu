# main_battle.py
'''Monster Quest 3 main battle'''
import man
import fire_mon_star as fms

def main_battle():
  # モンスターの出現
  print(f"{fms.FMS_NAME}が現れた！")
  # バトル開始
  while man.MAN_HP > 0 and fms.FMS_HP >0:
    # 勇者の体力の状態
    print(f"manHP : {man.MAN_HP}")
    # 勇者の攻撃
    y = man.yusha()
    if y == "bye":
      break
    elif y == "flee":
      break
    else:
      fms.FMS_HP -= y
    
    # ファイアモンスターの体力の状態
    print(f"fmsHP:{fms.FMS_HP}")
    # ファイアモンスターの攻撃
    z = fms.fire_mon_star()
    man.MAN_HP -= z
    if man.MAN_HP < 0:
      print("勇者はたおれました・・・")

if __name__ == "__main__":
  main_battle()
