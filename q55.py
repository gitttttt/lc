def can_jump(nums):
    if len(nums) == 0 or (len(nums) == 1 and nums[0] != 0):
        return True
    max_step = nums[0]
    for i, v in enumerate(nums):
        max_step -= 1
        if nums[i] > max_step:
            max_step = nums[i]
        if i + max_step >= len(nums)-1:
            return True
        if max_step == 0:
            return False

print(can_jump([1, 2, 3, 1, 0, 1]))
