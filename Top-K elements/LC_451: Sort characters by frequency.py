# Approach:
# Use a max heap to pop to element which has high frequency as
# heapq is min heap by default we put -ve symbol to numbers while pushing so that this becomes a max heap.

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hashi = {}
        for i in s:
            hashi[i] = hashi.get(i,0) + 1
        heap = []
        for i in hashi:
            heapq.heappush(heap,[-hashi[i],i])
        ans = ''
        while len(heap) > 0:
            num, char =  heapq.heappop(heap)
            ans+= char*(-num)
        return ans
