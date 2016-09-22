# def numTrees(n):
#     res = 0
#     if n == 0 or n == 1:
#         return 1
#     else:
#         for i in range(n):
#             res += numTrees(i) * numTrees(n-i-1)
#     return res

def numTrees(n):
    res = [1, 1]
    for i in range(2, n+1):
        temp = 0
        for j in range(0, i):
            temp += res[j] * res[i-j-1]
        res.append(temp)
    return res[-1]




numTrees(4)