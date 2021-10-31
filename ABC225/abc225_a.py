s = input()
if len(s)==3:
  if s[0]==s[1]==s[2]:
    print(1)
  elif s[0]==s[2] and s[0] != s[1]:
    print(3)
  elif s[0]==s[1] and s[0] != s[2]:
    print(3)
  elif s[1]==s[2] and s[0] != s[1]:
    print(3)
  elif s[0] != s[1] != s[2]:
    print(6)
