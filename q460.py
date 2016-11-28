import sys

class LFUCache(object):

    def __init__(self, capacity):
        """

        :type capacity: int
        """
        self.c = capacity
        self.used = []
        self.f = {}
        self.m = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.m:
            return -1
        self.f[key] += 1
        self.used.remove(key)
        self.used.append(key)
        return self.m[key]



    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.c == 0:
            return
        if key in self.f:
            self.f[key] += 1
            self.used.remove(key)
            self.used.append(key)
        else:
            if len(self.m) >= self.c:
                minn = sys.maxint
                tmp = []
                for i in self.f:
                    if self.f[i] < minn:
                        tmp = [self.f[i]]
                        minn = self.f[i]
                    elif self.f[i] == minn:
                        tmp.append(self.f[i])
                r = 0
                if len(tmp) == 1:
                    r = tmp[0]
                else:
                    for u in self.used[::-1]:
                        if u in tmp:
                            r = u
                            break
                    self.used.remove(r)
                    self.f.pop(r)
            self.f[key] = 1
            self.used.append(key)
        self.m[key] = value
