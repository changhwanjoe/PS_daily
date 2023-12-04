import sys
from copy import deepcopy
import collections
from collections import deque
import heapq
import math

sys.stdin = open('17822_input.txt','r')
input = sys.stdin.readline


N, M, T = map(int, input().split()) # 2 ≤ N, M ≤ 50 1 ≤ T ≤ 50 # 4 4 1
#temp = list(map(int, input().split()))
#circle[0][0] , [0][1]

c = deque()
#circle =[[] for _ in range(N+1)]
circle = []
score = 0
circle.append([])
for i in range(1, N+1):
    c = deque()
    c.extend(list(map(int, input().split())))
    circle.append(c) # circle [1] [2]

def solution(x, d, k): # 2 0 1
    global N
    rest = N // x # N
    target = []
    for l in range(1, rest+1):
        rotation(x*l, d, k)

def rotation(tagrget_circle, d, k):
    global M
    global circle

    for _ in range(k):
        temp_circle = deepcopy(circle)

        if d == 0:
            nk = k
        else :
            nk = -k
        temp_circle[tagrget_circle].rotate(nk)
        # if d ==0: # 시계방향
        #     for i in range(M-1): # M = 4
        #         temp_circle[tagrget_circle][i+1] = circle[tagrget_circle][i]
        #     temp_circle[tagrget_circle][0] = circle[tagrget_circle][M-1]
        #
        # elif d == 1:
        #     for i in range(M-1): # M = 4
        #         temp_circle[tagrget_circle][i] = circle[tagrget_circle][i+1]
        #     temp_circle[tagrget_circle][M-1] = circle[tagrget_circle][0]

        circle = temp_circle

def subtract_number():
    exist_flag = False
    vertical_erase = []
    horizontal_erase = []
    global circle

    #껍질 늘어나면서 인접하다면
    for i in range(1, N + 1):
        for j in range(0,M): # 0, M-1
            if i < N:
                if circle[i][j] == circle[i+1][j]:
                    vertical_erase.append([i,j])
                    exist_flag= True
            if j < M-1:
                if circle[i][j] == circle[i][j+1]:
                    horizontal_erase.append([i,j])
                    exist_flag = True
            else:
                if circle[i][j] == circle[i][0]:
                    horizontal_erase.append([i, j])
                    exist_flag = True

    if exist_flag:  # 인접한 번호 있으면
        for dx,dy in vertical_erase:
            circle[dx][dy] = 0
            circle[dx+1][dy]=0
        for dx,dy in horizontal_erase:
            if dy+1 == M:
                circle[dx][dy] = 0
                circle[dx][0]= 0
            else:
                circle[dx][dy] = 0
                circle[dx][dy+1] = 0

    else : # 인접한거 없으면 전체 번호에 평균 +-
        for i in range(1,N+1):

            avg = sum(circle[i]) / len(circle[i])
            for j in range(len(circle[i])):
                if circle[i][j] > avg :
                    circle[i][j] -= 1
                elif circle[i][j] < avg :
                    circle[i][j] += 1

def find_score():
    global score, circle
    for i in range(1,N+1):
        score += sum(circle[i])

for j in range(T):
    xi, di, ki = map(int, input().split()) # 2 0 1
    solution(xi, di, ki)
    subtract_number()

find_score()
print(score)


# xi 배수, di방향 ki칸 회전
# di 0 : 시계 , 1 반시계

#인접한거 지우기, 없는경우 원판 평균 / 평균보다 큰수 -1 평균보다 작은수 +1


