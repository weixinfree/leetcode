"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        parentheses = {
            '(':')',
            '{':'}',
            '[':']'
        }
        open_p = set(parentheses.keys())
        close_p = set(parentheses.values())
        stack = []

        for c in s:
            if c in open_p:
                stack.append(c)
            elif c in close_p and stack and c == parentheses.get(stack[-1], None):
                stack.pop()
            else:
                return False

        return not stack

def main():
    print(Solution().isValid('{}'))
    print(Solution().isValid('{[]}'))
    print(Solution().isValid('{1}'))

if __name__ == '__main__':
    main()
