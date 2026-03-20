class Solution(object):
    def minAbsDiff(self, grid, k):
        rows = len(grid)
        cols = len(grid[0])

        res = [[0] * (cols - k + 1) for u in range(rows - k + 1)]

        for i in range(rows - k + 1):
            for j in range(cols - k + 1):
                arr = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        arr.append(grid[r][c])
                if k == 1:
                    res[i][j] = 0
                    continue
                arr = sorted(set(arr))
                if len(arr) <= 1:
                    res[i][j] = 0
                    continue
                    
                mini = float('inf')
                for p in range(1,len(arr)):
                    mini = min(mini, arr[p] - arr[p-1])
                
                res[i][j] = mini

        return res
