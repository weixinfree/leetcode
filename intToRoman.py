class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        p = [('CM', 900), ('CD', 400), ('XC', 90),
             ('XL', 40), ('IV', 4), ('IX', 9),
             ('M', 1000), ('D', 500), ('C', 100),
             ('L', 50), ('X', 10), ('V', 5),
             ('I', 1)]

        p.sort(key=lambda x: -x[1])
        # print(p)

        index = 0
        while index < len(p):
            _, v = p[index]
            if v <= num:
                break
            index += 1

        result = []
        remind = num
        while remind > 0:
            roma, v = p[index]
            index += 1
            count = remind // v
            result.append(roma * count)
            remind %= v
        return ''.join(result)


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(123))
    print(s.intToRoman(3))
    print(s.intToRoman(4))
    print(s.intToRoman(9))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))
