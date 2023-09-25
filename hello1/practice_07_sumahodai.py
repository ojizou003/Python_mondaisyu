time = int(input("今月の通話時間は何分ですか？ \n>>>"))

def calc_payment():
  payment = 5000+10*time  #固定料金5000
  print(f"今月のスマホ代は{payment}円です。")

calc_payment()