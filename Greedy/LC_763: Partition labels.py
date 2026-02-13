# Greedy Idea (Core Logic):
# 1. Store last index of each char
# 2. Track current partition end
# 3. When index == end → partition done

class Solution(object):
    def partitionLabels(self, s):
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        
        ans = []
        start = 0
        end = 0
        
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            
            if i == end:
                ans.append(end - start + 1)
                start = i + 1
        
        return ans
