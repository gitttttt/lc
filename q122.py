def maxProfit(prices):
    if len(prices) < 2:
        return 0
    max_ = 0
    for i, v in enumerate(prices[1:]):
        if v > prices[i]:
            print((v-prices[i]))
            max_ += (v-prices[i])
    return max_
a = []
for i in range(100000):
    a.append(i)
print(a)
print(maxProfit(a))
map()