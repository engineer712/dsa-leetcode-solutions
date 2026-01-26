# Approach:(multi source bfs)

# * Create a result matrix filled with `-1`
# * Push **all `0` cells** into a queue and mark their distance as `0`
# * Run **BFS** in 4 directions
# * For every unvisited neighbor, set
#   `distance = current + 1` and push to queue
# * BFS guarantees the **nearest 0 distance**
# **Key idea:** *Multi-source BFS from all zeros*

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        
        dircs = [(1,0),(-1,0),(0,1),(0,-1)]
        result = [[-1] * cols for i in range(rows)]
        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    result[i][j] = 0
                    
        while queue:
            r,c = queue.popleft()
            for dr,dc in dircs:
                nr = r+dr
                nc = c+dc
                if 0<= nr < rows and 0<= nc < cols and result[nr][nc] == -1:
                    result[nr][nc] = result[r][c] + 1
                    queue.append((nr,nc))
        return result
