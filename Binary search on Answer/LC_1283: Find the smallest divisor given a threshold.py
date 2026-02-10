#This problem is most similar when compared to "koko eating bananas"
# ***instead of ceil(i/val) , we can use (i + val - 1)//val
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def isvalid(val):
            total = 0
            for i in nums:
                total += (i + val -1)//val
            if total <= threshold:
                return True
            return False
        low = 1
        high = max(nums)
        while low <= high:
            mid = (low + high)//2
            print("mid: ",mid)
            if isvalid(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
