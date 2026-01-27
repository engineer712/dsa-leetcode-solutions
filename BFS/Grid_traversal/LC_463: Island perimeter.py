# Question

# Given a 2D grid where `1` represents land and `0` represents water, calculate the **perimeter of the island**.
# Each land cell contributes to the perimeter based on how many of its sides are exposed to water or the grid boundary.

#  Pattern Used ( NOT BFS/ DFS)

# **Grid Traversal with Directional Neighbor Checking**
# > This problem belongs to the grid-based problems category, commonly solved using BFS/DFS.
# > However, since traversal or visitation tracking is not required, a direct neighbor-counting approach is sufficient.

#  Core Idea

# * Traverse every cell in the grid.
# * For each land cell:
#   * Start with **4 sides**.
#   * Check its **4 adjacent neighbors** (up, down, left, right).
#   * For every adjacent land cell, **reduce the perimeter by 1** (shared edge).
# * Accumulate the total perimeter.


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        dircs = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans+=4
                    for r,c in dircs:
                        nr = i+r
                        nc = j+c
                        if 0<= nr< rows and 0<= nc < cols and grid[nr][nc] == 1:
                            ans-=1
        return ans

        
