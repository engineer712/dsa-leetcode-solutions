# Given a string of digits, each digit maps to a set of characters on a phone keypad. The idea is to generate all possible letter combinations that the digits could represent.

# Approach (Backtracking):
# 1. Create a dictionary that maps each digit (2–9) to its corresponding letters.
# 2. Use **backtracking** to build combinations recursively.
# 3. Start from index `0` of the digits string and maintain a `path` string representing the current combination.
# 4. For the current digit, iterate through all its mapped letters.
# 5. Append each letter to the current path and recursively move to the next digit.
# 6. When the path length equals the number of digits, add the combination to the result list.
# 7. Continue exploring all possible choices until every combination is generated.


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
