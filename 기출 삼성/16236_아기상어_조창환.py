from collections import deque
import sys
INF = 1e9 # 무한을 의미하는 10억
sys.stdin = open("16236_input.txt", "r")
input = sys.stdin.readline


n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
# array = map

now_size = 2
now_x,now_y = 0,0
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = j, i
            array[i][j] = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0] # 상좌하우


for i in range(4):
    nx = x + dx
    ny = y + dy
    if 0<=nx<n and 0<=ny<n:
        pass

def bfs(start_v, graph):
    q = deque()
    visited = [start_v]
    while q:
        v = q.popleft()
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                q.append(w)
