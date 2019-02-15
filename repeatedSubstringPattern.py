class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        size = len(s)

        def is_repeat(step, p):
            if size % step != 0:
                return False
            
            for i in range(step, size+1, step):
                if s[i-step:i] != p:
                    return False
            
            return True

        for i in range(1, size//2 + 1):
            p = s[:i]
            if is_repeat(i, p):
                print('repeat pattern: ', i, p)
                return True
            
        return False

def main():
    print(Solution().repeatedSubstringPattern('abac'))

if __name__ == '__main__':
    main()