
def threeSums(nums):
    # if len(nums) < 3:
    #     return None
    # res = []
    # for (i1, v1) in enumerate(nums):
    #     for (i2, v2) in enumerate(nums[i1+1:]):
    #         for (i3, v3) in enumerate(nums[i1+i2+1:]):
    #             if v1+v2+v3 == 0 and not res.__contains__(sorted([v1,v2,v3])):
    #                 res.append(sorted([v1, v2, v3]))
    # return res
    if len(nums) < 3:
        return None
    sorted(nums)
    print(nums)
    i, j, k, res = 0, 1, len(nums)-1, []
    while i < len(nums)-2:
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i]+nums[j]+nums[k] > 0:
                k -= 1
            elif nums[i]+nums[j]+nums[k] < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j+=1
                k-=1
                while j<k and nums[j] == nums[j-1]:
                    j += 1
                while j<k and nums[k] == nums[k+1]:
                    k -= 1
        while nums[i] == nums[i+1] and i < len(nums)-2:
            i += 1
        i+=1
    return res


a = [1,2,3,2,1]
print(threeSums(a))
help(list.reverse)
