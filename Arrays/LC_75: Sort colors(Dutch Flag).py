#Here we use three pointers for three different elements usually this is called as "Dutch National Flag" theorem.

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #red = 0,white = 1,blue = 2
        low = 0
        mid = 0
        high = len(nums) -1
        while mid <= high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid], nums[low]
                low+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1
        return nums


