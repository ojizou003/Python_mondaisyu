man_HP = 300
monster_HP = 100

print("モンスターがあらわれた！\n")

for i in range(3):
  damage = input("attack or magic or heart? \n>>>")
  
  if damage == "attack":
    monster_HP -= 50
    print("モンスターに 50 のダメージ！\n")

  if damage == "magic":
    monster_HP -= 70
    print("モンスターに 70 のダメージ！\n")
    
  if damage == "heart":
    monster_HP -= 100
    print("モンスターが仲間になりました！")
    break
    
  if damage != "magic":
    man_HP -= 100
    print("モンスターの攻撃！")
    print("勇者に 100 のダメージ！\n")
    
  if monster_HP <= 0:
    print("モンスターをたおしました！")
    break
  
  if man_HP <= 0:
    print("勇者はたおれました・・・")
    break
  
if monster_HP > 0:
  print("モンスターに逃げられました・・・")