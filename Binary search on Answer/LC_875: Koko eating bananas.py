#Here, low i.e., minimum spped is taken as 1 because if we take '0' , the pile will be never finished.
# If we take greater than 1, the algorithm becomes more inefficient


class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def isvalid(num):
            hrs = 0
            for p in piles:
                hrs += (p + num - 1) // num
            return hrs <= h
            
        
        low = 1
        high = max(piles)
        
        while low <= high:
            mid = (low + high)//2
            if isvalid(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low 

        
