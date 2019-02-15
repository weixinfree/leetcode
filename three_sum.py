class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import combinations
        r = set()
        for i in combinations(nums, 3):
            li = frozenset(i)
            print(li)
            if sum(li) == 0:
                r.add(li)
        return r


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
