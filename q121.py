def maxProfit(prices):
    if not prices or len(prices) < 2:
        return 0
    max_price, min_price, i = 0, prices[0], 1
    while i < len(prices):
        min_price = min(min_price, prices[i])
        max_price = max(max_price, prices[i]-min_price)
        i += 1
    return max_price

print(maxProfit([5,4,3]))
