class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(0, 32):
            tmp = 0
            for j in nums:
                if j & (1 << i):
                    tmp += 1
            tmp %= 3
            if i != 31:
                res += tmp << i
            elif tmp == 1:
                res -= 1 << 31
        return res


print Solution().singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])