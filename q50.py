import sys

# def myPow(x, n):
#     def tail(a, b, res):
#         if b == 0:
#             return res
#         if b > 0:
#             return tail(a, b - 1, res * a)
#         else:
#             return tail(a, b + 1, res / b)
#     return tail(x, n, 1)

def myPow(x, n):
    res = 1
    if n > 0:
        for i in range(n):
            res *= x
            if res == 0:
                return 0
    else:
        for i in range(n):
            res /= x
            if res == 0:
                return 0
    return res

print(myPow(2.0, -2147483648))