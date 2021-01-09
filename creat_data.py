import random as rd

rd.seed()

# hàm rand() :D

# init n

def rand():
    return rd.random() + 0.0134 * rd.random() * rd.randint(-1, 1) + 0.528
n = 10000100
# init thời gian mua vé của n người
buy_time = []

temp = []  # thời gian mua 1 vé
temp2 = []  # --------------2 vé
temp3 = []  # --------------3 vé

max_cost = 300
for i in range(n):
    temp.append(rd.randint(1, max_cost-100))
    temp2.append(round(temp[-1] * 2 * rand()))
    temp3.append(round(temp[-1] * 3 * rand()))

buy_time = [temp] + [temp2] + [temp3]


cost = [0] * n

# và khởi tạo những giá trị đầu tiên

cost[0] = buy_time[0][0]
cost[-2] = max_cost*3

def dp(x):
    cost[0] = buy_time[0][0]
    cost[-2] = max_cost

    for i in range(1, x):
        ans1 = cost[i - 2] + buy_time[1][i - 1]  # nhờ người i-1 mua giùm 2 vé
        ans2 = cost[i - 3] + buy_time[2][i - 2]  # nhờ người i-2 mua giùm 3 vé
        ans3 = cost[i - 1] + buy_time[0][i]  # tự mua
        cost[i] = min(ans1, ans2, ans3)  # nào ít tốn kém nhất lấy




import cProfile as cp
import pstats
import io

pr = cp.Profile()
with open('test.txt', 'w+') as f:
    for i in range(1000000,10000001,225000):
        pr.enable()

        my_result = dp(i)

        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
        ps.print_stats()


        f.write(s.getvalue())
        print(i)