graph = [[0]*5 for _ in range(4)]
answer = 0
def dfs(x,y,graph):
    global answer
    if 0<=x<3 and 0 <= y <4 and graph[x][y]==0 :
        graph[x][y] = 1
        for i in range(4):                
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            answer +=1 
    




            
    