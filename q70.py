def climbStairs(n):
    if n < 4:
        return n
    res = [0, 1, 2, 3]
    for x in range(4, n+1):
        res.append(res[x-1]+res[x-2])
    return res[n]

# for x in range(10):
#     print(climbStairs(x))

print(climbStairs(10))