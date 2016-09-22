def strStr(haystack, needle):
    h, n = len(haystack), len(needle)
    for i in range(h-n+1):
        if needle == haystack[i:i+n]:
            return i
    return -1

print(strStr("aa", "aa"))