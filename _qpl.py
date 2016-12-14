def qpl_r(list):
    if not list:
        return [[]]
    if len(list) == 1:
        return [[list[0]]]
    res = []
    for i in range(len(list)):
        lcopy = list[::]
        lcopy.pop(i)
        res += map(lambda x: x + [list[i]], qpl_r(lcopy))
        #res.extend(map(lambda x: x + [list[i]], qpl_r(lcopy)) also okay
    return res

def qzh_i(list):
    res = []
    for i in range(1 << len(list)):
        tmp = []
        num = i
        count = 0
        while num > 0:
            if num & 1:
                tmp.append(list[count])
            num >>= 1
            count += 1
        res.append(tmp)
    return res


# def qpl_i(list):
#     res = [list]
#     for i in range(len(list)):
#         for j in range(i+1, len(list)):
#             l = list[::]
#             l[i], l[j] = l[j], l[i]
#             res.append(l)
#     return res

def qzh_r(list):
    if not list:
        return [[]]
    rest = list[1::]
    return qzh_r(rest) + map(lambda x: x + [list[0]], qzh_r(rest))

print qzh_r([1,2,3,4])