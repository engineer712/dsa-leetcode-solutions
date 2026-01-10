#  Used "fixed-size sliding window" based on word length.
#  For each start index, split the substring into equal word blocks, count frequencies using a dictionary, and compare with given words frequency.
#  If all words match exactly once, store the index.

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        wordlen = len(words[0])
        total_words = len(words)
        window_len = wordlen * total_words
        n = len(s)
        word_count = {}
        for w in words:
            word_count[w] = word_count.get(w,0)+1
        ans = []
        for i in range(wordlen):
            left = i
            curr = {}
            count =0
            for j in range(i,n-wordlen+1,wordlen):
                word = s[j:j+wordlen]
                if word in word_count:
                    curr[word] = curr.get(word,0)+1
                    count+=1
                    while curr[word]> word_count[word]:
                        lw = s[left: left+wordlen]
                        curr[lw] -=1
                        left+=wordlen
                        count-=1
                    if count == total_words:
                        ans.append(left)
                else:
                    curr.clear()
                    count = 0
                    left = j + wordlen
        return ans
