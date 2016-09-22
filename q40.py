class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        now, res, begin = [], [], 0
        self.search(sorted(candidates), target, now, res, begin)
        return res

    def search(self, candidates, target, now, res, begin):
        if target == 0 and now not in res:
            res.append(now[::])
            return
        else:
            for i in range(begin, len(candidates)):
                if target >= candidates[i]:
                    now.append(candidates[i])
                    self.search(candidates, target-candidates[i], now, res, i+1)
                    now.pop()

print Solution().combinationSum2([1,1,2,2,4], 6)