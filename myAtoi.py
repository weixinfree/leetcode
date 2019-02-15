class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """

        INT_MIN = -1 * 2 ** 31
        INT_MAX= 2 ** 31 - 1
        
        nums = []
        start_num = False
        for c in s:
            if not start_num and c == ' ':
                continue

            start_num = True

            if c in '-+' and not nums:
                nums.append(c)
            elif c in '0123456789':
                nums.append(c)
            else:
                break

        if not nums:
            return 0
        
        try:
            value = int(''.join(nums))
        except:
            return 0
        
        if value > INT_MAX:
            return INT_MAX
        if value < INT_MIN:
            return INT_MIN
        
        return value

def main():
    print(Solution().myAtoi('-5-'))
    print(Solution().myAtoi('123'))
    print(Solution().myAtoi('-100'))
    print(Solution().myAtoi('hello 100'))
    print(Solution().myAtoi('100 hello'))

if __name__ == '__main__':
    main()

