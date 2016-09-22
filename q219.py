def containsNearbyDuplicate(nums, k):
    numDict = dict()
    for x in range(len(nums)):
        idx = numDict.get(nums[x])
        print(idx, x)
        if idx >= 0 and x - idx <= k:
            return True
        numDict[nums[x]] = x
    return False

print(containsNearbyDuplicate([1,2,3], 4))