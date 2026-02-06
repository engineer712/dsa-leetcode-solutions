#This is classic DFS problem with slight logic building..
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        total = 0
        sx = sy= 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != -1:
                    total += 1
                if grid[i][j] == 1:
                    sx, sy = i, j

        def dfs(i,j,remain):
            nonlocal ans
            if i<0 or j<0 or i>= rows or j>= cols or grid[i][j] == -1:
                return
            if grid[i][j] == 2 and remain == 1:
                ans+=1
                return

            temp = grid[i][j]
            grid[i][j] = -1

            dfs(i+1,j,remain-1)
            dfs(i-1,j,remain-1)
            dfs(i,j+1,remain-1)
            dfs(i,j-1,remain-1)

            grid[i][j] = temp
        dfs(sx,sy,total)
        return ans
