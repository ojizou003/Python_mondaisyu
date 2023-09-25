A = "Hello World"
B = "Hello Python"
C = "Hello "

def circuit(arg=None):
  global C
  C += arg
  
  result = A and B and C
  return result

y = circuit("BEAR")

print(y)
