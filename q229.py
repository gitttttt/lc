class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        z1, z2 = 0, 0
        n1, n2 = 0, 0
        for i in nums:
            if i == z1:
                n1 += 1
            elif i == z2:
                n2 += 1
            elif not n1:
                z1 = i
                n1 = 1
            elif not n2:
                z2 = i
                n2 = 1
            else:
                n1 -= 1
                n2 -= 1
        r1, r2 = 0, 0
        print z1, z2
        for i in nums:
            if i == z1:
                r1 += 1
            elif i == z2:
                r2 += 1
        res = []
        if r1 > int(len(nums)/3):
            res.append(z1)
        if r2 > int(len(nums)/3):
            res.append(z2)
        return res

print Solution().majorityElement([0,0,0])