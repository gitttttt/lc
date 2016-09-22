
def fourSums(nums, target):
    # if len(nums) < 3:
    #     return None
    # res = []
    # for (i1, v1) in enumerate(nums):
    #     for (i2, v2) in enumerate(nums[i1+1:]):
    #         for (i3, v3) in enumerate(nums[i1+i2+1:]):
    #             if v1+v2+v3 == 0 and not res.__contains__(sorted([v1,v2,v3])):
    #                 res.append(sorted([v1, v2, v3]))
    # return res
    if len(nums) < 4:
        return None
    nums.sort()
    i, j, k, m, res = 0, 1, 2, len(nums)-1, []
    while i < len(nums)-3:
        j = i + 1
        m = len(nums) - 1
        while j < len(nums)-2:
            k = j + 1
            m = len(nums) - 1
            while k < m:
                print(nums[i], nums[j], nums[k], nums[m])
                if nums[i]+nums[j]+nums[k]+nums[m] > target:
                    m -= 1
                elif nums[i]+nums[j]+nums[k]+nums[m] < target:
                    k += 1
                else:
                    res.append([nums[i], nums[j], nums[k], nums[m]])
                    k += 1
                    m -= 1
                    while k < m and nums[k] == nums[k-1]:
                        k += 1
                    while k < m and nums[m] == nums[m+1]:
                        m -= 1
            while nums[j] == nums[j+1] and j < len(nums)-2:
                j += 1
            j += 1
        while nums[i] == nums[i+1] and i < len(nums)-3:
            i += 1
        i += 1
    return res


a = [1,2,3,2,1]
print(fourSums([1,0,-1,0,-2,2], 0))