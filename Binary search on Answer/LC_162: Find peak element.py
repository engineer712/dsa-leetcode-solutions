# An element is called as peak element if and only if both the left and right of that numbers are less than that number
# To solve this problem efficiently think of a mountain having peak
# Peak elements 'left subarray' is increasing and 'right sub array' is decreasing...
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        low = 0
        high = len(nums)-1
        while low < high:
            mid = (low+high)//2
            # If "mid+1" element is greater than "mid" it means that the peak element is to the right side of the array
            if nums[mid]< nums[mid+1]:
                low = mid +1
            
            else:
                high = mid 
        
        return low
