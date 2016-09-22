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
            print visited
        return num + 2

print Solution().ladderLength('hit', 'cog', {"hot","dot","dog","lot","log"})