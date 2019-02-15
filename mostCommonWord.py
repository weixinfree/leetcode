class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        banned = set(banned)

        import re
        from collections import defaultdict
        collect = defaultdict(int)
        for w in re.findall(r'\w+', paragraph.lower()):
            if w not in banned:
                collect[w] += 1
        return max(collect, default = 0, key = lambda x: collect[x])


def main():
    print(Solution().mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', []))

if __name__ == '__main__':
    main()