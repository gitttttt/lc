class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        if length % 2:
            return self.find(nums1, nums2, (length+1)/2)
        else:
            return (self.find(nums1, nums2, length/2) + self.find(nums1, nums2, length/2+1)) / 2.0

    def find(self, a, b, k):
        if len(a) > len(b):
            return self.find(b, a, k)
        if not a:
            return b[k-1]
        if k == 1:
            return min(a[0], b[0])
        pa = min(len(a), k/2)
        pb = k - pa
        if a[pa-1] < b[pb-1]:
            return self.find(a[pa::1], b, k-pa)
        elif a[pa-1] > b[pb-1]:
            return self.find(a, b[pb::1], k-pb)
        else:
            return a[pa-1]


print(Solution().findMedianSortedArrays([1], [2]))
