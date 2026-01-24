class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([])
        visited = set()
        dircs = [(1,0),(-1,0),(0,1),(0,-1)]
        def bfs(r,c):
            queue.append((r,c))
            visited.add((r,c))
            ans = 0
            while queue:
                ans+=1
                r1, c1 = queue.popleft()
                for dr,dc in dircs:
                    nr = r1+dr
                    nc = dc + c1
                    if 0<= nr < rows and 0<= nc < cols and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            return ans

        curr = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    curr = max(curr,bfs(i,j))
        
        return curr
