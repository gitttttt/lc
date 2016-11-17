class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = 0
        for i in range(max(0, k-len(nums2)), min(k, len(nums1))+1):
            a = self.get(nums1, i)
            b = self.get(nums2, k-i)
            print a, b
            print self.merge(a, b)
            tmp = int(''.join(map(str, self.merge(a, b))))
            if tmp > res:
                res = tmp
        return res

    def get(self, arr, k):
        tmp = []
        for i in range(len(arr)):
            if not tmp:
                tmp.append(arr[i])
            elif tmp[-1] >= arr[i]:
                tmp.append(arr[i])
            else:
                while tmp and tmp[-1] < arr[i] and len(tmp) + len(arr) - i > k:
                    tmp.pop()
                tmp.append(arr[i])
        return tmp[:k]

    def merge(self, arr1, arr2):
        tmp = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                tmp.append(arr1[i])
                i += 1
            elif arr1[i] < arr2[j]:
                tmp.append(arr2[j])
                j += 1
            else:
                pass

        while i < len(arr1):
            tmp.append(arr1[i])
            i += 1
        while j < len(arr2):
            tmp.append(arr2[j])
            j += 1
        return tmp

    def mergeMax(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            if nums1 > nums2:
                ans += nums1[0],
                nums1 = nums1[1:]
            else:
                ans += nums2[0],
                nums2 = nums2[1:]
            print ans, nums1, nums2
        return ans

nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
print Solution().mergeMax(nums2, nums1)