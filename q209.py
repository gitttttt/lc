class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # min_len = len(nums) + 1
        # for i, v in enumerate(nums):
        #     if v >= s:
        #         min_len = 1
        #         break
        #     else:
        #         j, sum_ = i + 1, v
        #         while j <= len(nums) - 1:
        #             sum_ += nums[j]
        #             if sum_ >= s:
        #                 min_len = min(min_len, j-i+1)
        #             j += 1
        #     print i, min_len
        # return min_len if min_len <= len(nums) else 0
        start, end, sum_, min_ = 0, 0, 0, len(nums) + 1
        while end < len(nums) and start < len(nums):
            while sum_ < s and end < len(nums):
                sum_ += nums[end]
                end += 1
            while sum_ >= s and start < len(nums):
                sum_ -= nums[start]
                start += 1
            min_ = min(min_, end - start + 1)
            print min_
        return min_ if min_ <= len(nums) else 0


print Solution().minSubArrayLen(15, [1, 2, 3, 4, 5])

