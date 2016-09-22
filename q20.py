def isValid(s):
    left = ['(', '[', '{']
    right = [')', ']', '}']
    stack = []
    for i in s:
        print i
        if i in left:
            stack.append(i)
        elif i in right > 0:
            if not stack:
                return False
            elif stack[-1] == left[right.index(i)]:
                stack.pop()
            else:
                return False
        else:
            return False
    return not stack

print(isValid(""))
