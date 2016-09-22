class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = []
        for i in range(len(nums)):
            if not tmp:
                tmp.append(nums[i])
            else:
                if nums[i] == tmp[-1]:
                    tmp.append(nums[i])
                else:
                    tmp.pop()
        return tmp[0]

print Solution().majorityElement([1,1,1,2,5,34,24,3,3,3,3])