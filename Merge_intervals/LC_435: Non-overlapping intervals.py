class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda interval: interval[1])
        ans = 0
        start = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < start:
                ans += 1
            else:
                start = intervals[i][1]

        return ans


