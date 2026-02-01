class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
    
        visited = [ [0]*cols for i in range(rows) ]
        def dfs(r,c):
            if r >= rows or r<0 or c>= cols or c< 0 or grid[r][c] == 0 or visited[r][c] == 1:
                return 0
            
            visited[r][c] = 1
            return dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        

        curr = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and visited[i][j] != 1:
                   curr = max(curr,dfs(i,j))
        
        return curr
