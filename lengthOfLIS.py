"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        size = len(nums)

        def ascending_seq(c, index):

            if index >= size - 1:
                yield c
            
            top = nums[index]
            c.append(top)

            for i, v in enumerate(nums[index+1:]):
                    if v > top:
                        ascending_seq(list(c), i + index + 1)

        lis = 1
        while i < size - lis:
            for seq in ascending_seq([], i):
                print(seq)
                l = len(seq) 
                if l >= lis:
                    print(seq)
                    lis = l
            i += 1
        
        return lis
    
def main():
    # print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
    # print(Solution().lengthOfLIS([0]))
    print(Solution().lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))

if __name__ == '__main__':
    main()

