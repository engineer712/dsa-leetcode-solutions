# Approach – Binary Search on Answer:
# 1. The minimum capacity must be at least the maximum weight (otherwise we can’t ship the heaviest package).
# The maximum capacity can be sum of all weights (ship everything in one day).
# 2. Apply binary search between max(weights) and sum(weights) to find the minimum valid capacity.
# 3. For each mid (capacity), simulate shipping:
#     -> Keep adding weights to current load.
#     -> If adding a package exceeds capacity, increment day count and start new day.
#     -> Finally check if total days used ≤ given days.
# 4. If possible within given days → try smaller capacity (move left).
# Else → increase capacity (move right).


class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def satisfy(n, arr,days):
            day = 1
            curr_weight = 0
            for i in arr:
                if curr_weight + i > n:
                    day += 1
                    curr_weight = 0
                curr_weight += i
            return day <= days

        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = (l+r)//2
            if satisfy(mid,weights,days):
                r = mid - 1
            else:
                l = mid + 1
        return l
