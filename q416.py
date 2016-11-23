class Solution(object):

    def __init__(self):
        self.flag = False

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2:
            return False
        res = []

        self.bs(nums, 0, [], res, s/2, self.flag)
        return self.flag

    def bs(self, arr, begin, cur, res, t, flag):
        if not self.flag:
            if sum(cur) == t:
                self.flag = True
                return
            elif sum(cur) < t:
                for i in range(begin, len(arr)):
                    cur.append(arr[i])
                    self.bs(arr, i+1, cur, res, t, self.flag)
                    cur.pop()

a = [1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100,99,100]
print len(a)
print Solution().canPartition(a)