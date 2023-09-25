Pman_HP = 5

monster_HP = 100

print("モンスターが現れた！")

for i in range(3):
  damage = input("attack or run-away ? \n")

  if damage == "attack":
    monster_HP -= 1
    print("モンスターに 1 のダメージ！ \n")

    Pman_HP -= 10
    if Pman_HP <= 0:
      print("モンスターの反撃！ 10 ノダメージ！ \n""Pmanは、たおれました・・・")
      break
    
  if damage == "run-away":
    Pman_HP += 5
    print("Pmanは、逃げ出しました \n""Pmanの HP が 5 上がりました")
    break
  
if Pman_HP > 0:
  print("Pman「わたしは強くなる！」")