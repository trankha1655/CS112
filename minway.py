
m,n= map(int,input().split())

L=[]
for i in range(m):
    L.append(list(map(int, input().split())))



zr= [0]*(n+1)
for i in range(m):
    L[i].insert(0,0)
L.insert(0,zr)

mod= 10**13+1
def road():
    for j in range(2, n + 1):
        if L[1][j]:
            L[1][j] = (L[0][j] + L[1][j - 1])% mod
    for i in range(2,m+1):
        for j in range(1,n+1):
            if L[i][j]:
                L[i][j]= (L[i-1][j]+L[i][j-1]) %mod



road()

print(L[-1][-1] %mod)
