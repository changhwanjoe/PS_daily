from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs2(i,j):
            if not (0<=i<len(grid) and 0<=j<len(grid) and grid[i][j] ==1 ):
                return 
            grid[i][j]= 0
            dfs2(i+1,j)
            dfs2(i-1,)
            
        
        def dfs(i, j):
            # 더이상 따잉 아닌 경우 종료 
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return # 탈출조건

            grid[i][j] = 0 # 한번 방문한 곳은 지워버림. 
            #동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count


'''
grid = [
  ["1","1","1","1","0"], # grid[0][0],grid[0][1]
  ["1","1","0","1","0"], # grid[1][0]
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]'''
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


a = Solution()
result = a.numIslands(grid)
print(result)