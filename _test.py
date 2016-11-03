arr = [[7,0], [4,4], [7,1], [5,2], [6,1], [5,1]]

def s(x, y):
    if x[0] == y[0]:
        return x[1]-y[1]
    else:
        return y[0] - x[0]
arr.sort(cmp=s)

print arr
tmp = []
a = [1,2,3]
a.insert(1,33)
print a