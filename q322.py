class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        res = [amount+1] + [amount+1 for _ in range(amount)]
        # print res
        for i in coins[::-1]:
            j = 1
            while j * i <= amount:
                res[i*j] = min(res[i*j], j)
                j += 1
        # print res
        for i in range(1, amount+1):
            if res[i] != 1:
                tmp = amount + 1
                for j in coins:
                    if j <= amount and res[j] != -1 and i-j >= 1 and res[i-j] != -1:
                        tmp = min(tmp, res[i-j] + 1)
                res[i] = tmp if tmp < amount+1 else -1
            # print i, res[i]
        return res[-1]

print Solution().coinChange([146,66,355,93,255,152,225,244,168,205]
,8069)

