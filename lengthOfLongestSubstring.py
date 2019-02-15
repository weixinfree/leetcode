class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        def calcMaxLen(index):
            r = set()
            for i, c in enumerate(s[index:]):
                if c in r:
                    return i
                r.add(c)
            return len(r)

        return max([calcMaxLen(index) for index, _ in enumerate(s)])


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring('pwwkew'))
    print(s.lengthOfLongestSubstring(''))
    print(s.lengthOfLongestSubstring(' '))
