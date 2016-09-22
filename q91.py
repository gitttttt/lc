class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return 0 if s[0] == '0' else 1
        if len(s) == 2:
            if s[-2] == '0' or (s[-2] >= '3' and s[-1] == '0'):
                return 0
            if (s[-2] == '1' and s[-1] != '0') or (s[-2] == '2' and s[-1] <= '6'):
                return 2
            return 1
        else:
            if '10' < s[-2::] < '26':
                return self.numDecodings(s[:-2:]) + self.numDecodings(s[:-1:])
            if s[-2] == '0' and s[-1] != '0':
                return self.numDecodings(s[:-1:])
            if s[-2::] == '10' or s[-2::] == '20':
                return self.numDecodings(s[:-2:])
            if (s[-2] >= '3' or s[-2] == '0') and s[-1] == '0':
                return 0

print Solution().numDecodings('1031')
