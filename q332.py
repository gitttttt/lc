class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        m = {}
        for t in tickets:
            if t[0] not in m:
                m[t[0]] = []
            m[t[0]].append(t[1])
        for f in m:
            m[f].sort()
        print m
        now = 'JFK'
        res = [now]
        while now:
            if now not in m:
                break
            else:
                if m[now]:
                    now = m[now].pop(0)
                    res.append(now)
                else:
                    break
        return res

a = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print Solution().findItinerary(a)