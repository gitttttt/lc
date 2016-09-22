class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.search(s, 0, len(s)-1, res, [])
        return res

    def search(self, s, begin, end, res, cur):
        if begin > end:
            res.append(cur[::])
        else:
            for i in range(begin, end+1):
                if self.isp(s[begin:i+1]):
                    print 'i', s[begin:i+1]
                    cur.append(s[begin:i+1])
                    self.search(s, i+1, end, res, cur)
                    cur.pop()



    def isp(self, s):
        print s
        return s == s[::-1]

print Solution().partition( "aabaa")