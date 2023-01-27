def solution(n):
    grid = []
    answer = []
    for i in range(n):
        temp =[0]*(i+1)
        grid.append(temp)
    insert_snail(n,grid)
    for elm in grid:
        answer+=elm
    
    return answer

def insert_snail(n,grid):
    dx = [1,0,-1]
    dy = [0,+1,-1] # 하 우, 좌상
    d = 0
    tx,ty= 0,0
    x,y = -1,0
    count = 1
    whole_num = 0
    for i in range(n,0,-1):
        for j in range(i):
            x,y = x+dx[d],y+dy[d]
            grid[x][y] = count
            count+=1
        d+=1
        d=d%3
    
     


if __name__=="__main__":
    n= 6
    sol = solution(n)
    print(sol)