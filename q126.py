import time
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        def f(s1, s2):
            i = 0
            for k in range(len(s1)):
                if s1[k] != s2[k]:
                    i += 1
                if i > 1:
                    return False
            return i == 1
        num = 0
        visited = [[beginWord]]
        while True not in map(lambda x: f(x, endWord), visited[-1]):
            tmp = []
            for s in visited[-1]:
                for j in range(len(s)):
                    for k in range(ord('a'), ord('z')):
                        ne = s[:j] + chr(k) + s[j+1:]
                        if ne in wordList and ne != s:
                            wordList.remove(ne)
                            tmp.append(ne)
            if not tmp:
                return 0
            visited.append(tmp)
            num += 1
        res = [[beginWord]]
        for i in range(1, len(visited)):
            now = visited[i]
            last = visited[i-1]
            if len(now) == 1:
                for j in res:
                    j.append(now[0])
            else:
                n = 0
                r = res[::]
                for j in res:
                    for k in now:
                        if f(j[-1], k):
                            if n == 0:
                                j.append(k)
                                n = 1
                            else:
                                l = j[::]
                                l.append(k)
                                r.append(l)
                res = r
        print 'r', res
        result = []
        m = min(map(lambda x: len(x), res))
        for i in res:
            if f(i[-1], endWord) and len(i) == m:
                i.append(endWord)
                result.append(i)
        print result
        return num + 2

print Solution().ladderLength('hit', 'cog', {"hot","dot","dog","lot","log"})