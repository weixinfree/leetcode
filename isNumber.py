class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        import re
        pats = {
            # 整数
            re.compile(r'\s*[+-]?\d+\s*'),
            # 小数
            re.compile(r'\s*[+-]?\.\d+\s*'),
            re.compile(r'\s*[+-]?\d*\.\d+\s*'),
            re.compile(r'\s*[+-]?\d+\.\s*'),
            # 指数
            re.compile(r'\s*[+-]?\.\d+?(e|E)[+-]?\d+?\s*'),
            re.compile(r'\s*[+-]?\d*\.\d+?(e|E)[+-]?\d+?\s*'),
            re.compile(r'\s*[+-]?\d+\.?(e|E)[+-]?\d+?\s*')
        }        

        return True if any(pat.fullmatch(s) for pat in pats) else False

def main():
    print(Solution().isNumber(' 0e '))
    print(Solution().isNumber(' -123 '))
    print(Solution().isNumber(' abc 0 '))
    print(Solution().isNumber(' 3.2 '))
    print(Solution().isNumber(' -0.2 '))
    print(Solution().isNumber(' 2e10 '))
    print(Solution().isNumber(' 2.35E-10.28 '))
    print(Solution().isNumber(' 0 '))
    print(Solution().isNumber(' 0 '))

if __name__ == '__main__':
    main()