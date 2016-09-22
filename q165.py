class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        p1 = version1.count('.')
        p2 = version2.count('.')
        if p1 > p2:
            version2 += ".0" * (p1 - p2)
        if p1 < p2:
            version1 += ".0" * (p2 - p1)
        version1 = version1.split('.')
        version2 = version2.split('.')
        for i in range(len(version1)):
            if int(version1) > int(version2):
                return 1
            if int(version1) < int(version2):
                return -1
        return 0

print '1.1'.split(".")