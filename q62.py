def uniquePaths(m, n):
    if m == 1 or n == 1:
        return 1
    res = [[1] * n]
    for i in range(1, m):
        temp = [1]
        for j in range(1, n):
            print('i',i,'j',j)
            temp.append(temp[j-1] + res[i-1][j])
        res.append(temp)
    return res[m-1][n-1]
uniquePaths(3,4)