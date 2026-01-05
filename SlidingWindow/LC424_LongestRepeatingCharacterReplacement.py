#LeetCode 424 - Longest Repeating Character Replacement(in python)

Sliding Window Pattern:
Maintain a window such that:
      (window_length - max_frequency_in_window) <= k
```python
class Solution(object):
    def characterReplacement(self, s, k):
        
        freq = {}
        max_freq = 0
        left = 0
        answer = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])

            # shrink window if more than k replacements needed
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer
```
