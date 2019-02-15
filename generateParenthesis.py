"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        n *= 2
        
        def all(c, index):
            c[index] = '('
            if index + 1 < n:
                yield from all(list(c), index + 1)
            
            if index == n - 1:
                yield ''.join(c)
            
            c[index] = ')'
            if index + 1 < n:
                yield from all(list(c), index + 1)

            if index == n - 1:
                yield ''.join(c)
        
        def is_valid(s):
            stack = []
            try:
                for c in s:
                    if c == '(':
                        stack.append(c)
                    elif c == ')':
                        stack.pop()
            except:
                return False
            
            return not stack

        _a = list(all(list(range(n)),0))
        print(_a)
        return [c for c in _a if is_valid(c)]
            
def main():
    print(Solution().generateParenthesis(3))

if __name__ == '__main__':
    main()
