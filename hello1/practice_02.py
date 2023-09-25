'''暗号のヒントは BEAR の好物です'''

alphabet = "abcdefghijklmnopqrstuvwxyz"

a = alphabet[0]
b = alphabet[15]
c = alphabet[11]
d = alphabet[4]

code = a + b + c + d

#aple

result = input("Please, code \n>>>")

if code == result:
  print("Great!")
else:
  print("Boo")