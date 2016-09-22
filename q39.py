import copy,time


class Solution:
    ans = []
    cans = []
    def combinationSum(self, candidates, target):
        self.cans = candidates
        self.cans.sort()
        self.dfs([], 0, target)
        print(self.ans)
        return self.ans

    def dfs(self, cur, fro, target):
        print(cur, fro, target)
        if target == 0:
            print('cur', copy.copy(cur))
            self.ans.append(cur[:])
        else:
            for i in range(fro, len(self.cans)):
                if self.cans[i] <= target:
                    cur.append(self.cans[i])
                    self.dfs(cur, i, target-self.cans[i])
                    cur.remove(self.cans[i])
a = time.time()
print(Solution().combinationSum([39,42,22,24,33,48,36,26,23,38,25,34,30,41,40,31,28,27,21,47,35,43,20,49,45,37,44,32], 61))
print(time.time() - a)
