# page 45. 

from xml.dom.expatbuilder import ElementInfo


graph = [[1,3,5,8],[4,2,1,7],[4,3,2,3]]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

x,y = 0,0

def solution(x,y,cost):
    if (x,y) == (2,3):
        return cost
    else : 
        n_cost = -1
        for i in range(0,4):
            nx = x+dx[i]
            ny = y+dy[i]
            temp_x,temp_y = 0,0
            if 0<=nx<4 and 0<=ny<5:
                if n_cost == -1 or graph[nx][ny] < n_cost:
                    n_cost = graph[nx][ny]
                    temp_x,temp_y = nx,ny
                else : continue
        cost += n_cost
        sol = solution(x,y,cost)
    return sol 

def recursive_solution(cost, x,y):
    if (x,y) == (0,0):
        return graph[0][0]
    elif x == 0:
        return recursive_solution(cost, x, y-1) + graph[x][y]
    elif y == 0 :
        return recursive_solution(cost,x-1,y) + graph[x][y]
    else:
        sol_a = recursive_solution(cost, x, y-1)
        sol_b = recursive_solution(cost, x-1, y)
        cost += min(sol_a,sol_b) + graph[x][y]
    return cost

def bottom_up(cost,x,y):
    mem = [[0 for _ in range(4)] for _ in range(3)]
    print(mem)
    mem[0][0] = graph[0][0]
    for i in range(2):
        mem[i+1][0] = graph[i+1][0] + mem[i][0]
    for j in range(3):
        mem[0][j+1] = graph[0][j+1] + mem[0][j]
    for i in range(1,3):
        for j in range(1,4):
            mem[i][j] = min(mem[i-1][j], mem[i][j-1]) + graph[i][j]
    print(mem)

# page 130

#    mem[0][0]=
#   for i in range(0,3):

        
        
if __name__ == "__main__":
    print(recursive_solution(0,2,3))
    bottom_up(0,0,0)

    #print(solution(0,0,1))
    

