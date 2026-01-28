class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        ans = nums[n-1]
        for i in range(0,n-k+1):
            ans = min(ans, nums[i+k-1] - nums[i])
        return ans
