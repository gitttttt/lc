class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = set()
        res = 0
        for i in s:
            if i in st:
                st.remove(i)
                res += 2
            else:
                st.add(i)
        if st:
            res += 1
        return res
