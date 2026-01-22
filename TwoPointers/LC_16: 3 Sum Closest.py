# LeetCode 16 – 3Sum Closest

# Approach:
# Sort the array and fix one element at a time.
# For the remaining part, use two pointers to find the sum closest to the target.
# Update the closest sum whenever a better candidate is found.
# Adjust pointers based on whether the current sum is smaller or larger than the target.
# Return early if an exact match is found.


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]

                if abs(curr - target) < abs(closest - target):
                    closest = curr

                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
                else:
                    return curr  

        return closest
