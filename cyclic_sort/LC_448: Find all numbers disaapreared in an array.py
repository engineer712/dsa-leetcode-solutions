# 448. Find All Numbers Disappeared in an Array — Cyclic Sort

# Rearrange numbers so that nums[i] = i+1 whenever possible.
# All indices where this condition fails represent missing numbers.


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            crct = nums[i]-1
            if nums[i] != nums[crct]:
                nums[i],nums[crct] = nums[crct],nums[i]
            else: 
                i+=1
        ans = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans

        
