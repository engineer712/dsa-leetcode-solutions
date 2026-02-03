# heap has an optimal time complexity of O(n log k) compared to sorting which has O(n logn).
# Python has some built-in methods like heappush,heappop which makes an array as min heap.
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heap = []
        for i in nums:
            heapq.heappush(heap,i)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

        
