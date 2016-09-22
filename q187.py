def findRepeatedDnaSequences(s):
    if len(s) <= 10:
        return []
    res, sets = set(), set()
    for i in range(len(s)-9):
        str = s[i: i+10]
        if sets.__contains__(str):
            res.add(str)
        else:
            sets.add(str)
    return list(res)

print(str(1221).count("1"))

print(findRepeatedDnaSequences("AAAAAAAAAAAA"))
