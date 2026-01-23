# BFS is a logical and efficient pattern for solving problems involving levels or time.
# Once the core BFS pattern is understood, many problems become easy to solve.
# LeetCode 994 (Rotting Oranges) and the below prblm are some good examples where BFS is used to simulate the spread minute by minute.


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        dircs = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()

        def bfs(r,c):
            q = deque([(r,c)])
            visited.add((r,c))
            while q:
                r1,c1 = q.popleft()
                for dr,dc in dircs:
                    nr = dr+r1
                    nc = dc+c1
                    if (0<= nr<rows and 0<= nc <cols and (nr,nc) not in visited and grid[nr][nc] =="1"):
                        visited.add((nr,nc))
                        q.append((nr,nc))


        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    ans += 1
                    bfs(i,j)
                  
        return ans

