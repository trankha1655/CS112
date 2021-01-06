# read and prepare data
def mv(x):
    return x//2+1


n = int(input())

data=[]
for i in range(n):
    inp= input().split()
    temp= list(map(int,inp[1:]))
    temp.append(inp[0])
    data.append(temp)
data.sort()

#win_n là tổng phiếu đại CT cả nước
win_n=0
for i in range(n):
    data[i][1]=mv(data[i][1])
    win_n+=data[i][0]

"""___________________________________________________"""
def find_track():
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
                    L[j][1]= 1          # check
                    #Trace[j]= x[0]
                    if P[j][1]:
                        if L[j][0] > P[j][0]:
                            L[j][0] = P[j][0]
                        else:
                            Trace[j] = [x[0], i]
                    else:
                        Trace[j] = [x[0],i]
"""___________________________________________________"""
#create L for dp
L=[]
for i in range(win_n+1):
    L.append([0,0])
L[0][1]=1

#create Trace array
Trace=['']*(win_n+1)
Trace[0]=[0,0]

#main
find_track()


#tìm số phiếu nhỏ nhất để win
way=0
min_= L[-1][0]
for i in range(win_n//2+1,win_n+1):
    if L[i][1]:
        if min_> L[i][0]:
            min_= L[i][0]
            way=i

while way >0:
    print(data[Trace[way][-1]][-1])
    way-= Trace[way][0]