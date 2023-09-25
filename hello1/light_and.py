def light():
  x = int(input("number ? \n>>>"))

  switch_a = 1 < x
  switch_b = x > 2
  
  if switch_a and switch_b:
    print("light ON!")
  else:
    print("Light OFF...")

if __name__ == "__main__":
  light()