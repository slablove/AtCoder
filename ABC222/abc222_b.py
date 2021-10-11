N,X=map(int, input().split())
A=list(map(int, input().split()))

score=[]

for i in range(N):
    if A[i] < X:
        score.append(A[i])

print(len(score))
