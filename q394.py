class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in range(len(s)):
            if s[i] == ']':
                tmp = []
                while res and res[-1] != '[':
                    tmp.append(res.pop())
                res.pop()
                num = []
                while res and '0' <= res[-1] <= '9':
                    num.append(res.pop())
                num = int(''.join(num[::-1]))
                res.append(''.join(tmp[::-1] * num))
            else:
                res.append(s[i])
        return ''.join(res)

print Solution().decodeString('2[abc]3[cd]ef')