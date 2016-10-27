class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        nums = sorted(envelopes,
                      cmp = lambda x,y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) / 2
                if dp[mid][1] < nums[x][1]:
                    low = mid + 1
                else:
                    high = mid - 1
            print dp
            if low < len(dp):
                dp[low] = nums[x]
            else:
                dp.append(nums[x])
            print dp
            print
        return len(dp)

Solution().maxEnvelopes([[1,2], [2,4], [2,3], [3,5]])