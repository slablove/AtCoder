text = input().split()

if text[1] == '+':
  print(int(text[0]) + int(text[2]))
else:
  print(int(text[0]) - int(text[2]))
