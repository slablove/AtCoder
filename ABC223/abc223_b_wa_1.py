a = input()
a = list(a)
a.sort()
c = ''.join(a)
print(c)
a.sort(reverse=True)
d = ''.join(a)
print(d)