# Approach:
# - Since both interval lists are already sorted and internally non-overlapping,
#   we use a two-pointer technique.
# - For each pair of intervals, compute:
#       start = max(start1, start2)
#       end   = min(end1, end2)
# - If start <= end, they overlap → add [start, end] to result.
# - Move the pointer of the interval that ends first,
#   because it cannot overlap with future intervals.
# - Time Complexity: O(n + m)
# - Space Complexity: O(k) for storing intersections.


class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        res = []
        while i<len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                res.append([start,end])

            if firstList[i][1] < secondList[j][1]:
                i+=1
            else:
                j+=1
        return res
