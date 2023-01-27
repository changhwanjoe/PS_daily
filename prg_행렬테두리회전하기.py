#https://school.programmers.co.kr/learn/courses/30/lessons/77485?language=python3
from collections import deque
import copy
def solution(rows, columns, queries):
    answer = []
    grid = [[0]*columns for _ in range(rows)]
    org_grid = [[0]*columns for _ in range(rows)]
    count = 1
    for i in range(rows):
        for j in range(columns):
            grid[i][j] = count
            count +=1 
    org_grid = copy.deepcopy(grid)
    for elm in queries:
        x1,y1,x2,y2 = elm
        temp_answer = rotation(x1,y1,x2,y2,grid)
        answer.append(temp_answer)

    return answer

def rotation(x1,y1,x2,y2,grid):
    row_dif = x2-x1
    col_dif = y2-y1
    li_temp = []
    d = deque()
    for i in range(col_dif):
        d.append(grid[x1-1][(y1-1)+(i)])
    temp_y = (y1-1)+(i) +1 
    for j in range(row_dif):
        d.append(grid[(x1-1)+(j)][temp_y])
    temp_x = (x1-1)+(j) +1
    for k in range(col_dif):
        d.append(grid[temp_x][temp_y-k])
    temp_y = temp_y-k -1 
    for l in range(row_dif):
        d.append(grid[temp_x-l][temp_y])

    d.rotate(1)
    rotated = []
    for elm in d:
        rotated.append(elm)
    rotated.sort()
    min_n = rotated[0]
    for i in range(col_dif):
        grid[x1-1][(y1-1)+(i)] = d.popleft()
    temp_y = (y1-1)+(i) +1 
    for j in range(row_dif):
        grid[(x1-1)+(j)][temp_y] = d.popleft()
    temp_x = (x1-1)+(j) +1
    for k in range(col_dif):
        grid[temp_x][temp_y-k] = d.popleft()
    temp_y = temp_y-k -1 
    for l in range(row_dif):
        grid[temp_x-l][temp_y] = d.popleft()
    return min_n

def check_min(org_grid,grid,rows, columns):
    dif_list = []
    for i in range(rows):
        for j in range(columns):
            if org_grid[i][j] != grid[i][j]:
                dif_list.append(grid[i][j])
    dif_list.sort()
    return dif_list[0]



if __name__=="__main__":
    rows,columns,queries=6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]	
    sol = solution(rows, columns, queries)
    print(sol)