# read and prepare data
def mv(x):
    return x//2+1


n = int(input())

data=[]
for i in range(n):
    data.append(list(map(int,input().split()[1:])))
data.sort()

win_n=0
for i in range(n):
    data[i][-1]=mv(data[i][-1])
    win_n+=data[i][0]


def find():
    last=0
    for i in range(n):
        x=data[i]
        last += x[0]
        P=[]
        for k in range(last+1):
            P.append(list(L[k]))


        for j in range(x[0],last+1):
            if x[0]<=j:
                if P[j-x[0]][1]:
                    L[j][0]= P[j-x[0]][0]+ x[1]    # cộng giá trị
                    L[j][1]= 1                           # check
                    if P[j][1]:
                        L[j][0] = min(L[j][0],P[j][0])


L=[]
for i in range(win_n+1):
    L.append([0,0])
L[0][1]=1


find()


min_= L[-1][0]
for i in range(win_n//2+1,win_n+1):
    if L[i][1]:
        min_=min(min_,L[i][0])


print(min_)