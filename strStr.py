class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        len_s = len(haystack)
        len_n = len(needle)

        if len_n == len_s:
            return 0 if haystack == needle else -1

        if len_n > len_s:
            return -1

        for i in range(len_s - len_n + 1):
            if haystack[i:i+len_n] == needle:
                return i

        return -1