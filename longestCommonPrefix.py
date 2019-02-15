class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        index = -1
        L = min(len(s) for s in strs)

        for i in range(L):
            v = strs[0][i]
            if all(s[i] == v for s in strs[1:]):
                index = i
            else:
                break
        return strs[0][:index+1]


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix([]))
