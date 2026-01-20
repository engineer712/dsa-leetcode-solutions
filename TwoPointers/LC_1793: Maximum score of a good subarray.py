# LeetCode 1793 – Maximum Score of a Good Subarray

# You are given an integer array `nums` and an index `k`.
# A subarray is *good* if it contains index `k`.
# The score of a subarray is `min(subarray) * length(subarray)`; return the maximum score.

# Approach: 

# 1. Start with two pointers `i = j = k`, since every valid subarray must include `k`.
# 2. Maintain `mini`, the minimum value in the current window.
# 3. Expand the window one step at a time until it covers the whole array.
# 4. If one side is out of bounds, expand to the other side.
# 5. Otherwise, expand toward the side with the **larger adjacent value** to keep `mini` as large as possible.
# 6. After each expansion, update the score using
#    `mini × (j - i + 1)` and track the maximum.

class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = nums[k]
        mini = nums[k]
        i = j = k
        n = len(nums)

        while i > 0 or j < n - 1:
            if i == 0:
                j += 1
            elif j == n - 1:
                i -= 1
            elif nums[i - 1] < nums[j + 1]:
                j += 1
            else:
                i -= 1

            mini = min(mini, nums[i], nums[j])
            res = max(res, mini * (j - i + 1))

        return res

