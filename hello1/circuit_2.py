A = "Hello World"
B = "Hello Python"
C = "Hello "

lst = [A, B, C]

def circuit_2(arg=None):
  global C
  C += arg
  
  result = A and B or C
  for i in lst:
    print(result is i)
    
  return result
  
y = circuit_2("BEAR")

print(y)
