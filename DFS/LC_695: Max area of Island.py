class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        visited = [ [0]*cols for i in range(rows)]
        def dfs(r,c):
            if r >= rows or r<0 or c>= cols or c< 0 or grid[r][c] == 0 or visited[r][c] == 1:
                return 0
            
            visited[r][c] = 1
            a = dfs(r+1,c)
            b = dfs(r-1,c)
            c1 = dfs(r,c+1)
            d = dfs(r,c-1)
            return 1+ a + b + c1+ d
        

        curr = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and visited[i][j] != 1:
                   
                    curr = max(curr,dfs(i,j))
        
        return curr
