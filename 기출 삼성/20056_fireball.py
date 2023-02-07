import sys
from collections import deque, defaultdict
input = sys.stdin.readline
N, M, K =map(int, input().split())
grid = [[0]*N for _ in range(N)]
li = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    y = li[i][0]
    x = li[i][1]
    grid[y][x] +=1

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for i in range(M):
    r, c, s, m, d = li[j]
    y = li[i][0]
    x = li[i][1]
    grid[y][x] -=1

    ny = (y + dy[d] * s)% N
    nx = (x + dx[d] * s)% N
    grid[ny][nx] += 1
li =[]
for i in range(N):
    for j in range(N):
        if grid[i][j] >1:



    #    r, c, s, m, d
    (x+N) % N
    for j in range(len(li)):

        if grid[nr][nc]>1: