class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if i-1 == -1 or grid[i-1][j] == 0:
                        res += 1
                    if i+1 == len(grid) or grid[i+1][j] == 0:
                        res += 1
                    if j-1 == -1 or grid[i][j-1] == 0:
                        res += 1
                    if j+1 == len(grid[0]) or grid[i][j+1] == 0:
                        res += 1
        return res