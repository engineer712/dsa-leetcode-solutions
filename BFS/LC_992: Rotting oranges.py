# Rotting Oranges — Question

# You are given a grid where `0` = empty, `1` = fresh orange, and `2` = rotten orange.
# Each minute, rotten oranges rot their adjacent (up, down, left, right) fresh oranges; return the minimum minutes needed or `-1` if impossible.

# Approach:(multi-source and level - order)

# 1. Use "multi-source BFS" by pushing all initially rotten oranges into a queue.
# 2. Count total **fresh oranges** to know when all are rotted.
# 3. Process the queue **level by level**, where each level represents **1 minute**.
# 4. For each rotten orange, rot its valid fresh neighbors and add them to the queue.
# 5. If fresh count becomes zero, return minutes; otherwise, return `-1`.


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1
        min = 0
        dircs = [(-1,0),(1,0),(0,1),(0,-1)]
        while queue and fresh >0:
            size = len(queue)

            for i in range(size):
                r, c = queue.popleft()
                for dr,dc in dircs:
                    rr = r+dr
                    cc = c+dc
                    if 0<= rr <rows and 0<= cc <cols and grid[rr][cc] == 1:
                        fresh-=1
                        grid[rr][cc] = 2
                        queue.append((rr,cc))
            min+=1
        return min if fresh == 0 else -1
            


        
