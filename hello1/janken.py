# janken.py

import random as rd

LIST = ["goo", "choki", "par"]

def janken():
  man = input("goo choki par ? \n>>>")
  pcs = rd.choice(LIST)
  print(f"Your {man}! vs PCsan {pcs}!")
  
  goo_win = man == "goo" and pcs == "choki"
  chk_win = man == "choki" and pcs == "par"
  par_win = man == "par" and pcs == "goo"
    
  goo_lose = man == "goo" and pcs == "par"
  chk_lose = man == "choki" and pcs == "goo"
  par_lose = man == "par" and pcs == "choki"
  
  if goo_win or chk_win or par_win:
    print("you win !")
    for i in range(10):
      coin = rd.randint(2,20)
      print(coin)
    print(f"You get {coin} coins !")
  elif goo_lose or chk_lose or par_lose:
    print("you lose...")
  else:
    print("even..")
    janken()
    
if __name__ == "__main__":
  janken()
