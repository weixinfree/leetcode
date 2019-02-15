class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def match_c(pi, si):
            if p[pi] == s[si]:
                return True
            if p[pi] == '.':
                return True

            return False

        pi = 0
        si = 0
        while si < len(s) and pi < len(p):
            pc = p[pi]
            sc = s[si]
            if match_c(pi, si):
                si += 1
                pi += 1
            elif pc == '*' and pi > 0 and match_c(pi - 1, si):
                si += 1
            elif (pi + 1 < len(p)) and p[pi + 1] == '*':
                pi += 2
            elif pc == '*' and (pi + 1 < len(p)):
                pi += 1
            else:
                print('mismatch: ', sc, si, '==', pc, pi)
                return False
        print('str:', s, si, 'pattern:', p, pi)
        return si == len(s) and pi >= len(p)


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aa", "a"))
    print(s.isMatch('aa', 'a*'))
    print(s.isMatch('ab', '.*'))
    print(s.isMatch('aab', 'c*a*b'))
    print(s.isMatch('mississippi', "mis*is*p*."))
    print(s.isMatch('ab', '.*c'))
    print(s.isMatch('aaa', 'aaaa'))
