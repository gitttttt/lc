# def candy(ratings):
#     if not ratings:
#         return 0
#     elif len(ratings) == 1:
#         return 1
#     tmp = []
#     if ratings[0] <= ratings[1]:
#         tmp.append(1)
#     else:
#         tmp.append(2)
#     for i in range(1, len(ratings)-1):
#         if ratings[i] > ratings[i-1] and ratings[i] > ratings[i+1]:
#             tmp.append(tmp[i-1] + 1)
#         else:
#             tmp.append(1)
#     if ratings[-1] > ratings[-2]:
#         tmp.append(tmp[-1] + 1)
#     else:
#         tmp.append(1)
#     return sum(tmp)

def candy(ratings):
    length = len(ratings)
    if length <= 1:
        return length
    else:
        tmp = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i-1]:
                tmp[i] = tmp[i-1] + 1
        for i in range(length-1, 0):
            if ratings[i-1] > ratings[i]:
                tmp[i-1] = max(tmp[i-1], tmp[i]+1)
        return sum(tmp)

print(candy([1,2,2]))