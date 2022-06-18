S = input()
A = int(S[0:2])
B = int(S[2:4])
if 1 <= A <= 12:
  if 1 <= B <= 12:
    print("AMBIGUOUS")
  else:
    print("MMYY")
else:
  if 1 <= B <= 12:
    print("YYMM")
  else:
    print("NA")
