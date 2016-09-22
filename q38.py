def countAndSay(n):
    if n == 1:
        return str(1)
    res = "1"
    temp = ""
    while n > 1:
        i, j = 0, 0
        while j < len(res):
            if res[i] == res[j]:
                j += 1
            else:
                temp += str(j-i)
                temp += str(res[i])
                i = j
                j += 1
        if i != j:
            temp += str(j-i)
            temp += str(res[i])
        res = temp
        temp = ""
        n -= 1
        print('x', res, n)
    return res

print(' ', countAndSay(5))