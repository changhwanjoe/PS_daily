from collections import deque, defaultdict

def bfs_iterative(start_node,graph):
    discovered = [start_node]
    q = deque()
    q.append(start_node)
    
    while q:
        v = q.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                q.append(w)
    return discovered

if __name__ == "__main__":
    pass
            

