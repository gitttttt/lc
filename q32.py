class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                tmp.append(i)
            else:
                if len(tmp) > 1:
                    tmp.pop()
                    res = max(res, i - tmp[0])
                else:
                    tmp.pop()
                    tmp.append(i)
        print res

Solution().longestValidParentheses("()(())((()")



