class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if len(data) == 1:
            return data[0] | (1 << 7) == 0
        head = data[0]
        i = 0
        while head & (1 << 7):
            i += 1
            head <<= 1
        if i > len(data):
            return False
        print i
        res = 0
        for i in range(1, i):
            if 128 <= data[i] < 192:
                res += (data[i] - 128)
            else:
                print 'dd'
                return False
        return res 


print Solution().validUtf8([240,162,138,147,145])
