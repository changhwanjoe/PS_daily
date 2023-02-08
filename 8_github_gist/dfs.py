from collections import deque

def dfs_recursive(v, graph,discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w, graph, discovered)
    return discovered

def dfs_iteration(start_v,graph):
    discovered =[]
    stack= [start_v]
    while stack :
        v = stack.pop()
        if v not in discovered:
            for w in graph[v]:
                stack.append(w)
    return discovered

