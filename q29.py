def divide(dividend, divisor):
    res = 0
    flag = (divisor > 0) ^ (dividend < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    d = divisor
    result = 0

    while dividend >= divisor:
        res = 0
        while dividend >= divisor:
            divisor <<= 1
            res += 1
        divisor >>= 1
        res -= 1
        result += 2 ** res
        dividend = dividend - divisor
        divisor = d
        print('d', dividend, divisor, result, res)

    return flag * result

print(divide(-2147483648,-1))
print(True ^ False)
