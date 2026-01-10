# LeetCode 209 – Minimum Size Subarray Sum

# Used Sliding Window / Two Pointers technique.
# Maintain a window with left and right pointers and keep adding elements until the sum becomes ≥ target.
# Then shrink the window from the left to find the minimum length subarray while keeping sum ≥ target.
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        sumi = 0
        ans = len(nums)+1
        for j in range(len(nums)):
            sumi += nums[j]
            while sumi >= target:
                if ans == 0:
                    ans = j-i+1
                else:
                    ans = min(ans,j-i+1)
                
                sumi-=nums[i]
                i+=1
            
        return ans


        
