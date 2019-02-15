class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index, v in enumerate(nums):
            if v >= target:
                return index

        return len(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))
    print(s.searchInsert([1, 3, 5, 6], 7))
    print(s.searchInsert([1, 3, 5, 6], 2))
    print(s.searchInsert([1, 3, 5, 6], 0))
