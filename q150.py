import re

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        res = []
        for i in tokens:
            print res
            if re.match(r'^-?\d+$', str(i)):
                res.append(int(i))
            else:
                left = res.pop()
                right = res.pop()
                if i == "+":
                    res.append(left+right)
                if i == "-":
                    res.append(right-left)
                if i == "*":
                    res.append(left*right)
                if i == "/":
                    f1 = -1 if right < 0 else 1
                    f2 = -1 if left < 0 else 1
                    res.append(f1*f2*(abs(right)/abs(left)))
        return res[0]

#向上取整 向下取整 向0取整

print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])