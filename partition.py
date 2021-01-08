#n = int(input())
mod =10**17+3
n=6000
path="C:/Users/phamt/PycharmProjects/22_12_2020/choi_do.py"

L= [1]*(n+1)

def dp():
    for x in range(2,n+1):
        for i in range(x,n+1):
            k=0
            if i>=x:
                k= L[i-x]
            L[i] =  (L[i] + k) % mod


f= open(path,"w")

dp()
inp= "n = int(input())\n"
lstr= "L=[" +str(L[0])

for k in range(1,len(L)):
    lstr= lstr+ ", " + str(L[k])
lstr+=']\n'

strans= "print(L[n])"

f.write(inp)
f.write(lstr)
f.write(strans)

f.close()


