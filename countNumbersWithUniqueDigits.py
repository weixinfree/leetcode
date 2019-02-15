class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 1:
            return 1

        if n == 1:
            return 10
        
        return 10 ** n - n * 10 * (n-1) * (10 ** (n-2))  + 10 ** (n-2)

def main():
    print(Solution().countNumbersWithUniqueDigits(1))
    print(Solution().countNumbersWithUniqueDigits(2))
    print(Solution().countNumbersWithUniqueDigits(3))

if __name__ == '__main__':
    main()