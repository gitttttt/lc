def diffWaysToCompute(input):
    tmp = {}
    return mid(input, tmp)

def mid(input, tmp):
    res = []
    for i, v in enumerate(input):
        if v == "+" or v == "-" or v == "*":
            part1, part2 = input[:i], input[i+1:]
            res1, res2 = [], []
            if part1 in tmp:
                res1 = tmp[part1]
            else:
                res1 = mid(part1, tmp)
            if part2 in tmp:
                res2 = tmp[part2]
            else:
                res2 = mid(part2, tmp)
            for p1 in res1:
                for p2 in res2:
                    if v == "+":
                        res.append(p1+p2)
                    if v == "-":
                        res.append(p1-p2)
                    if v == "*":
                        res.append(p1*p2)
    if not res:
        res.append(int(input))
    tmp[input] = res
    return res

print(diffWaysToCompute("1+2*2-1"))


