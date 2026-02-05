#For next greater element we use montonic decereasing stack i.e. 
# we pop elements when the monotonic decreasing property is violated

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        stack = []
        ans = [0]* n 

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                poppy = stack.pop()
                ans[poppy] = i - poppy 
            stack.append(i)
        return ans
        
