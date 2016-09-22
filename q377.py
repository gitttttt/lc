from math import factorial

class Solution(object):

    def combinationSum4(self, nums, target):
        res = [0 for x in range(target+1)]
        for i in range(target+1):
            tmp = 0
            for j in range(len(nums)):
                if i-nums[j] > 0:
                    tmp += res[i-nums[j]]
                elif i-nums[j] == 0:
                    tmp += 1
            res[i] = tmp
        print res

    # def combinationSum4(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     res, result = [], 0
    #     self.bs(nums, [], target, res, 0)
    #     for i in range(len(res)):
    #         tmp, m = res[i], {}
    #         for j in tmp:
    #             if j not in m:
    #                 m[j] = 0
    #             m[j] += 1
    #         arr = [m[j] for j in m]
    #         r = factorial(sum(arr)) / reduce(lambda x, y: x*y, map(factorial, arr))
    #         result += r
    #         print m
    #         print r
    #     print result
    #
    # def bs(self, arr, cur, target, res, begin):
    #     if target == 0:
    #         res.append(cur[::])
    #     else:
    #         for i in range(begin, len(arr)):
    #             if i <= target:
    #                 cur.append(arr[i])
    #                 self.bs(arr, cur, target-arr[i], res, i)
    #                 cur.pop()


Solution().combinationSum4([1,2,3], 4)

