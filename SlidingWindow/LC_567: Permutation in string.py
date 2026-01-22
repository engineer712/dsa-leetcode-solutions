class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        map_s1 = {}
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        # frequency map of s1
        for ch in s1:
            map_s1[ch] = map_s1.get(ch, 0) + 1

        for i in range(n2):
            if s2[i] in map_s1:
                l = i
                r = i + n1
                if r <= n2: # if the matched letter is last letter of string s2
                    map_s2 = {}
                    for j in range(l, r):
                        map_s2[s2[j]] = map_s2.get(s2[j], 0) + 1
                    if map_s1 == map_s2:# checks whether key,values of both dictionaries are same irrespective of the order
                        return True

        return False
