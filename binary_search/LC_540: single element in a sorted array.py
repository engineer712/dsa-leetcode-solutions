#LeetCode 540 – Single Element in a Sorted Array

# Problem:
# Given a **sorted array** where every element appears **twice except one**, find the 
# single element in **O(log n)** time and **O(1)** space.

# Approach

# * Use **binary search**.
# * Before the single element, pairs start at **even indices**.
# * After it, pairs shift to **odd indices**.
# * Make `mid` even and compare with `mid + 1`.
# * If pair matches → go right, else → go left.


class Solution(object):
    def singleNonDuplicate(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if mid % 2:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        return nums[l]


If you want it **even shorter (one-screen README)** or **with comments removed**, tell me 👍
