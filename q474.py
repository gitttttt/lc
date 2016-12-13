class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            for i in range(m, s.count('0')-1, -1):
                for j in range(n, s.count('1')-1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-s.count('0')][j-s.count('1')])
            print dp
            print
        return dp[-1][-1]


s = ["10", "0001", "111001", "1", "0"]
Solution().findMaxForm(s, 5, 3)