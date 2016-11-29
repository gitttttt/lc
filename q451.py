class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = {}
        for i in s:
            if i not in tmp:
                tmp[i] = 0
            tmp[i] += 1
        tmp = sorted(tmp.iteritems(), key=lambda x: x[1], reverse=True)
        print tmp
        res = []
        for i in tmp:
            res.append(i[1] * i[0])
        return ''.join(res)

print Solution().frequencySort("2a554442f544asfasssffffasss")
