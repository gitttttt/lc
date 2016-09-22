def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    if len(nums) == 3:
        return max([nums[0]+nums[2], nums[1]])
    res = [nums[0], max(nums[0], nums[1])]
    for x in range(2, len(nums)):
        res.append(max(res[x-2]+nums[x], res[x-1]))
    return res[:-1]

print(rob([]))
