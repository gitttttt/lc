class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if not s:
        #     return 0
        # if len(s) == 1:
        #     return 0 if s[0] == '0' else 1
        # if len(s) == 2:
        #     if s[-2] == '0' or (s[-2] >= '3' and s[-1] == '0'):
        #         return 0
        #     if (s[-2] == '1' and s[-1] != '0') or (s[-2] == '2' and s[-1] <= '6'):
        #         return 2
        #     return 1
        # else:
        #     if '10' < s[-2::] < '26':
        #         return self.numDecodings(s[:-2:]) + self.numDecodings(s[:-1:])
        #     if s[-2] == '0' and s[-1] != '0':
        #         return self.numDecodings(s[:-1:])
        #     if s[-2::] == '10' or s[-2::] == '20':
        #         return self.numDecodings(s[:-2:])
        #     if (s[-2] >= '3' or s[-2] == '0') and s[-1] == '0':
        #         return 0
        if not s:
            return 0
        tmp = [0 for _ in s]
        for i in range(len(s)):
            if s[i] == '0':
                if i == 0 or not (s[i-1] == '1' or s[i-1] == '2'):
                    return 0
                else:
                    tmp[i] = 1 if i == 1 else tmp[i-2]
            else:
                if i > 0 and 10 < int(s[i-1:i+1:]) <= 26:
                    tmp[i] = tmp[i-1] + tmp[i-2] if i > 1 else tmp[i-1] + 1
                else:
                    tmp[i] = tmp[i-1] if i > 0 else 1
        print tmp
        return tmp[-1]

print Solution().numDecodings('12314')
