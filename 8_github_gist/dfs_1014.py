from typing import Deque


def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            recursive_dfs(w,discovered)
    return discovered

def dfs_with_iteration(start_v):
   discovered =[]
   q = Deque()
   stack= [start_v]
   while stack :
       v = stack.pop()
       for w in graph[v]:
            if not w in discovered:
                stack.append(w)
    return discovered


