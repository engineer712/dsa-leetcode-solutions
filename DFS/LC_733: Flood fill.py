#  LeetCode 733 Flood Fill

# 1. Store the starting pixel’s color ('old').
# 2. If 'old' is the same as 'Color', return the image immediately.
# 3. Start DFS from the given cell `(sr, sc)`.
# 4. For each cell, check bounds and ensure its color matches 'old'.
# 5. Recolor the cell to 'Color' and continue in 4 directions (up, down, left, right).


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        old = image[sr][sc]
        if old == color:
            return image
        
        rows , cols = len(image), len(image[0])
        def dfs(r,c):
            if r<0 or c<0 or r>= rows or c>= cols:
                return
            if image[r][c] != old:
                return
            image[r][c] = color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        dfs(sr,sc)
        return image
