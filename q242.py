def is_anagram(s, t):
    m1, m2 = {}, {}
    if len(s) != len(t):
        return False
    for i in s:
        if i in m1:
            m1[i] += 1
        else:
            m1[i] = 1
    for i in t:
        if i in m2:
            m2[i] += 1
        else:
            m2[i] = 1
    return m1 == m2

{1:2}.has_key
