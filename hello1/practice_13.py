a = "Hello World"
b = "Lovely Thank You"
c = "Life is beautiful"
d = "Python is great"

list = [a,b,c,d]

def length():
  for i in range(len(list)):
    print(f"{list[i]}の長さは、{len(list[i])}です。")
    
length()