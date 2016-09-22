class Solution(object):

    def __init__(self):
        self.flag = True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        gragh = [[0 for x in range(numCourses)] for x in range(numCourses)]
        for i in prerequisites:
            gragh[i[0]][i[1]] = 1
        for i in [0]:
            if not self.flag:
                return False
            else:
                visited = [0] * numCourses
                visited[i] = 1
                self.dfs_matrix(i, gragh, visited)
                print self.flag
        return self.flag

    def dfs_matrix(self, i, gragh, visited):
        print i, visited
        if not self.flag:
            return False
        else:
            for c, v in enumerate(gragh[i]):
                if c != i and v == 1:
                    if visited[c] == 0:
                        visited[c] = 1
                        self.dfs_matrix(c, gragh, visited)
                    else:
                        self.flag = False

print Solution().canFinish(3, [[0,1],[0,2],[1,2]])
