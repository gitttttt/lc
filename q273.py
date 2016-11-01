class Solution(object):

    def __init__(self):
        self.word = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        self.teen = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.teens = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.jz = ['', ' Thousand', ' Million', ' Billion']


    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        num = str(num)
        res = []
        jz = 0
        for i in range(len(num))[::-3]:
            s = i-2 if i-2 > 0 else 0
            tmp = num[s:i+1]
            if len(tmp) == 3:
                res.append(self.part(tmp) + self.jz[jz] + ' ')
            else:
                res.append(self.p2(tmp) + self.jz[jz] + ' ')
            jz += 1
        return ''.join(res[::-1]).lstrip()



    def part(self, num):
        res = []
        if num[0] != '0':
            res.append(self.word[int(num[0])] + ' Hundred ')
        if num[1:] != '00':
            res.append(self.p2(num[1:]))
        return ''.join(res).rstrip()

    def p2(self, num):
        if len(num) == 1:
            return self.word[int(num[0])]
        if num[-1] == '0':
            return self.teens[int(num[0])]
        else:
            if num[0] == '1':
                return self.teen[int(num[1])]
            else:
                return self.teens[int(num[0])] + ' ' + self.word[int(num[1])]

print Solution().numberToWords(100811)
