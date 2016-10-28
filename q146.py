class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.l = capacity
        self.history = []
        self.map = {}


    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.map:
            return -1
        self.history.remove(key)
        self.history.append(key)
        return self.map[key]


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.map:
            self.history.remove(key)
            self.history.append(key)
            self.map[key] = value
        else:
            if len(self.history) == self.l:
                k = self.history.pop(0)
                self.map.pop(k)
            self.history.append(key)
            self.map[key] = value
