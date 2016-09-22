import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        res = []
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1
        for v in heapq.nlargest(k, hashmap.values()):
            for k in hashmap:
                if hashmap[k] == v and k not in res:
                    res.append(k)
        return res

print Solution().topKFrequent([1,2], 2)