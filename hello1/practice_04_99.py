''' 九九 - 入れ子のfor文のアルゴリズム - '''

number =list(range(1,10))

for i in number:
  print(f"{i}の段")
  
  for j in number:
    result = i * j
    print(f"{i} ✕ {j} = {result}")
    