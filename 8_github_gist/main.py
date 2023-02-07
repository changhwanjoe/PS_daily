
graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]}

from bfs import bfs_iterative
from dfs import dfs_iterative, dfs_recusrive

visited = bfs_iterative(1,graph)
print(f"bfs = {visited}")

visited = dfs_iterative(1,graph)
print(f"dfs = {visited}")

visited= []
visited = dfs_recusrive(1,graph,visited)
print(f"rcs = {visited}")