class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i, j, res = 0, 0, []
        while i > -1:
            if i > len(strs[0])-1:
                return "".join(res)
            p = strs[0][i]
            j = 1
            while j < len(strs):
                if i > len(strs[j])-1 or strs[j][i] != p:
                    return "".join(res)
                j += 1
            res.append(p)
            i += 1
        return "".join(res)

print Solution().longestCommonPrefix([])