def addBinary(a, b):
    res, tmp, carry = "", 0, 0
    while a and b:
        temp_a = int(a[-1])
        temp_b = int(b[-1])
        tmp = temp_a + temp_b + carry
        if tmp >= 2:
            res = str(tmp-2) + res
            carry = 1
        else:
            res = str(tmp) + res
            carry = 0
        a, b = a[:-1], b[:-1]
    while a:
        temp_a = int(a[-1])
        tmp = temp_a + carry
        if tmp == 2:
            res = "0" + res
            carry = 1
        else:
            res = str(tmp) + res
            carry = 0
        a = a[:-1]
    while b:
        temp_b = int(b[-1])
        tmp = temp_b + carry
        if tmp == 2:
            res = "0" + res
            carry = 1
        else:
            res = str(tmp) + res
            carry = 0
        b = b[:-1]
    if carry:
        res = "1" + res
    return res

print(addBinary('101000', '100'))