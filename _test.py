def a(n):
    res = []
    help(n, 0, 0, res, '')
    return res

def help(max, l, r, res, cur):
    if len(cur) == 2 * max:
        res.append(cur)
    if l < max:
        help(max, l+1, r, res, cur+'(')
    if r < max:
        help(max, l, r+1, res, cur+')')

print len(a(4))