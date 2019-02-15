class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        
        times = 1
        r = A
        while B not in r:
            r += A
            times += 1
            if len(r) > 10000:
                return -1
        
        return times