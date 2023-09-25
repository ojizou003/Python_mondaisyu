def f(arg):
  word = f"Hello {arg}!"
  # print(arg)
  return word

def hello():
  x = input("please,name \n>>>")
  y = f(x)
  # print(y)
  return y

if __name__ == "__main__":
  result = hello()
  print(result)

