


import numpy as np

path= 'test.txt'

f= open(path,'r')
filt1=f.read().split('function calls in')[1:]

print(len(filt1))
filt2=[]
for x in filt1:
    filt2.append(float(x.split('seconds')[0]))

n=[]
for i in range(1000000,30000001,725000):
    n.append(i)

row1= np.asarray(n).reshape((1,-1))
row2= np.asarray(filt2).reshape((1,-1))

data= np.concatenate((row1,row2))


print(data)
np.savetxt('output.txt',data)
