# def lengthOfLongestSubstring(s):
#     if len(s) < 2:
#         return len(s)
#     res, start, used = 0, 0, {}
#     for i in range(len(s)):
#         if s[i] in used and start <= used[s[i]]:
#             start = used[s[i]] + 1
#         else:
#             res = max(res, i-start+1)
#         used[s[i]] = i
#         print used, start
#     return res

def lengthOfLongestSubstring(s):

    # i, j = 0, 0
    # res = 0
    # used = set()
    # while i < len(s) and j < len(s):
    #     if s[j] in used:
    #         used.remove(s[i])
    #         i += 1
    #     else:
    #         used.add(s[j])
    #         res = max(res, j-i+1)
    #         j += 1
    #     print res, used
    # return res
    used = {}
    res = 0
    i, j = 0, 0
    while i < len(s) and j < len(s):
        if s[j] in used:
            i = used[s[j]]+1
        res = max(res, j-i+1)
        used[s[j]] = j
        j += 1
    return res



print lengthOfLongestSubstring("abba")


