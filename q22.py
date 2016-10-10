def generateParenthesis(n):
    res = []
    res.append([""])
    for i in range(1, n+1):
        tmp = []
        for j in range(i):
                left, right = res[j], res[i-1-j]
                for l in left:
                    for r in right:
                        tmp.append("(" + l + ")" + r)
        res.append(tmp)
    return res[-1]

print generateParenthesis(3)
