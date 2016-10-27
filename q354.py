class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        http://www.cnblogs.com/grandyang/p/5568818.html
        not understand, iq zhuoji
        :type envelopes: List[List[int]]
        :rtype: int
        """
        nums = sorted(envelopes,
                      cmp = lambda x,y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        size = len(nums)
        print nums
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

Solution().maxEnvelopes([[5,100],[6,4],[6,3],[6,8]])