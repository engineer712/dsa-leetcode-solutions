class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(start, path):
            if start == len(nums):
                res.append(path[:])
                return
            path.append(nums[start])
            backtrack(start+1,path)
            path.pop()
            backtrack(start + 1, path)

        
        backtrack(0,[])
        return res

