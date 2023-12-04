import sys
from collections import deque
#https://hose0728.tistory.com/67

dx = [-1, 0, 1, 0] # dx[0] = left dx[1] = right
dy = [0, -1, 0, 1] # dy[2] = UP  dy[3] = down


sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def sub(bd, cst, sx, sy, fl): #sx, sy :   # driver's first position
    if cst.get((sx, sy)) is not None:
        return sy, sy, fl
    queue = deque()
    nque = deque()
    point = []
    visit = {(sx, sy): 1}
    queue.append((sx, sy))
    while 1:
        while queue:
            x, y = queue.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if -1 < nx < n and -1 < ny < n and bd[nx][ny] == 0 and visit.get((nx, ny)) is None:
                    visit[(nx, ny)] = 1
                    if cst.get((nx, ny)) is not None:
                        point.append((nx, ny))
                    else:
                        nque.append((nx, ny))
        fl -= 1
        if fl < 0:
            return -1, -1, -1

        elif point: # point appended
            if len(point) > 1:
                point.sort()
            return point[0][0], point[0][1], fl

        else:
            queue = nque
            nque = deque()


def sub2(bd, fl, sx, sy, t_x, t_y):
    if sx == t_x and sy == t_y:
        return 0
    queue = deque()
    visit = {(sx, sy): 1}
    queue.append((sx, sy, 0))
    while queue:
        x, y, count = queue.popleft()
        if count > fl:
            return float('inf')
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < n and -1 < ny < n and bd[nx][ny] == 0 and visit.get((nx, ny)) is None:
                visit[(nx, ny)] = 1
                if nx == t_x and ny == t_y :
                    return count + 1
                queue.append((nx, ny, count + 1))

    return float('inf')


answer = 0
n, m, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
gsx, gsy = map(int, input().split())  # driver's first position

gsx -= 1
gsy -= 1
customer = {}  # dictionary

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    customer[(x1 - 1, y1 - 1)] = [x2 - 1, y2 - 1] # {(4, 3): [0, 5]}

while 1:
    px, py, fuel = sub(board, customer, gsx, gsy, fuel)
    if fuel < 0 :
        print(-1)
        break

    tx, ty = customer[(px, py)]
    cal = sub2(board, fuel, px, py, tx, ty)

    if cal > fuel:
        print(-1)
        break
    else:
        fuel += cal
        del customer[(px, py)]
        if not customer:
            print(fuel)
            break
        gsx = tx
        gsy = ty

