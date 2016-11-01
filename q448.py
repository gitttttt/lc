class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # res = []
        # for i in range(len(nums)):
        #     index = abs(nums[i]) - 1
        #     if nums[index] > 0:
        #         nums[index] = -nums[index]
        #     print nums
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         res.append(i+1)
        # return res

        res = []
        for i in nums:
            if nums[abs(i)-1] > 0:
                nums[abs(i)-1] = -nums[abs(i)-1]
            else:
                res.append(abs(i))
                print i
            print nums
        return res

print Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
