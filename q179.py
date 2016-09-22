def largestNumber(nums):

    def part(n1, n2):
        s1, s2 = str(n1), str(n2)
        return 1 if s1+s2 > s2+s1 else 0 if s1+s2 == s2+s1 else -1

    print(part(1,2))
    nums.sort(cmp=lambda x, y: part(x, y))
    return "".join(map(str, nums))

print(largestNumber([1,13,23,22]))