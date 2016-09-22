def palindromePairs(words):
    def isPair(str):
        return str.__eq__(str[::-1])
    if not words:
        return []
    res = []
    maps = dict(zip(words, range(len(words))))
    empty_index = maps.get("", -1)
    for s in maps:
        if s != '' and empty_index != -1 and isPair(s):
            res.append([empty_index, maps[s]])
            res.append([maps[s], empty_index])
        if s[::-1] in maps and maps[s] != maps[s[::-1]]:
            res.append([maps[s], maps[s[::-1]]])
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            if isPair(left) and right[::-1] in maps:
                print(s, left, right, i, '1')
                res.append([maps[right[::-1]], maps[s]])
            if isPair(right) and left[::-1] in maps:
                print(s, left, right, i, '2')
                res.append([maps[s], maps[left[::-1]]])
    return res

print(palindromePairs(["a","b","c","ab","ac","aa"]))