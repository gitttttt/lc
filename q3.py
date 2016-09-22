def lengthOfLongestSubstring(s):
    if len(s) < 2:
        return len(s)
    res, start, used = 0, 0, {}
    for i in range(len(s)):
        if s[i] in used and start <= used[s[i]]:
            start = used[s[i]] + 1
        else:
            res = max(res, i-start+1)
        used[s[i]] = i
        print used, start
    return res

print lengthOfLongestSubstring("tmmzuxt")


