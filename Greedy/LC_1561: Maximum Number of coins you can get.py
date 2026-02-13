# Approach:
# Step 1 — Sort the piles
# Sort the array so coins are arranged from smallest → largest.
# Step 2 — Understand selection pattern**
# After sorting:
# * Friend takes largest
# * You take second largest
# * Bob takes smallest
#   Repeat this for every 3 piles → So pick every **2nd element** from the last `2/3` part.
# Step 3 — Sum your coins
# Start from index `n // 3` and keep adding every 2nd pile till end.
#Take a pen and paper and observe the pattern of selection of numbers after sorting the pile


class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n = len(piles)
        return sum([piles[i] for i in range(n//3, n, 2)])

