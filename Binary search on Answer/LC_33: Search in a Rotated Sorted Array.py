# (Approach):
# 1. Use "binary search" because the array is originally sorted, just rotated — so we can still achieve O(log n) time.
# 2. In every iteration, at least **one half (left–mid or mid–right) will be properly sorted**.
#    * If "nums[l] <= nums[mid]", left half is sorted.
#    * Else, right half is sorted.
# 3. Check whether the **target lies inside the sorted half’s range.
#    * If yes → move towards that half.
#    * If no → search in the other half.
# 4. Continue until you find the target or l > r.

# Key idea: *Identify the sorted half first, then decide direction.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
