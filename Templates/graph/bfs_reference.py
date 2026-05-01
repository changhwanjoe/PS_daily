"""
BFS / DFS 레퍼런스 구현 모음
- 다양한 출처(알고리즘 인터뷰, 이코테)의 구현을 비교 정리
"""
from collections import deque

graph = []


# ===== BFS =====

def bfs_basic(start_v):
    """알고리즘 인터뷰 원본 (deque 사용으로 최적화)"""
    discovered = {start_v}          # set 사용: in 연산 O(1)
    queue = deque([start_v])        # deque: popleft O(1)
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.add(w)
                queue.append(w)
    return discovered


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


# ===== DFS =====

def dfs_iterative(start_node, graph):
    """스택 기반 DFS (파이썬 알고리즘 인터뷰)"""
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


def dfs_recursive(v, discovered=None):
    """재귀 DFS (파이썬 알고리즘 인터뷰)"""
    if discovered is None:          # mutable default argument 방지
        discovered = []
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = dfs_recursive(w, discovered)
    return discovered


def dfs_visited(graph, v, visited):
    """나동빈 「이것이 코딩테스트다」 스타일"""
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs_visited(graph, i, visited)
