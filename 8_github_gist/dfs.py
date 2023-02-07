from collections import deque

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

def dfs_recusrive(v,graph,discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = dfs_recusrive(w,graph,discovered)
    return discovered

    