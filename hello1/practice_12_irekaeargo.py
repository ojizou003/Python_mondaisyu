def rangef(start=0, stop=None, step=1):
  if stop==None:
    start,stop = 0,start
  while start < stop:
    yield start
    start += step

for i in rangef(10):
    print(i, "Hello World")
  