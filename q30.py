class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wl = len(words[0])
        wsl = len("".join(words))
        res = []
        m2 = {}
        for i in words:
            if i not in m2:
                m2[i] = 0
            m2[i] += 1
        for i in range(len(s)-wsl+1):
            if i+wsl <= len(s) and self.equ(s[i:i+wsl], m2, wl):
                res.append(i)
        return res

    def equ(self, s, w, l):
        sl = []
        for i in range(len(s)/l):
            sl.append(s[i*l:(i+1)*l])
        m1 = {}
        for i in sl:
            if i not in m1:
                m1[i] = 0
            m1[i] += 1
        print m1, w
        if len(m1) != len(w):
            return False
        for i in m1:
            if i not in w or m1[i] != w[i]:
                return False
        return True

s = "wordgoodgoodgoodbestword"
w = ["word","good","best","good"]
print Solution().findSubstring(s, w)