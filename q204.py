# def countPrimes(n):
#     res = 0
#     if n <= 2:
#         return 0
#     if n == 3:
#         return 1
#     if n % 2:
#         countPrimes(n-2) + isPrime(n)
#     else:
#         countPrimes(n-2) + isPrime(n-1)
#     return res
#
#
#
# def isPrime(n):
#     if n == 2:
#         return 1
#     i = 2
#     while i <= sqrt(n):
#         if not n % i:
#             print(n, ' ', 0)
#             return 0
#         else:
#             None
#         i += 1
#     return 1
#
# print(countPrimes(100)+1)


def is_prime(n):
    res, i = [False] * n, 2
    while i < n:
        j = i
        while i * j < n:
            if not res[i * j]:
                res[i * j] = True
            j += 1
        i += 1
    print(res)
    return res.count(False)

print(sum([True, True, False]))
