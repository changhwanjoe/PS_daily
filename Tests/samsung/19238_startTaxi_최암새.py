'''
https://chldkato.tistory.com/184
https://www.acmicpc.net/problem/19238 -> 문제 '''

from collections import deque
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs1(x, y):
    global fuel
    q1.append([x, y])
    c1[x][y], cnt = 1, 0
    while q1:
        qlen = len(q1)
        p = []
        cnt += 1
        if cnt >= fuel:
            return 0
        for _ in range(qlen):
            x, y = q1.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if a[nx][ny] != -1 and c1[nx][ny] == 0: # c1 == 0 not visited
                        if a[nx][ny] > 0:
                            p.append([nx, ny])
                        q1.append([nx, ny])
                        c1[nx][ny] = 1
        if p:
            break

    if not p:
        return 0

    fuel -= cnt
    p = sorted(p)
    x, y = p[0]
    res = bfs2(x, y, a[x][y])
    if res == 0:
        return 0

    length, nx, ny = res
    fuel += length
    a[x][y] = 0
    return nx, ny


def bfs2(x, y, idx): #고객 위치, 고객 idx 에서 목적지까지의 거리.
    q2.append([x, y])
    c2[x][y] = 0
    while q2:
        x, y = q2.popleft()
        if c2[x][y] >= fuel:
            return 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n: # 맵안에 있다면
                if a[nx][ny] != -1 and c2[nx][ny] == -1: #벽이 아니고, not visitied(-1) 이면.,
                    q2.append([nx, ny])
                    c2[nx][ny] = c2[x][y] + 1 # 거리값 넣음.
                    if [nx, ny] == d[idx]: # 좌표가 destination이라면,
                        return c2[nx][ny], nx, ny  # return 목적지까지의 거리, 목적지의 위치
    return 0

n, m, fuel = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(n):
        if a[i][j] == 1:
            a[i][j] = -1  # 벽을 -1로 채움.

x, y = map(int, input().split()) # driver's first position
x -= 1
y -= 1

d = [[] for _ in range(m + 1)]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    a[x1 - 1][y1 - 1] = i + 1 # passeneger map
    d[i + 1] = [x2 - 1, y2 - 1]  # destination map


for _ in range(m):
    q1, c1 = deque(), [[0 for _ in range(n)] for _ in range(n)]
    q2, c2 = deque(), [[-1 for _ in range(n)] for _ in range(n)]

    if a[x][y] > 0:
        res = bfs2(x, y, a[x][y])
        if res == 0:
            print(-1)
            sys.exit()
        length, nx, ny = res #목적지 거리, 목적지 위치.
        if length > fuel:
            print(-1)
            sys.exit()
        fuel += length
        a[x][y] = 0
        x, y = nx, ny # 목적지 위치.
        continue

    res = bfs1(x, y) #목적지에서 새로운 고객 찾기.
    if res == 0:
        print(-1)
        sys.exit()
    else:
        x, y = res
print(fuel)