import itertools

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) <=1:
            return list(digits)
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = kvmaps[digits[0]]
        for i in digits[1::]:
            tmp = []
            for j in kvmaps[i]:
                for k in res:
                    tmp.append(k + j)
            res = tmp
        print len(res)


Solution().letterCombinations("234")
