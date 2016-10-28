class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        m = {}
        for i in range(num+1):
            if i == 4:
                continue
            if num-i == 6:
                continue
            r1 = []
            if str(i) + 'a' in m:
                r1 = m[str(i) + 'a']
            else:
                self.help(i, ['0' for _ in range(4)], r1, 0)
                m[str(i) + 'a'] = r1
            r2 = []
            if str(num-i) + 'b' in m:
                r2 = m[str(num-i) + 'b']
            else:
                self.help(num-i, ['0' for _ in range(6)], r2, 0)
                m[str(num-i) + 'b'] = r2
            res.extend(self.format(r1, r2))
        print res


    def help(self, t, now, res, begin):
        if now.count('1') == t:
            res.append(now[::])
        else:
            for i in range(begin, len(now)):
                now[i] = '1'
                self.help(t, now, res, i+1)
                now[i] = '0'

    def format(self, arr1, arr2):
        res = []
        for i in arr1:
            for j in arr2:
                a = int(''.join(i), 2)
                if a > 12:
                    continue
                else:
                    b = int(''.join(j), 2)
                    if b > 59:
                        continue
                    else:
                        if b < 10:
                            res.append(str(a) + ':0' + str(b))
                        else:
                            res.append(str(a) + ':' + str(b))
        return res

Solution().readBinaryWatch(0)