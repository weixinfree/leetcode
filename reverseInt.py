class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        sign = 1 if x > 0 else -1

        def split(x):
            result = []
            a = x % 10
            b = 10
            result.append(a)

            while (x % b) != x:
                _b = b
                b *= 10
                a = x % b // _b
                result.append(a)

            return result
            
        value = sign * int(''.join(str(item) for item in split(abs(x))))
        if value > 2 ** 31 - 1 or (value < -1 * 2 ** 31):
            return 0
        return value

def main():
    print(Solution().reverse(-123))

if __name__ == '__main__':
    main()