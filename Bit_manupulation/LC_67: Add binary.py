class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def findnum(binary):
            return int(binary,2)

        ans = findnum(a) + findnum(b)
        res =  bin(ans)
        return res[2:]
