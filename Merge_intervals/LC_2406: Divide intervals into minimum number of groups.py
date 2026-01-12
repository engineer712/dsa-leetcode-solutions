class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        print(intervals)
        heap = [intervals[0][1]]
        ans = 1
        for i in range(1,len(intervals)):
            if intervals[i][0] <= heap[0]:
                ans += 1
                heap.append(intervals[i][1])
            else:
                    heap.pop(0)
                    heap.append(intervals[i][1])
            heap.sort()
        return ans
        
        
