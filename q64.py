class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = [[0 for _ in grid[0]] for _ in grid]
        res[0][0] = grid[0][0]
        for i in range(1, len(grid[0])):
            res[0][i] = res[0][i-1] + grid[0][i]
        for i in range(1, len(grid)):
            res[i][0] = res[i-1][0] + grid[i][0]
            for j in range(1, len(grid[i])):
                res[i][j] = min(res[i][j-1], res[i-1][j]) + grid[i][j]
        print res
        return res[-1][-1]

print Solution().minPathSum([[1,2,3], [4,5,6], [7,8,9]])