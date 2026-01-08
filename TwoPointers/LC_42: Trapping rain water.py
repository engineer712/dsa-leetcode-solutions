# LeetCode 42 – Trapping Rain Water (Hard)

# You are given an array where each value represents the height of a bar.
# After raining, water can be trapped between taller bars.
# Your task is to calculate "total units of water trapped" between the bars.
# Water above any bar depends on the **minimum of the tallest bar on its left and right**.

# Example:
# [4,2,0,3,2,5] → Output: 9

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        leftmax = rightmax = 0
        water = 0
        while l<r:
            if height[l] <= height[r]:
                if height[l] > leftmax:
                    leftmax = height[l]
                else:
                    water += leftmax - height[l]
                l+=1
            else:
                if height[r] > rightmax:
                    rightmax = height[r]
                else:
                    water += rightmax - height[r]
                r-=1
        return water
