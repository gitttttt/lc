def hIndex(citations):
    citations.sort(reverse=True)
    print(citations)
    for k, v in enumerate(citations):
        if k >= v:
            return k

print(hIndex([3, 0, 6,1, 5]))