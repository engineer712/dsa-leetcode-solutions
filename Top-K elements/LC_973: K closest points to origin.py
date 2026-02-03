#Optimal Approach:
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for x1,y1 in points:
            heapq.heappush(heap,(-(x1**2 + y1**2),[x1,y1]))
            if len(heap)>k:
                heapq.heappop(heap)
              
        return [j for i,j in heap]
      
#Approach 2:(not much optimal)
# class Solution(object):
#     def kClosest(self, points, k):
#         """
#         :type points: List[List[int]]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         heap = []
#         for x1,y1 in points:
#             heapq.heappush(heap,(-math.sqrt(x1**2 + y1**2),[x1,y1]))
        
#         for i in range(len(points) - k):
#             heapq.heappop(heap)

#         return [j for i,j in heap]
        
