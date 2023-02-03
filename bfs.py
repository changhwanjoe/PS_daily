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

def bfs(graph, start, visited):
    visited =[start]
    stack=deque([start])
    while stack:
        v = stack.popleft()
        for w in graph[v]:
            if w not in visited:
                stack.append(w)
                visited.append(w)
    return visited


