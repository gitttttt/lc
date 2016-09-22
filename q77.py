import time

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return [[]]
        arr = [i for i in range(1, n+1)]
        res = []
        if k <= int(n/2):
            self.search(res, [], 0, arr, k)
            return res
        else:
            self.search(res, [], 0, arr, n - k)
            return map(lambda x: list(set(arr) - set(x)), res)



    def search(self, res, cur, begin, arr, k):
        if len(cur) == k:
            res.append(cur[::])
        else:
            for i in range(begin, len(arr)):
                cur.append(arr[i])
                self.search(res, cur, i+1, arr, k)
                cur.pop()

t = time.time()
Solution().combine(20, 19)
print time.time() - t