import math
import heapq

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        ln1 = len(nums1)
        ln2 = len(nums2)

        nums = list(heapq.merge(nums1, nums2))

        _mid = (ln1 + ln2 - 1) / 2
        supremum = math.ceil(_mid)
        infimun = math.floor(_mid)

        print(_mid, infimun, supremum)

        return (nums[infimun] + nums[supremum]) / 2

        
def main():
    Solution().findMedianSortedArrays([1,2], [3, 4])

if __name__ == '__main__':
    main()