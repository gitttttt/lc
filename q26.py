
def removeDuplicates(nums):
    for i, v in enumerate(nums[:-1]):
        print(nums[:-1])
        if nums[i] == nums[i+1]:
            j = i
            while j < len(nums)-1:
                nums[j] = nums[j+1]
                nums.pop()
                j += 1
    print(nums)
    return len(nums)

print(removeDuplicates([1,2,2,3,3,3,5]))