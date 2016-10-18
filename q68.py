class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        start = 0
        i = 0
        while i < len(words):
            j = 0
            total = len(words[i])
            while total <= maxWidth:
                j += 1
                total += len(words[i+j]) + 1
            part = words[i:j]
            r = (maxWidth - sum(map(len, part))) / (j-i)
            l = maxWidth - r * (j-i)
            tmp = [words[i] + ' '*l]
            for k in range(i+1, j):
                pass


