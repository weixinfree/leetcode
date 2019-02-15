class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        size = len(x)
        mid = size // 2
        for i in range(mid):
            if x[i] != x[size - i - 1]:
                return False
        
        return True

def main():
    print(Solution().isPalindrome(0))
    print(Solution().isPalindrome(12321))
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(1))

if __name__ == '__main__':
    main()
