class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if not nums:
            return 0

        L = len(nums)

        def remove(index):
            print('remove', index)
            for i in range(index, L-1):
                nums[i] = nums[i+1]

        remove_c = 0
        for i in range(L-1, -1, -1):
            if nums[i] == val:
                remove(i)
                print(nums)
                remove_c += 1

        return L - remove_c


if __name__ == "__main__":
    s = Solution()
    li = [3, 2, 2, 3]
    print(s.removeElement(li, 3))
