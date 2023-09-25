time={"たんじろう":350,"ねずこ":0,"あがつま":2000,"いのっち":10}

def payfor():
  for key,value in time.items():
    payment = 5000+10*value  #固定料金5000
    print(f"今月の{key}のスマホ代は{payment}円です。")

payfor()