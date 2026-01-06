class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        i = 0
        n = len(nums)
        while i<n:
            crct = nums[i]-1
            if crct<n and nums[i]!= nums[crct]:
                nums[i],nums[crct] = nums[crct],nums[i]
            else:
                i+=1
        for i in range(0,n):
            if i != nums[i]-1:
                res.append(nums[i])
        return res
