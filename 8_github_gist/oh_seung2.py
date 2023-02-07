import sys
from collections import defaultdict

input = sys.stdin.readline

savings = int(input()) # length of rows
current_values = list(map(int, input().split()))
future_values = list(map(int, input().split()))
num_stocks = len(current_values)
min_stocks = sorted(current_values)[0]
max_num_of_stocks = savings // min_stocks

profit_values =[]
for i in range(num_stocks):
    profit_values.append([current_values, future_values[i]-current_values[i]])
    # current values, capacity

def knapsack(savings, profit_values):
    capacity = savings
    stocks = profit_values
    pack = []
    # stocks = [주식가격, 얻을 수 있는 마진]
    # 한개 샀을때
    capacity -= stocks[0][0]
    pack.append([stocks[0][1]])
    for i in range(max_num_of_stocks + 1): # 가질 수 있는 주식의 갯수
        if i == 0:
            pack[i].append(0)
        elif capacity > :



        for c in range(ca)
        pack.append([])
        a = max( stocks[i-1][1] + pack[i-1][capacity - stocks[i-1][0]], pack[i-1][capacity])

        for c in range(capactiy + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif stocks[i - 1][1] <= c:
                pack[i].append(
                    max(
                        stocks[i - 1][0] + pack[i - 1][c - stocks[i - 1][1]],
                        pack[i - 1][c]
                    ))
            else:
                pack[i].append(pack[i - 1][c])
    return pack[-1][-1]

# knapsack problem
