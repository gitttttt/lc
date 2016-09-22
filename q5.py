class Solution(object):
    def longestPalindrome(self, s):
        length, res = 0, ''
        m = [[0 for x in range(len(s))] for x in range(len(s))]
        for i in range(len(s)):
            m[i][i] = 1
            if i+1 < len(s) and s[i] == s[i+1]:
                m[i][i+1] = 1
                length = 2
        print m
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i+j] == s[i-j] and i+1 < len(s) and j-1 >= 0 and m[i+1][j-1] == 1:
                    print i, j
                    m[i][j] = 1
                    if j-i+1 > length:
                        length = j-i+1
                        res = s[i:j+1]
        print m
        return res


    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     length = 0
    #     res = ''
    #     for i in range(0, len(s)):
    #         j = 0
    #         while i+j < len(s) and i-j >= 0 and s[i-j] == s[i+j]:
    #             if 2*j+1 >= length:
    #                 res = s[i-j: i+j+1]
    #                 length = 2*j+1
    #             j += 1
    #     for i in range(1, len(s)):
    #         j = 1
    #         while i-j >= 0 and i+j-1 < len(s) and s[i-j] == s[i+j-1]:
    #             if 2*j >= length:
    #                 res = s[i-j: i+j]
    #                 length = 2*j
    #             j += 1
    #     return res

print Solution().longestPalindrome('abbabbcccbb')
