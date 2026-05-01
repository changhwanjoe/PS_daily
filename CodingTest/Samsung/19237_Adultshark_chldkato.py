import sys

sys.stdin = open("19237_input.txt", "r")
input = sys.stdin.readline

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())

a, shark = [], [[] for _ in range(m)]  # a[][] -> [상어의 크기, k] ,[[] [] [] [] [] [] []]
0for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(n):
        if a[i][j]: # not zero -> shark exists 
            shark[a[i][j]-1].extend([i, j]) #shark[0].extend([0,0])
            a[i][j] = [a[i][j], k]

d = list(map(int, input().split()))
for i in range(m):
    shark[i].append(d[i])

dir = [[] for _ in range(m)]
idx = -1
for i in range(4*m):
    if i % 4 == 0:
        idx += 1
    dir[idx].append(list(map(int, input().split())))

ans = 0
while True:
    ans += 1
    if ans == 1001:
        print(-1)
        break

    check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        if shark[i] != 0:
            x, y, d, flag = shark[i][0], shark[i][1], shark[i][2], 0
            for j in range(4):
                ndir = dir[i][d-1][j] # i 번째 상어가, d-1 향하고 있을때, 우선순위 차례대로
                nx, ny = x + dx[ndir], y + dy[ndir]
                if 0 <= nx < n and 0 <= ny < n:
                    if a[nx][ny] == 0: #냄새가 없다면,
                        flag = 1
                        break
            if flag == 0: #빈칸이 없으면, 
                for j in range(4):
                    ndir = dir[i][d-1][j] # new heading 내가 오른쪽가면 오른쪽 향하고 있고, 왼쪽가면 왼쪽 향하고 있음.
                    nx, ny = x + dx[ndir], y + dy[ndir]
                    if 0 <= nx < n and 0 <= ny < n:
                        if a[nx][ny][0] == i+1:
                            break

            if check[nx][ny]: #움직이려는데 상어가 있다?
                if check[nx][ny] < i+1: # 나보다 숫자 작은 상어가 있다면
                    shark[i] = 0 # 나는 죽음
                else:
                    shark[check[nx][ny]-1] = 0 #걔는 죽음
            else:
                check[nx][ny] = i+1 # 움직이는곳에 상어가 없다
                shark[i] = [nx, ny, ndir]

    for i in range(n): #모든 좌표에 대해,
        for j in range(n):
            if a[i][j]: #냄새가 존재하면, 냄새에서 1 뺌
                a[i][j][1] -= 1
                if a[i][j][1] == 0:
                    a[i][j] = 0

    for i in range(m): # 상어 지금 있는 자리에 냄새남김.
        if shark[i]:
            x, y = shark[i][0], shark[i][1]
            a[x][y] = [i+1, k]

    if shark.count(0) == m-1:
        print(ans)
        break