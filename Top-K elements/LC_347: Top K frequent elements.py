# Problem:
# Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. The answer can be returned in any order.

# Approach (HashMap + Min Heap):    
# 1. **Frequency Counting**
#    * Use a hashmap (dictionary) to count occurrences of each number.
#    * This gives frequency in **O(n)** time.
# 2. **Maintain Min Heap of Size K**
#    * Push `(frequency, number)` into heap.
#    * If heap size exceeds `k`, remove the smallest frequency element.
#    * This ensures heap always contains top `k` frequent elements.

# Complexity:
# * **Time:** `O(n log k)`
# * **Space:** `O(n)` (hashmap + heap)


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashi = {}
        for i in nums:
            hashi[i] = hashi.get(i,0)+1
        heap = []
        ans = []
        for i in hashi:
            heapq.heappush(heap,(hashi[i],i))
            if len(heap) > k:
                heapq.heappop(heap)
        for freq, num in heap:
            ans.append(num) 
        return ans
