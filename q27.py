
def removeElement(nums, val):
    length = len(nums) - nums.count(val)
    while nums.__contains__(val):
        nums.remove(val)
    print(nums)
    return length

print(removeElement([1,2,2,3,3], 2))

