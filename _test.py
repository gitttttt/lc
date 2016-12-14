class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        s = nums[0]
        tmp = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == tmp+1:
                tmp = nums[i]
            else:
                if s == tmp:
                    res.append(str(s))
                else:
                    res.append(str(s) + '->' + str(tmp))
                s, tmp = nums[i], nums[i]
            i += 1
        if s == tmp:
            res.append(str(s))
        else:
            res.append(str(s) + '->' + str(tmp))
        return res

print Solution().summaryRanges([1,2])