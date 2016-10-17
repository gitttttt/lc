class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        v = [False] * len(nums)
        self.part(nums, [], res, v)
        return res

    def part(self, arr, cur, res, v):
        print v, cur
        if len(arr) == len(cur):
            res.append(cur[::])
        else:
            for i in range(0, len(arr)):
                if not v[i]:
                    if i>0 and arr[i] == arr[i-1] and v[i-1]:
                        return
                    v[i] = True
                    cur.append(arr[i])
                    self.part(arr, cur, res, v)
                    cur.pop()
                    v[i] = False

print (Solution().permuteUnique([1,1,1,2]))


