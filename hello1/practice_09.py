arg = input("Please,input >>>")

def doublebox(arg):
  if arg == "":
    arg = input("引数を入力してください >>>")
  if arg != "":
    for i in range(2):
      print(arg)
      
doublebox(arg)