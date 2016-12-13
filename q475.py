class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        i = 0
        j = 0
        res = 0
        while i < len(houses):
            while j < len(heaters) and houses[i] > heaters[j]:
                j += 1
            if j == len(heaters):
                res = max(res, abs(heaters[j-1]-houses[i]))
                break
            else:
                res = max(heaters[j]-houses[i], houses[i]-heaters[j-1], res)
        return res

hs = [1,2,3,4]
ht = [1,4]
print Solution().findRadius(hs, ht)