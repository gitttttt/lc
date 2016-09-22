def firstMissingPositive(nums):
    if not len(nums):
        return 1
    length = max(nums)
    res = [0 for i in range(length)]
    for i in nums:
        res[i-1] += 1
    for i, v in enumerate(res):
        if v == 0:
            return i+1
    return max(nums)+1

print(firstMissingPositive([1,2,3,5]))