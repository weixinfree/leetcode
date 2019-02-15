class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        class Node:
            def __init__(self, c):
                self.c = c
                self.nexts = []

        pat = Node('.')
        cur = pat
        for index, c in enumerate(p):
            if c == '*':
                pass
            elif c == '.':
                pass
            else:
                node = Node(c)
                cur.nexts.append(node)
                cur = node


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aa", "a"))
    print(s.isMatch('aa', 'a*'))
    print(s.isMatch('ab', '.*'))
    print(s.isMatch('aab', 'c*a*b'))
    print(s.isMatch('mississippi', "mis*is*p*."))
    print(s.isMatch('ab', '.*c'))
    print(s.isMatch('aaa', 'aaaa'))
