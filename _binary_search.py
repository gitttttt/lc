# nums = [12,22,1,3]
# print(sorted(nums, key=lambda x: str(x)[0],  reverse=True))
#
# print(sum([1,2,3,4,5,6][1:4:1]))
def binary(nums, target):
    left, right = 0, len(nums) - 1
    middle = (left + right) / 2
    while left <= right:
        if nums[middle] == target:
            a, b = middle, middle
            while a >= 0 and nums[a] == target:
                a -= 1
            while b <= len(nums)-1 and nums[b] == target:
                b += 1
            return [a+1, b-1]
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
        middle = (left + right) / 2
    return [-1, -1]

# def binaryLeft(nums, target):
#     left, right = 0, len(nums) - 1
#     middle = (left + right) / 2
#     while left <= right:
#         if nums[middle] < target:
#             left = middle + 1
#         else:
#             right = middle
#             if middle == 0 or nums[middle-1] != target:
#                 return middle
#         middle = (left + right) / 2
#     return -1
#
# def binaryRight(nums, target):
#     left, right = 0, len(nums) - 1
#     middle = (left + right) / 2
#     while left < right:
#         if nums[middle] > target:
#             right = middle - 1
#         else:
#             left = middle
#             if middle == len(nums)-1 or nums[middle+1] != target:
#                 return middle
#         middle = (left + right) / 2
#     return -1



print binary([1,1,1,2,2,2,3,5,6], 2)