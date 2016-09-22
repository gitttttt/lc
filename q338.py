def countBits(num):
    res = [0]
    if num == 0:
        return res
    else:
        while True:
            for i in res[::1]:
                res.append(i+1)
                if len(res) == num+1:
                    return res
