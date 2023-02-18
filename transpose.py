n = 5
count =1
graph = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        graph[i][j] = count
        count +=1

def printGrid(grid):
    global n
    for i in range(n):
        li = [format(elm,'02') for elm in grid[i]]
        print(li)
    print("\n")

def rotated(grid):
    global n 
    result = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-i-1] = grid[i][j]
    return result

def transpose(grid):
    global n 
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j], result[j][i]  = grid[j][i], grid[i][j]
    return result

def snail():
    global n 
    result = [[0]*n for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    d = 3
    count =1
    x,y= 0,0
    while (count <=n*n):
        result[x][y] = count
        nx,ny = x +dx[d], y+dy[d]
        if (0<=nx<n) and (0<=ny<n) and result[nx][ny]==0: 
            x,y =nx,ny
        else:
            d= (d+1)%4
            x,y = x+dx[d], y+dy[d]
        count+=1
    return result


printGrid(graph)

rot = rotated(graph)
print("\nrotated")
printGrid(rot)

sn = snail()
print("\n snail")
printGrid(sn)


tr = transpose(graph)
print("\n transpose")
printGrid(tr)