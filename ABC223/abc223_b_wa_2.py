import itertools
a_1 = input()

if len(a_1) >= 1 and len(a_1) <= 1000:
    b = list(min(itertools.permutations(a_1)))
    d = list(max(itertools.permutations(a_1)))
    c = ''.join(b)
    e = ''.join(d)
    print(c)
    print(e)
