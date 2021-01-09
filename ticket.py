
import random as rd

rd.seed()
''' khởi tạo dữ liệu
____________________________________________________'''
#hàm rand() :D
def rand():
    return rd.random()+0.0134*rd.random()*rd.randint(-1,1)+0.528

# init n
n= rd.randint(0,10000) +1000

# init thời gian mua vé của n người
buy_time=[]


temp = []  #thời gian mua 1 vé
temp2= []  #--------------2 vé
temp3= []  #--------------3 vé

for i in range(n):
    temp.append(rd.randint(1,100000))
    temp2.append(round(temp[-1] * 2 * rand()))
    temp3.append(round(temp[-1] * 3 * rand()))

buy_time= [temp] +[temp2]+[temp3]


#constant
max_cost= 1000001



''' phần giải
-------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------'''

# tạo mảng cost với shape = 1*n
'''cost[i] là thời gian phải tốn nhỏ nhất mua cho người thứ i
=> đáp án bài toán là cost[n]
   
'''
cost=[0]*n


# và khởi tạo những giá trị đầu tiên


cost[0]=  buy_time[0][0]
cost[-2]= max_cost


'''Phần giải thuật'''
'''giải thích công thức:

ví dụ ta có tính được cho tới cost[5] và việc tiếp theo phải tính cost[6]

người thứ 6 có 3 quyết định:
1. người thứ 5 mua giùm: 
                       
                        Công thức:   ans1 = cost[4] + buy_time[1][5]  
                        
Giải thích:  nếu người t5 chọn mua 2 vé (buy_time[1][5] có nghĩa là người t3 đã có vé rồi (cost[3])


2. người t4 mua giùm :   
                        CT: ans2 = cost[3] + buy_time[2][4]
        
Giải thích:  nếu người t4 chọn mua 3 vé (buy_time[2][4] có nghĩa là người t3 đã có vé rồi (cost[3])


3. mua cho bản thân :    
                        CT: ans3 = cost[5] + buy_time[0][6] 
                        
Giải thích:  nếu người t6 chọn tự mua  (buy_time[0][6] có nghĩa là người t5 đã có vé rồi (cost[5])
        
                        => cost[6] = min (ans1, ans2, ans3)
    


'''


def dp():
    for i in range(1,n):
        ans1 = cost[i-2] + buy_time[1][i-1]  # nhờ người i-1 mua giùm 2 vé
        ans2 = cost[i-3] + buy_time[2][i-2]  # nhờ người i-2 mua giùm 3 vé
        ans3 = cost[i - 1] + buy_time[0][i]  # tự mua
        cost[i] = min(ans1,ans2,ans3)        # nào ít tốn kém nhất lấy


dp()

print(cost[-1])