up = int(0.07*a)
down = int(0.07*a)
left_up = int(0.1*a)
left_down = int(0.1*a)
left = int(0.05*a)
right_up = int(0.01*a)
right_down = int(0.01*a)
up_up = int(0.02*a)
down_down = int(0.02*a)

N=int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int,input().split()))

rotation = ["left", "down", "right", "up"]
visited = [[0 for _ in range(N)] for _ in range(N)]

def main():
    s_x,s_y = N//2,N//2
    visited[s_x][s_y] = -1
    nx,ny =
    for i in range(N*N-1):
        rotate = rotation[i%4]
        jump_length =
        direction =


def tornado(x,y):
    rotation = ["left", "down", "right", "up"]
    move_twice = 0
    for i in range(N-1):
        rotation[(move_twice//2)%4]

def find_alpha(x,y,rotation):
    alpha_x = 0
    alpha_y = -1
    if rotation == "left":
        nx = x + alpha_x
        ny = y + alpha_y
    elif rotation == "up":
        nx = x + alpha_y
        ny = y - alpha_x
    elif rotation == "right":
        nx = x - alpha_x
        ny = y + alpha_y
    elif rotation == "down":
        nx = x - alpha_y
        ny = y + alpha_x
    return graph[nx][ny]

def move(x,y,rotation,alpha): # rotation should be left, up, right, down
    per_table = [0.05, 0.1, 0.1, 0.02, 0.7,0.7,0.02,0.01,0.01 ]
    move_x = [0, -1, +1, -2, -1, +1, +2, -1, +1]
    move_y = [-2, -1, -1, 0, 0, 0, 0, +1, +1]
    sum_alpha =0
    trash = 0
    for i in range(len(move_x)):
        if rotation == left:
            nx = x + move_x[i]
            ny = y + move_y[i]
        elif rotation == up :
            nx = x + move_y[i]
            ny = y - move_x[i]
        elif rotation == right :
            nx = x-move_x[i]
            ny = y+move_y[i]
        elif rotation == down :
            nx = x-move_y[i]
            ny = y+move_x[i]
        if not i ==len(move_x)-1:
            if not (0<= nx < N and 0<= ny <N):
                trash+= int(alpha * per_table[i])
            else:
                graph[nx][ny] = int(alpha * per_table[i])
                sum_alpha += graph[nx][ny]
        else:
            if not (0 <= nx < N and 0 <= ny < N):
                trash+= int(alpha * per_table[i])
            else:
                graph[nx][ny]= alpha-sum_alpha



        nx,ny = for i in range(len(move_x))
    rotation= [1,] # left, up, right, down
    left_up = x-1, y-1
    left_down = x+1, y-1
    right_up = x-1,y+1
    right_down = x+1, y+1
    up = x-1, y
    down = x+1, y
    up_up = x-2, y
    down_down = x+2, y
    alpha =
