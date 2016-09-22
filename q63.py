def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid[0]:
        return 0
    if len(obstacleGrid) == 1:
        if obstacleGrid[0].__contains__(1):
            return 0
        else:
            return 1
    if len(obstacleGrid[0]) == 1:
        if obstacleGrid.__contains__([1]):
            return 0
        else:
            return 1
    res, flag, temp = [], True, []
    for i in range(len(obstacleGrid[0])):
        if not flag:
            temp.append(0)
        elif obstacleGrid[0][i] == 1:
            flag = False
            temp.append(0)
        else:
            temp.append(1)
    res.append(temp)
    for i in range(1, len(obstacleGrid)):
        if obstacleGrid[i][0] == 0 and res[i-1][0] == 1:
            temp = [1]
        else:
            temp = [0]
        for j in range(1, len(obstacleGrid[i])):
            if obstacleGrid[i][j] == 1:
                temp.append(0)
            else:
                temp.append(temp[j-1]+res[i-1][j])
        res.append(temp)
    return res[len(obstacleGrid)-1][len(obstacleGrid[0])-1]

a = [[1, 0], [0, 0]]
print(uniquePathsWithObstacles(a))
