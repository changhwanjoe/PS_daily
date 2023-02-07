#https://chldkato.tistory.com/133
import sys
from copy import deepcopy

sys.stdin = open("17825_input.txt", "r")
input = sys.stdin.readline
sys.stdin = open("17825_input.txt", "r")

a = [0 for _ in range(33)] # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(21):
    a[i] = i+1 # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a[21] = 21
a[22], a[23], a[24] = 23, 24, 30
a[25], a[26] = 26, 30
a[27], a[28], a[29] = 28, 29, 30
a[30], a[31], a[32] = 31, 32, 20

#index    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,//  22, 23, 24,// 25, 26, //27, 28, 29, /30, 31, 32/, 33]

 #a       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,//  21, 23, 24,// 30, 26, //30, 28, 29, /30, 31, 32/, 20]
#plus =[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38,40,//  0,  13, 16, //19, 22,// 24, 28, 27, /26, 25, 30/, 35]
move_in = [0 for _ in range(16)]
move_in[5], move_in[10], move_in[15] = 22, 25, 27

plus = [0 for _ in range(33)]
for i in range(1, 21):
    plus[i] = i * 2
plus[22], plus[23], plus[24] = 13, 16, 19
plus[25], plus[26] = 22, 24
plus[27], plus[28], plus[29] = 28, 27, 26
plus[30], plus[31], plus[32] = 25, 30, 35
print(plus)

def dfs(dice_index, ans):
    global max_ans
    if dice_index == 10:
        max_ans = max(max_ans, ans)
        return

    for i in range(4):
        x, x0, move = chess[i], chess[i], dice[dice_index]

        if x == 5 or x == 10 or x == 15:
            x = move_in[x]
            move -= 1

        if x + move <= 21:
            x += move
        else:
            for _ in range(move):
                x = a[x]

        if c[x] and x != 21:
            continue

        c[x0], c[x], chess[i] = 0, 1, x
        dfs(dice_index + 1, ans + plus[x])
        c[x0], c[x], chess[i] = 1, 0, x0

dice = list(map(int, input().split()))

chess = [0 for _ in range(4)]
c = [0 for _ in range(33)] # 해당 지점 말이 있느지

max_ans = 0
dfs(0, 0)
print(max_ans)