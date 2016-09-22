def wordPattern(pattern, str):
    p = list(pattern)
    s = str.split(' ')
    sets = {}
    for x in list(zip(p, s)):
        print(x)
        if not sets.__contains__(x[0]):
            sets[x[0]] = x[1]
        elif sets[x[0]] != x[1] and sets:
            return False
    sets.clear()
    for x in list(zip(s, p)):
        print(x)
        if not sets.__contains__(x[0]):
            sets[x[0]] = x[1]
        elif sets[x[0]] != x[1] and sets:
            return False

    return True

print(wordPattern("ab", "b c"))