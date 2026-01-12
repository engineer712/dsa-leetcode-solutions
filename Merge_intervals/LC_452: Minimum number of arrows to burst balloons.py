class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        new = []
        start = points[0][0]
        end = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] > end:
                new.append([start,end])
                start = points[i][0]
                end = points[i][1]
            else:
                end = min(end,points[i][1])
        
        new.append([start,end])
        return len(new)


