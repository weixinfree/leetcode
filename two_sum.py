class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for index, v in enumerate(nums):
            r = target - v
            ri = d.get(r, -1)
            if ri != -1:
                return [ri, index]
            d[v] = index


def test():
    s = Solution()
    print(s.twoSum([3, 3], 6))


if __name__ == "__main__":
    test()
