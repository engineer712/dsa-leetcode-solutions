class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res= []
        phone = {'2':'abc','3':'def','4':'ghi','5': 'jkl','6':'mno','7':'pqrs', '8' : 'tuv', '9': 'wxyz'}
        def backtrack(start,path):
            if start == len(digits):
                res.append(path[:])
                return
            for i in phone[digits[start]]:
                backtrack(start+1,path+i)

            
        backtrack(0,'')
        return res
