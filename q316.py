def removeDuplicateLetters(s):
    tmp = {}
    res = []
    print(len(s))
    for i in range(len(s)):
        if i in tmp:
            if tmp[s[i]] == len(res)-1:
                continue
            elif res[tmp[s[i]]] > res[tmp[s[i]]+1]:
                res.pop(tmp[s[i]])
                res.append(s[i])
                tmp[s[i]] = len(res)-2
            else:
                continue
        else:
            res.append(s[i])
            tmp[s[i]] = len(res)-1

    return "".join(res)

print(removeDuplicateLetters("cbacdcbc"))