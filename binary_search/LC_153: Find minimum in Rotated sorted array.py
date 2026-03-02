# Approach:

# 1. The array is sorted but rotated, so one half is always sorted.
# 2. Use **binary search** to find the minimum in O(log n).
# 3. Compare `nums[mid]` with `nums[r]`:
#    * If `nums[mid] < nums[r]` → minimum is in left half (including mid), so `r = mid`.
#    * Else → minimum is in right half, so `l = mid + 1`.
# 4. When `l == r`, that element is the minimum.
# 5. Return `nums[l]`.


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <r:
            mid = (l+r)//2
            if nums[mid] < nums[r]:
                r = mid 
            else:
                l = mid+1
        return nums[l]
