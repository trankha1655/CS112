


m,n= map(int,input().split())

L0= (n+1)*[0]


L=[]
for i in range(m):
    L= list(map(int,input().split()))+[0]

    for j in range(n):
        if L[j]:
            L0[j]= max(L0[j-1],L0[j]) +L[j]

        else:
            L0[j]=0
print(L0[n-1])
