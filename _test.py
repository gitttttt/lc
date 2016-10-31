def fun(nums):
    res = []
    for i in nums:
        if nums[abs(i)-1] > 0:
            nums[abs(i)-1] = -nums[abs(i)-1]
        else:
            res.append(abs(i))
        print nums
    return res

print fun([10,2,5,10,9,1,1,4,3,7])

print map(abs, [1, -2, -3])