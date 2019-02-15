class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        last = None
        count = 0
        i = 0
        while i < len(chars):
            c = chars[i]

            if not last:
                last = c
                count = 1
                i += 1
                continue

            if c == last:
                count += 1
                i += 1
            else:
                last = c
                if count > 1:
                    chars[i-count+1:i] = str(count)
                    i = i-count+1 + len(str(count))
                count = 0           

        if count > 1:
            chars[i-count+1:i] = str(count)

        print(chars)
        return len(chars)

def main():
    print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
    print(Solution().compress(["a"]))
    print(Solution().compress(["a","a","b","b","c","c","c"]))
      

if __name__ == '__main__':
    main()