N, P = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans += a[i] < P
print(ans)
