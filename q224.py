class Solution(object):
    def calculate(self, s):
        """
        :type l: str
        :rtype: int
        """
        l = []
        for i in s:
            if i in ['(', ')', '+', '-']:
                l.append(i)
            else:
                if not l:
                    l.append(int(i))
                elif type(l[-1]) == int:
                    l[-1] = l[-1] * 10 + int(i)
                else:
                    l.append(int(i))
        print l
        stack = []
        for i in range(len(l)):
            if l[i] in ['+', '-']:
                stack.append(l[i])
            elif l[i] == ')':
                data = stack.pop()
                stack.pop()
                if not stack:
                    stack.append(data)
                else:
                    sym = stack.pop()
                    data2 = stack.pop()
                    if sym == "+":
                        stack.append(data2 + data)
                    if sym == "-":
                        stack.append(data2 - data)
            elif l[i] == '(':
                stack.append(l[i])
            else:
                if not stack:
                    stack.append(l[i])
                elif stack[-1] == '(':
                    stack.append(l[i])
                else:
                    if stack[-1] in ['+', '-']:
                        sym = stack.pop()
                        data = stack.pop()
                        if sym == "+":
                            stack.append(int(l[i]) + data)
                        if sym == "-":
                            stack.append(int(l[i]) - data)
                    else:
                        data = stack.pop()
                        stack.append(str(10 * data + l[i]))
            print stack
        return int(stack[-1])


print Solution().calculate('1-11')
