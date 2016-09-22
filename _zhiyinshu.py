import math

def zyf(n):
    if n<=2:
        return {n:1}
    res = {}
    for i in range(2, int(math.sqrt(n))):
        while not n % i:
            if i not in res:
                res[i] = 0
            n /= i
            res[i] += 1
    return res

print zyf(2)