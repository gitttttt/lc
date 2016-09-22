class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        return str(self.x) + " " + str(self.y)

def maxPoints(points):
    if len(points) < 3:
        return len(points)
    sets = {}
    for p in points:
        if sets.__contains__(p.x):
            sets[p.x] += 1
        else:
            sets[p.x] = 1
    max_x = max(sets.values())
    max_k = 0
    for k1, p1 in enumerate(points):
        sets.clear()
        points_copy = points[:]
        del points_copy[k1]
        temp = 0
        for p2 in points_copy:
            if not p1.x == p2.x:
                k = (p2.y - p1.y) / (p2.x - p1.x)
                if sets.__contains__(k):
                    sets[k] += 1
                else:
                    sets[k] = 1
            elif p1.y == p2.y:
                temp += 1
        if sets:
            max_k = max(max_k, max(sets.values())+1+temp)
    return max(max_x, max_k)

a = [Point(84,250), Point(0,0), Point(1,0), Point(0,-70),Point(0, -70), Point(1,-1), Point(21,10), Point(42,90), Point(-42, -230)]
print(maxPoints(a))