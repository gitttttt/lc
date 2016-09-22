class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def part(n, res, cur):
            if len(cur) == len(nums):
                res.append(cur[::])
            else:
                for i in range(len(n)):
                    cur.append(n[i])
                    nn = n[::]
                    nn.pop(i)
                    part(nn, res, cur)
                    cur.pop()
        res = []
        part(nums, res, [])
        return res

print Solution().permute([1,2,3])