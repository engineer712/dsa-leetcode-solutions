# 1. The answer is always in the range **1 to n+1** where `n = len(nums)`.

# 2. Try to place each number `x` at index `x-1`
#    (i.e., `1` at index `0`, `2` at index `1`, …).

# 3. While traversing, swap until:
#    * the number is out of range (`<=0` or `>n`)
#    * OR it is already in its correct position.
# 4. After rearranging, scan the array:
#    the first index `i` where `nums[i] != i+1` → answer is `i+1`.
# 5. If everything is in place, answer is `n+1`.

# This is a classic **Cyclic Sort + In-place hashing** problem.

class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        i = 0

        while i < n:
            correct = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
