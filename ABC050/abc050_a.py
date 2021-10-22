line = input().split()
a,b,c = map(str,line)
d,e = int(a),int(c)

if b == "+":
  print(d+e)
else:
  print(d-e)
  
