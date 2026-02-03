# Question:

# You are given an array `stones` where each element represents the weight of a stone. On each turn, select the two heaviest stones and smash them together:
# * If both stones have equal weight → both are destroyed.
# * If they have different weights → the smaller stone is destroyed and the larger stone becomes the difference of their weights.
# Continue this process until at most one stone remains. Return the weight of the last remaining stone, or `0` if no stones remain.

# Approach: 

# **Step 1:** Convert all stone weights to negative values(This helps simulate a **Max Heap** using Python’s Min Heap).
# **Step 2:** Use `heapify()` to convert the list into a heap in **O(n)** time.
# **Step 3:** While heap size is greater than 1:
# * Pop the largest stone.
# * Pop the second largest stone.
# **Step 4:** Compare both stones:
# * If equal → do nothing (both destroyed).
# * If different → push the difference back into heap.
# **Step 5:** After loop ends:
# * If heap has one element → return its positive value.
# * If heap is empty → return `0`.


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = [ -i for i in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap,-(first - second))

        return -heap[0] if heap else 0

            
        

        
        
