# Approach:
# Traverse `nums2` and use a **stack** to keep elements whose next greater element is not yet found.
# For each element in `nums2`, compare it with the top of the stack.
# If the current element is greater, pop from the stack and store the current element as the **next greater element** in a dictionary.
# Push the current element into the stack after processing.
# If any elements remain in the stack, their next greater element does not exist, so they remain mapped to `-1`.
# Finally, build the result list by fetching answers for each element in `nums1` from the dictionary.

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = defaultdict(lambda:-1 )
        for i in nums2:
            while stack and stack[-1] < i:
                ans[stack.pop()] = i
            stack.append(i)
        return [ ans[i] for i in nums1]
