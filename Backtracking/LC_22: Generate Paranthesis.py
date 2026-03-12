# Approach:
# Use backtracking to build valid parentheses combinations. At each step:
# Add "(" if the number of open brackets is less than n.
# Add ")" if the number of closing brackets is less than the number of open brackets.
# When the string length reaches 2 * n, store it in the result list. This ensures only valid parentheses sequences are generated.


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backtrack(open,close,string):
            if len(string) == n*2:
                res.append(string[:])
                return
            
            if open < n:
                backtrack(open+1,close,string + '(')
            if close < open:
                backtrack(open,close+1,string+ ')')


        backtrack(0,0,'')
        return res
