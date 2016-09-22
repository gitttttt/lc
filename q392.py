class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            while j < len(t) and t[j] != s[i]:
                j += 1
            if j == len(t) and t[-1] != s[i]:
                return False
            j += 1
            i += 1
            if i == len(s):
                return True
        return False

print Solution().isSubsequence('abc', 'aaaaabbbdc')