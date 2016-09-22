def containsDuplicate(nums):
    set_ = set()
    for i in nums:
        if set_.__contains__(i):
            return True
        set_.add(i)
    return False

print(containsDuplicate([1,2,2,3]))