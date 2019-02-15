class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        def as_num(c):
            return 0 if c == '0' else 1

        def b_add(l, r, carry):
            v = as_num(l) + as_num(r) + carry
            return v % 2, v // 2

        result = []
        carry = 0
        from itertools import zip_longest
        for l, r in zip_longest(reversed(a), reversed(b), fillvalue='0'):
            v, carry = b_add(l, r, carry)
            result.append(v)
        if carry > 0:
            result.append(carry)

        return ''.join(str(n) for n in reversed(result))


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary(a="11", b="1"))
    print(s.addBinary(a="1010", b="1011"))
