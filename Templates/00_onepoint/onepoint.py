from collections import deque

graph = []

def bfs_visited(graph, start, visited):
    """나동빈 「이것이 코딩테스트다」 스타일"""
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for w in graph[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = True


def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end =' ')
        for w in graph[v]:
            if not visited[w] :
                queue.append(w)
                visited[w] = True

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w, visited)



def dfs_visited(graph, v, visited):
    """나동빈 「이것이 코딩테스트다」 스타일"""
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs_visited(graph, i, visited)



if __name__=="__main__":
    
    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]
    visited = [False]*9

    dfs(graph,1, visited)