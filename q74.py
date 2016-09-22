class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        yl, yr, y = 0, len(matrix)-1, -1
        while yl <= yr:
            mid = (yl + yr) / 2
            print mid
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                y = mid
                break
            elif target > matrix[mid][-1]:
                yl = mid + 1
            else:
                yr = mid - 1
        if y == -1:
            return False
        else:
            print y
            xl, xr = 0, len(matrix[0])-1
            while xl <= xr:
                mid = (xl + xr) / 2
                if matrix[y][mid] == target:
                    return True
                elif target > matrix[mid][-1]:
                    xl = mid + 1
                else:
                    xr = mid - 1
            return False

print Solution().searchMatrix([
    [1,3,5]
], 1)
