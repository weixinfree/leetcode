from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        def _key(v: str) -> str:
            return ''.join(sorted(v))

        from collections import defaultdict
        d = defaultdict(list)
        for s in strs:
            key = _key(s)
            d[key].append(s)

        return [v for _, v in d.items()]


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
