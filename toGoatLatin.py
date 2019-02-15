class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        segs = S.split()
        
        def transform(w, index):
            r = None
            if w[0] in 'aeiouAEIOU':
                r = w + 'ma'
            else:
                r = w[1:] + w[0] + 'ma'

            r += 'a' * (index + 1)
            return r
        
        return ' '.join([transform(w, index) for index, w in enumerate(segs)])

def main():
    print(Solution().toGoatLatin("I speak Goat Latin"))

if __name__ == '__main__':
    main()