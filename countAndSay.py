class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def count(nums):
            r = []
            pre = None
            count = 0
            for v in nums:
                if not pre:
                    pre = v
                    count = 1
                    continue
                if pre == v:
                    count += 1
                else:
                    r.append(count)
                    r.append(pre)
                    pre = v
                    count = 1

            if count > 0:
                r.append(count)
                r.append(nums[-1])
            return r

        nums = [1]
        for _ in range(1, n):
            nums = count(nums)
        return ''.join(str(n) for n in nums)


if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(1))
    print(s.countAndSay(2))
    print(s.countAndSay(3))
    print(s.countAndSay(4))
    print(s.countAndSay(5))
    print(s.countAndSay(6))
    print(s.countAndSay(7))
    print(s.countAndSay(8))
