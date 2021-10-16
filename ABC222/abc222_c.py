n,m=map(int,input().split())

def sol(a,b):
    if a==b:
        return [0,0]
    elif (a=='G' and b=='C') or (a=='C' and b=='P') or(a=='P' and b=='G'):
        return [-1,0]
    elif (b=='G' and a=='C') or (b=='C' and a=='P') or(b=='P' and a=='G'):
        return [0,-1]

db=[]
for i in range(2*n):
    db.append([0,i+1,input()])

for i in range(m):
    for j in range(1,n+1):
        a=db[2*j-1-1][2][i]
        b=db[2*j-1][2][i]
        
        tmp=sol(a,b)
        db[2*j-1-1][0]+=tmp[0]
        db[2*j-1][0]+=tmp[1]
        
        db.sort()

for i in range(2*n): 
    print(db[i][1])
