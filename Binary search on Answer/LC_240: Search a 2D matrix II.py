class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # We are starting from top-right element...
        low = 0
        high = cols-1
        while low>=0 and high >= 0 and low < rows and high < cols:
            if matrix[low][high] == target:
                return True
            # If current element is greater than target element then move left
            if matrix[low][high] > target:
                high -= 1
            # Else move down..i.e., to next row
            else:
                low += 1
        return False
