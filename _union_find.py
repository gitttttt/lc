class UF:

    def __init__(self, n):
        self.arr = [i for i in range(n)]
        self.count = n

    def count(self):
        return self.count

    def connected_qf(self, p, q):
        return self.find_qf(p) == self.find_qf(q)

    def connected_qu(self, p, q):
        return self.find_qu(p) == self.find_qu(q)

    def find_qf(self, p):
        return self.arr[p]

    def find_qu(self, p):
        while self.arr[p] != p:
            p = self.arr[p]
        return p

    def union_qf(self, p, q):
        pg = self.find_qf(p)
        qg = self.find_qf(q)
        if self.connected_qf(p, q):
            return
        for i in range(len(self.arr)):
            if self.arr[i] == pg:
                self.arr[i] = qg
        self.count -= 1

    def union_qu(self, p, q):
        pg = self.find_qu(p)
        qg = self.find_qu(q)
        if self.connected_qu(p, q):
            return
        self.arr[p] = q
        self.count -= 1

uf = UF(10)
add = [(0, 1), (1, 2), (0, 2)]
for i in add:
    uf.union_qu(i[0], i[1])
    print uf.arr
    print uf.count
