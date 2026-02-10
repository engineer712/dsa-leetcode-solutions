#Approach: 
# This is a classic binary search prblm without any other extra logics..this is the core template for all problems relative to this pattern
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def valid(val,num):
            if val*val == num:
                return True
            
            return False


        low = 1
        high = num
        while low <= high:
            mid = (low + high) // 2
            if valid(mid, num):
                return True
                
            elif mid*mid > num:
                high = mid -1
            else:
                low = mid+1
        return False



        
