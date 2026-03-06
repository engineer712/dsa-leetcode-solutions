# Approach:
# Here, instead of searching for elements which make up to 'x' , we instead search the maximum subarray containing elements with 'sum == total - x'.
# For this, we use sliding window pattern.


class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total = sum(nums)
        subarray = total - x
        if subarray < 0:
            return -1
        i = 0
        curr = 0
        ans = -1
        for j in range(0,len(nums)):
            curr += nums[j]
            while curr > subarray:
                curr -= nums[i]
                i+=1
            if curr == subarray:
                ans = max(ans,j-i+1)

        return  len(nums)- ans if ans != -1 else ans
