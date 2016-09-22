def groupAnagrams(strs):
    if not strs:
        return [[]]
    maps = {}
    for s in strs:
        if str(sorted(s)) in maps:
            maps[str(sorted(s))].append(s)
        else:
            maps[str(sorted(s))] = [s]
    values = maps.values()
    for value in values:
        value.sort()
    return list(values)

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))