party = ["man", "BEAR", "Pman"]

man_HP = 100
BEAR_HP = 120
Pman_HP = 5

metal_monster_HP = 30

for i in range(3):
  damage = input("attack or magic ? \n>>>")

  for i in party:
    print(f"{i}のこうげき！",end="")

    if damage == "attack":
      metal_monster_HP -= 1
      print("メタルモンスターに 1 のダメージ！ \n")

    if damage == "magic":
      metal_monster_HP -= 0
      print("メタルモンスターに 0 のダメージ！ \n")
      
    if damage != "attack":
      if damage != "magic":
        print("ミス！\n") 
      
    if metal_monster_HP <= 0:
      print("メタルモンスターをたおしました")
      break
    
if metal_monster_HP >0:
  print("メタルモンスターに逃げられました")

print(f"{i}「口ほどにもないやつめ、ふふ・・・」")