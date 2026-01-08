# LeetCode 128 - Longest Consecutive Sequence
# Pattern: Hash Set (Hashing)
#
# Problem:
# Given an unsorted array of integers, find the length of the longest
# sequence of consecutive numbers.
#
# Example:
# Input:  [100, 4, 200, 1, 3, 2]
# Output: 4   # because the sequence is 1,2,3,4
#
# Idea:
# - Store all numbers in a set for O(1) lookup.
# - Start counting only if (num - 1) is not in the set.
# - Expand the sequence using num + 1, num + 2, ...

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return 0
        freq = set(nums)
        ans = 0
        for num in freq:
            if num - 1 not in freq:
                val = num
                curr = 1
                while val + 1 in freq:
                    curr += 1
                    val += 1
                ans = max(ans,curr)
        return ans
