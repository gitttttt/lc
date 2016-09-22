def dker_loop(l):
    if not l:
        return []
    if len(l) == 1:
        return l[0]
    res = l[0]
    for i in l[1::]:
        tmp = []
        for j in res:
            for k in i:
                tmp.append(j * k)
        res = tmp
    return res

def dker_recursion(l):
    if not l:
        return []
    if len(l) == 1:
        return l[0]
    res = []
    for i in dker_recursion(l[:-1:]):
        for j in l[-1]:
            res.append(i+j)
    return res

print dker_recursion([['1', '2'], ['3', '4'], ['5', '6']])