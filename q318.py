class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(words[i]) * len(words[j]) > res:
                    if self.help(words[i], words[j]):
                        res = len(words[i]) * len(words[j])
        return res

    def help(self, s1, s2):
        s1 = ''.join(list(set(s1)))
        s2 = ''.join(list(set(s2)))
        i1, i2 = 0, 0
        for i in s1:
            print '1', (ord(i) - ord('a'))
            i1 |= 1 << (ord(i) - ord('a'))
        for i in s2:
            i2 |= 1 << (ord(i) - ord('a'))
        return (i1 & i2) == 0

print Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
