


def cre(x):
    return x==x[::-1]

s= input()

L=[]
n=len(s)
for i in range(n):
    L.append([0]*n)

for i in range(n):
    L[i][i]=1

def fmax():
    for l in range(2,n+1):
        for st in range(n-l+1):
            end= st+l-1
            x= s[st:end+1]
            if x[0]==x[-1]:
                L[st][end]= L[st+1][end-1]+2
            else:
                L[st][end] = max(L[st][end-1],L[st+1][end])

fmax()
print(L[0][n-1])