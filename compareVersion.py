class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        v1stack = version1.split('.')
        v2stack = version2.split('.')

        while v1stack and v2stack:
            v1 = int(v1stack.pop(0))
            v2 = int(v2stack.pop(0))



            if v1 > v2:
                return 1
            
            if v1 < v2:
                return -1

        print(v1stack)
        print(v2stack)
        
        if v1stack and not all(item == '0' for item in v1stack):
            return 1
        if v2stack and not all(item == '0' for item in v2stack):
            return -1

        return 0

def main():
    print(Solution().compareVersion('1','1.1'))

if __name__ == '__main__':
    main()
