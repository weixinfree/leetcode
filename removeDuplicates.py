from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]):
        """
        :type nums: List[int]
        :rtype: int
        """

        last = None
        for index, num in enumerate(nums):
            if num == last:
                nums[index] = None
            last = num
        
        c = nums.count(None)
        [nums.remove(None) for i in range(c)]

        return len(nums)

def main():
    nums = [1,1,1,1,2,2,3,4]
    Solution().removeDuplicates(nums)
    print(nums)

if __name__ == '__main__':
    main()
