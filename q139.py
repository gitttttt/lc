class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [True] + [False for _ in s]
        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    print i
                    dp[i] = True
                    break
        print dp
        return dp[-1]

s = ''
w = {'aa', 'aaa'}
print Solution().wordBreak(s, w)
