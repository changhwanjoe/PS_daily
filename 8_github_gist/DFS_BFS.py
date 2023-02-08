#page325
from collections import deque
graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]}

def dfs(graph,v, visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


def recursive_dfs(v, discovered = []): 
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered

def iterative_dfs(start_v): # DFS with stack
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

def bfs(graph,start,visited):
    queue = deque([start])    
    visited[start]=True
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True

def iterative_bfs(start_v): #BFS with queue
    discovered  = start_v
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered


                