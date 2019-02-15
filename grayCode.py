"""
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印格雷码序列。格雷码序列必须以 0 开头。

例如，给定 n = 2，返回 [0,1,3,2]。其格雷编码是：

00 - 0
01 - 1
11 - 3
10 - 2
说明:

对于给定的 n，其格雷编码的顺序并不唯一。

例如 [0,2,3,1] 也是一个有效的格雷编码顺序。
"""


class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if n <= 0:
            return [0]

        def all(a, i):
            a[i] = 0
            if i + 1 < len(a):
                yield from all(list(a), i + 1)

            if i == len(a) - 1:
                yield list(a)

            a[i] = 1
            if i + 1 < len(a):
                yield from all(list(a), i + 1)

            if i == len(a) - 1:
                yield list(a)

        _a = [0 for _ in range(n)]

        combine = list(all(_a, 0))
        size = len(combine)

        def diff(l, r):
            return sum(1 for i,j in zip(l,r) if i != j)

        def find_diff_1(from_index, a):
            _index = from_index
            while _index < size:
                if diff(a, combine[_index]) == 1:
                    return _index
                _index += 1

        def ajust():
            index = 0
            while index + 1 < size:
                if diff(combine[index], combine[index+1]) == 1:
                    index += 1
                    continue

                l = index+1
                r = find_diff_1(index+2, combine[index])
                print(l, r)
                if r:
                    print(combine[l], combine[r])
                    combine[r], combine[l] = combine[l], combine[r]
                index += 1

        print('before', combine)
        ajust()
        print('after', combine)

        def as_int(a):
            return sum(2 ** (n - 1 - i) for i, _ in enumerate(a) if a[i] == 1)

        return [as_int(item) for item in combine]



def main():
    print(Solution().grayCode(3))


if __name__ == '__main__':
    main()
