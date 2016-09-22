class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = len(s)
        flag = False
        tmp = [-1 for x in range(26)]
        for i in range(len(s)):
            if tmp[ord(s[i]) - ord('a')] == -1:
                tmp[ord(s[i]) - ord('a')] = i
            elif tmp[ord(s[i]) - ord('a')] == -2:
                continue
            else:
                tmp[ord(s[i]) - ord('a')] = -2
        for i in tmp:
            if i > -1:
                res = min(res, i)
                flag = True
        return res if flag else -1

print Solution().firstUniqChar("a")

