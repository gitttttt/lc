from collections import deque

def infix_to_postfix(s):
    w = {'+': 1, '-': 1, '*': 2, '/': 2}
    S = deque()
    t = []
    n = len(s)
    i = 0
    while i < n:
        c = s[i]
        if c.isdigit():
            j = i
            while j < n and s[j].isdigit():
                j += 1
            t.append(s[i:j])
            i = j
        elif c == '(':
            S.append(c)
            i += 1
        elif c == ')':
            while S[-1] != '(':
                t.append(S.pop())
            S.pop()
            i += 1
        else:  # operators
            while S and S[-1] != '(' and w[S[-1]] >= w[c]:
                t.append(S.pop())
            S.append(c)
            i += 1
        print S
        print t
    while S:
        t.append(S.pop())
    return t

print infix_to_postfix('9+(3-1)*3+10/2')