def minimumTotal(triangle):

    res = [triangle[0]]
    for i1, v1 in enumerate(triangle[1:]):
        temp = [v1[0]+res[i1][0]]
        for i2, v2 in enumerate(v1[1:-1]):
            temp.append(v2 + min(res[i1][i2], res[i1][i2+1]))
        temp.append(v1[-1]+res[i1][-1])
        res.append(temp)
    return min(res[-1])

a=[
    [2],
]
print(minimumTotal(a))