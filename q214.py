class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lcs = self.lcs(s, s[::-1])
        return s[lcs:][::-1] + s[:lcs] + s[lcs:]

    def lcs(self, s1, s2):
        res = 0
        dp = [[0 for _ in s2] for _ in s1]
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] != s2[j]:
                    dp[i][j] = 0
                else:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1

                    res = max(res, dp[i][j])
        return res
a = 'aacecaaa'
print Solution().shortestPalindrome(a)
