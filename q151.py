def reverseWords(s):
    s = s.lstrip(" ").rstrip(" ").split(" ")
    while "" in s:
        s.remove("")
    s.reverse()
    return " ".join(s)

print(reverseWords(" a b    c"))