import sys
#https://hose0728.tistory.com/39
import heapq
import collections
# dfs 이용

sys.stdin = open("17825_input.txt", "r")
input = sys.stdin.readline

def solution(count, sub, position):
    global answer
    if count == 9 and answer!= 0:
        if sub+40 < answer:
            return
    elif count == 10:
        if answer < sub:
            answer = sub
        return
    for i in range(4): # 네개의 말에 대하여,
        x, y = position[i] # 말 포지션  : position [[0, 0], [0, 0], [0, 0], [0, 0]]
        if x== 4 and y== 4:
            continue
        nx, ny = position[i]
        if x == 0: # at the start location
            if y == 5 :
                nx = 1
                ny= -1
            elif y== 10:
                nx = 2
                ny = -1
            elif y== 15:
                nx =3
                ny = -1
            elif y ==20 :
                nx =4
                ny =3

        ny += dices[count]
        if nx == 0 and ny >=20:
            nx = 4
            if ny == 20 :
                ny = 3
            else:
                ny =4

        elif 0< nx < 4 and ny > len(map1[nx]) -1 :
            ny -= len(map1[nx])
            nx = 4

        elif nx ==4 and ny >4:
            ny =4

        if map1[nx][ny] != 0 and [nx, ny ] in position:
            continue
        position[i] = [nx, ny]
        solution(count +1, sub+map1[nx][ny], position)
        position[i] = [x,y]

answer = 0
dices = list(map(int, sys.stdin.readline().split()))
map1 =  [[], [13,16,19], [22,24], [28,27,26], [25,30,35,40,0] ]
#[[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40], [13, 16, 19], [22, 24], [28, 27, 26], [25, 30, 35, 40, 0]]

for i in range(21):
    map1[0].append(2*i)

stack = [[0,0,[[0,0] for _ in range(4)],[0]*4]] # [[0, 0, [[0, 0], [0, 0], [0, 0], [0, 0]], [0, 0, 0, 0]]]
solution(0,0, [[0, 0] for _ in range(4)]) # (0, 0, [[0, 0], [0, 0], [0, 0], [0, 0]])
print(answer)