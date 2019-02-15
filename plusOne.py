class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        carry = 1
        for n in reversed(digits):
            v = n + carry
            carry = v // 10
            r = v % 10
            result.append(r)

        if carry > 0:
            result.append(carry)

        return list(reversed(result))


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1, 2, 3]))
    print(s.plusOne([4, 3, 2, 1]))
