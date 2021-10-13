a,b = map(int, input().split())
c = map(int, input().split())
print(sum(x < b for x in c))
