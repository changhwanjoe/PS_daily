from collections import deque
graph = []
def bfs(v):
    visited =[v]
    stack = deque()
    stack.append(v)
    while stack:
        w = stack.popleft()
        for n in graph[w]:
            if w not in visited:
                stack.append(w)
                visited.append(w)


def dfs(start,graph, visited):
    q = deque([start])
    visited = [start]
    while q :
        v = q.popleft()
        for w in graph[w]:
            if w not in visited:
                q.append(w)
                visited.append(w)

def dfs(start,graph, visited):
    visited = []
    stack = deque([start])
    while stack:
        v = stack.pop()
        visited.append(v)
        for w in graph[v]:
            if w not in visited:
                stack.append(w)       

def dfs_iterative(start_node,graph):
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