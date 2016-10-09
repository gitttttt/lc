class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        i, j = 0, 0
        tmp = []
        while i < len(s1) and j < len(s3):
            while s1[i] != s3[j]:
                tmp.append(s3[j])
                j += 1
            i += 1
            j += 1
        if i != len(s1):
            return False
        else:
            while j < len(s3):
                tmp.append(s3[j])
                j += 1
            print tmp
        return "".join(tmp) == s3

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print Solution().isInterleave(s1, s2, s3)
