def removeDuplicateLetters(s):
    m = {}
    for i in s:
        if i not in s:
            s[i] = 0
        s[i] += 1


print(removeDuplicateLetters("cbacdcbc"))