"""
        LeetCode 15 - 3Sum

        Two Pointers Pattern:
        1. Sort the array
        2. Fix one element and use two pointers on the rest
        3. Skip duplicates to avoid repeated triplets
"""
class Solution(object):
    def threeSum(self, nums):

        nums.sort()
        result = []

        for i in range(len(nums)):
            # skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # skip duplicate left values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # skip duplicate right values
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
