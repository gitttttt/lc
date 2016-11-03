class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = [[None, 0] for i in range(52)]
        for i in s:
            if