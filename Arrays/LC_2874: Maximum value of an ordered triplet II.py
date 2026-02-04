# Approach:
# Use prefix and suffix maximum arrays.
# For each middle index `j`, take the maximum value before it (`prefix_max[j-1]`) and after it (`suffix_max[j+1]`) and compute
# ((prefix_max[j-1] - nums[j]) X suffix_max[j+1]).
# Track the maximum result.

class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        prefix_max = [0] * n
        suffix_max = [0] * n
        prefix_max[0]  = nums[0]
        suffix_max[n-1] = nums[n-1]
        i = n-2
        while i >= 0:
            suffix_max[i] = max(suffix_max[i+1],nums[i])
            i-=1
        for j in range(1,n-1):
            prefix_max[j] = max(prefix_max[j-1],nums[j])
            val = (prefix_max[j-1] - nums[j])*suffix_max[j+1]
            ans = max(ans,val)
        return ans


        
