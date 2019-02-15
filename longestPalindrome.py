"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def is_pal(start, end):
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False

            return True

        max_pal = ''
        size = len(s)
        for i in range(size):
            for j in range(size - 1, i-1, -1):
                if is_pal(i, j):
                    
                    pal = s[i:j+1]
                    _s_pal = j+1-i
                    
                    if _s_pal > len(max_pal):
                        max_pal = pal
                    
                    if _s_pal == size:
                        return max_pal
        
        return max_pal


def main():
    print(Solution().longestPalindrome('a'))


if __name__ == '__main__':
    main()
