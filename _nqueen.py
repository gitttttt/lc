class Solution(object):
    def solveNQueens(self, n):
        """
        http://blog.csdn.net/hackbuteer1/article/details/6657109
        :type n: int
        :rtype: List[List[str]]
        """
        arr = [-1 for _ in range(n)]
        res = []
        i, j = 0, 0
        while i < n:
            while j < n:
                if self.valid(i, j, arr):
                    arr[i] = j
                    j = 0
                    break
                else:
                    j += 1
            if arr[i] < 0:
                if i == 0:
                    break
                else:
                    i -= 1
                    j = arr[i] + 1
                    arr[i] = -1
                    continue
            if i == n-1:
                res.append(arr[::])
                j = arr[i] + 1
                arr[i] = -1
                continue
            i += 1
        result = []
        print res
        for i in res:
            tmp = [['.' for _ in range(n)] for _ in range(n)]
            for j in range(n):
                tmp[j][i[j]] = 'Q'
            result.append(map(lambda x: "".join(x), tmp))
        return result

    def valid(self, x, y, arr):
        for i in range(x):
            if arr[i] == y or abs(i-x) == abs(y-arr[i]):
                return False
        return True

print Solution().solveNQueens(8)
