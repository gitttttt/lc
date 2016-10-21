class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: st
        :type t: st
        :rtype: st
        """
        tmap = {}
        for i in t:
            if i not in tmap:
                tmap[i] = 0
            tmap[i] += 1
        smap = {}
        count = 0
        start = 0
        l = 1000000
        st = ''
        for i in range(len(s)):
            if s[i] in tmap:
                if s[i] not in smap:
                    smap[s[i]] = 0
                smap[s[i]] += 1
                if smap[s[i]] <= tmap[s[i]]:
                    count += 1
                if count == len(t):
                    while s[start] not in smap or smap[start] > tmap[start]:
                        if smap[start] > tmap[start]:
                            smap[start] -= 1
                        start += 1
                    tmp = i - start + 1
                    if tmp < l:
                        l = tmp
                        st = s[start:i+1]
        return st

