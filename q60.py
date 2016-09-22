def getPermutation(n, k):
    temp = [1] * n
    num = list(range(1, n+1))
    print(num)
    for i in range(1, n):
        temp[i] = temp[i-1] * (i+1)
    res = ""
    for i in range(n):
        m = int((k-1) / temp[n-i-2]) + 1
        number = num[m-1]
        res += str(number)
        num.remove(number)
        k -= (m-1) * temp[n-i-2]
    return res


getPermutation(2, 22)

# def get(n):
#     res = []
#     if n > 1:
#         temp = get(n-1)
#         for t in temp:
#             for i in range(n):
#                 res.append(t[:-i]+str(n)+t[-i:])
#     else:
#         res = ["1"]
#     print(res)
#     return res
#
# get(3)