from collections import deque

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        w = {'+': 1, '-': 1, '*': 2, '/': 2}

        def trans(s):
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
                else:  # operators
                    while S and w[S[-1]] >= w[c]:
                        t.append(S.pop())
                    S.append(c)
                    i += 1
            while S:
                t.append(S.pop())
            return t

        def eval_postfix(t):
            S = deque()
            for item in t:
                if item[0].isdigit():
                    S.append(item)
                else:
                    op2 = int(S.pop())
                    op1 = int(S.pop())
                    if item == '+':
                        S.append(op1+op2)
                    elif item == '-':
                        S.append(op1-op2)
                    elif item == '*':  # *
                        S.append(op1*op2)
                    else:  # *
                        if op1 * op2 > 0:
                            S.append(abs(op1)/abs(op2))
                        else:
                            S.append(-abs(op1)/abs(op2))
            return int(S[-1])
        s = s.replace(' ', '')
        if not s:
            return 0
        return eval_postfix(trans(s))