import heapq

h = []
n = 5
while n >= 0:
    heapq.heappush(h, n)
    print h
    n -= 1
print h
print heapq.nsmallest(5, h)

print [1,2,3][:-1]