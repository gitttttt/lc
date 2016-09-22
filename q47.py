class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.part(nums, [], res, 0)
        return res

    def part(self, arr, cur, res, begin):
        if len(arr) == len(cur):
            res.append(cur[::])
        else:
            for i in range(begin, len(arr)):
                cur.append(arr[i])
                self.part(arr, cur, res, begin+1)
                cur.pop(-1)

print Solution().permuteUnique([1,1,2])
a = [1,1,2]
a.pop()
print a