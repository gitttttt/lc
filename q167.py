class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(numbers)):
            left = i+1
            right = len(numbers)-1
            while left <= right:
                middle = (left + right) / 2
                if numbers[middle] + numbers[i] == target:
                    return [i+1, middle+1]
                elif numbers[middle] + numbers[i] < target:
                    left = middle+1
                else:
                    right = middle-1

print Solution().twoSum([1,2], 3)
