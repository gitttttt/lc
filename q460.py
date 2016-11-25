class LFUCache(object):

    def __init__(self, capacity):
        """

        :type capacity: int
        """
        self.c = capacity
        self.used = []
        self.frequency = {}
        self.m = {}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.frequency[key] += 1
        self.used.remove(key)
        self.used.append(key)
        return self.m[key]



    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if len(self.m) >= self.c:
            v = min(self.frequency.values())
            tmp = []
            for i in self.m:
                if self.m[i] == v:
                    tmp.append(i)
            r = 0
            if len(tmp) == 1:
                r = tmp[0]
            else:
                for u in self.used[::-1]:
                    if u in tmp:
                        r = u
                        break
                self.used.remove(r)
                self.frequency.pop(r)
        self.frequency[key] = 1
        self.used.append(key)
        self.m[key] = value




        # Your LFUCache object will be instantiated and called as such:
        # obj = LFUCache(capacity)
        # param_1 = obj.get(key)
        # obj.set(key,value)