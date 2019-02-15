class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = [('CM', 900), ('CD', 400), ('XC', 90),
             ('XL', 40), ('IV', 4), ('IX', 9),
             ('M', 1000), ('D', 500), ('C', 100),
             ('L', 50), ('X', 10), ('V', 5),
             ('I', 1)]

        result = 0

        index = 0
        L = len(s)
        while index < L:
            for roman, v in p:
                step = len(roman)
                if roman == s[index:index + step]:
                    result += v
                    index += step
                    break

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt('III'))
    print(s.romanToInt('IV'))
    print(s.romanToInt("IX"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))
    print(s.romanToInt("MMMXLV"))
