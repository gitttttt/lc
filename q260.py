class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(lambda x, y: x ^ y, nums)
        mask = xor & (~(xor - 1))
        print mask
        a, b = 0, 0
        for i in nums:
            if i & mask == 0:
                a ^= i
            else:
                b ^= i
        print [a, b]

Solution().singleNumber([1,1,5, 4,2,2,4,7])