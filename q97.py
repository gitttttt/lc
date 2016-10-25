class Solution(object):
    class Solution(object):
        def isInterleave(self, s1, s2, s3):
            """
            :type s1: str
            :type s2: str
            :type s3: str
            :rtype: bool
            """
            tmp = [[True for _ in len(s2) + 1] for _ in len(s1) + 1]
            for i in range(1, len(s2)+1):
                tmp[0][i] = tmp[0][i-1] if s2[i-1] == s3[i-1] else False
            for j in range(1, len(s1)+1):
                tmp[j][0] = tmp[j-1][0] if s1[j-1] == s3[j-1] else False
            for i in range(1, len(s1)+1):
                for j in range(1, len(s2)+1):
                    if s1[i-1] == s3[i+j-1] or s2[j-1] == s3[i+j-1]:
                        tmp[i][j] = tmp[i-1][j] or tmp[i][j-1]
                    else:
                        tmp[i][j] = False
            return tmp[-1][-1]

                pass

            # def isInterleave(self, s1, s2, s3):
    #     """
    #     :type s1: str
    #     :type s2: str
    #     :type s3: str
    #     :rtype: bool
    #     """
    #     if len(s1) + len(s2) != len(s3):
    #         return False
    #     i, j = 0, 0
    #     tmp = []
    #     while i < len(s1) and j < len(s3):
    #         while s1[i] != s3[j]:
    #             tmp.append(s3[j])
    #             j += 1
    #         i += 1
    #         j += 1
    #     if i != len(s1):
    #         return False
    #     else:
    #         while j < len(s3):
    #             tmp.append(s3[j])
    #             j += 1
    #         print tmp
    #     return "".join(tmp) == s3

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print Solution().isInterleave(s1, s2, s3)
