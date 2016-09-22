class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        now, res, begin, candidates, num = [], [], 0, [i for i in range(1, 10, 1)], 0
        self.search(candidates, n, now, res, begin, num, k)
        return res

    def search(self, candidates, target, now, res, begin, num, k):
        if target == 0:
            if num == k:
                res.append(now[::])
                return
            else:
                return
        else:
            for i in range(begin, len(candidates)):
                if target >= candidates[i]:
                    now.append(candidates[i])
                    self.search(candidates, target-candidates[i], now, res, i+1, num+1, k)
                    now.pop()

print Solution().combinationSum3(3, 9)
