import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx = [-1, 0 , 0 ,1]
dy = [0, 1, -1 ,0 ]

block = {'black':0,'rainbow':1,'normal':2}
normal_color = [1,2,3,4]
black = -1
rainbow = 0

dicovered = []
max_size= 0
max_rainbow_num = 0
for j in range(N):
    for i in range(N):
        if visited[i][j] == 1:
            continue
        elif ground[i][j] > 0:
            visited[i][j]= 1
            normal_block_color = ground[i][j]
            size, rainbow_num, discovered = dfs(i,j,normal_block_color,discovered)
            if size >=max_size or (max_size == size and rainbow_num>=max_rainbow_num):
                    max_x = j
                    max_y = i
        else:
            continue
def dfs(y,x,normal_num, discovered,cnt):
    if ground[y][x] > 0 :
    dfs(ny, nx, s)
    return cnt

def recursive_dfs(start_v
def dfs(start_v):
    discoverd = []
    discovered.append(start_v)
    stack =deque()
    stack.append(start_v)
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)

    return discovered
def recursvie_dfs(start_v,discovered=[]):
    discovered=[start_v]
    for w in graph[v]:
        recursvie_dfs(w, discovered)

    return discovered

    v = start_v
    if v not in discovered:
        discovered.append(v)
        for w in graph(v):
            recursvie_dfs(w, discovered)
    return discovered
def bfs(star_v):
    q = deque()
    discovered= []
    while q :
        v = q.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                q.append(w)



input = '''5 3
2 2 -1 3 1
3 3 2 0 -1
0 0 0 1 2
-1 3 1 3 2
0 3 2 2 1
'''