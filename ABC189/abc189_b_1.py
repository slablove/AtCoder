N,X=map(int, input().split())

alcohol=0

for i in range(N):
  V,P = map(int, input().split())
  alcohol+=V*P 
  if 100*X<alcohol:
    print(i+1)
    exit()

print(-1)
