class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        digree = [0 for i in xrange(n)]
        g = [[0 for i in xrange(n)] for i in xrange(n)]
        for x,y in edges:
            digree[x] += 1
            digree[y] += 1
            g[x][y] = 1
            g[y][x] = 1
        print g
        print digree

        leaves = [i for i in xrange(n) if digree[i]==1]
        nodes = n
        while nodes > 2:
            temp = []
            nodes -= len(leaves)
            for i in leaves:
                digree[i] = 0
                for j in g[i]:
                    if j == 1:
                        digree[j] -= 1
                        if digree[j] == 1:
                            temp.append(j)
            leaves = temp
        return leaves

print Solution().findMinHeightTrees(6,
                                    [[3,0],[3,1],[3,2],[3,4],[5,4]])