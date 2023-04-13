from collections import deque
graph = []
def bfs(start_v): # 알고리즘인터뷰 원본
    discovered =[start_v]
    queue = [start_v]
    while queue: 
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)

def bfs(start_v): # 알고리즘 인터뷰 deque 변형
    q = deque([start_v])
    discovered=[start_v]
    while q:
        v = q.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                q.append(w)

def bfs(graph,start, visited): # 나동빈 이것이 코테다
    q = deque([start])
    visited[start] = True
    while q :
        v = q.popleft()
        print(v,end=' ')        
        for w in graph[v]:
            if not visited[w]:
                q.append(w)
                visited[w]=True

def dfs_iterative(start_node,graph): # 파이썬 알고리즘 인터뷰 
    discovered = []
    stack = deque()
    stack.append(start_node)
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
                
    return discovered

def dfs_recursive(v,discovered=[]): # 파이썬 알고리즘 인터뷰
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = dfs_recursive(w,discovered)
    return discovered

def dfs(graph,v, visited): # 나동빈 이것이 코테다
    visited[v] = True
    print(v,end ='')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
    
