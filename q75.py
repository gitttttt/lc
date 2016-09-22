import time

def sortColors(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

nums = [0,2,1,2,1,2,2,1,0]
sortColors(nums)
print(nums)