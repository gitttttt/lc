def isNumber(s):
    symbol, point, e = True, True, True
    for i in s:
        if i == "":
            continue
        elif i == "+" or i == "-":
            if symbol:
                symbol = False
            else:
                return False
        elif i == ".":
            if point:
                point = False
            else:
                return False
        elif i == "e" or i == "E":
            point = True
            if e:
                e = False
            else:
                return False
        elif "9" >= i >= "0":
            continue
        else:
            return False
    return True

print(isNumber(".12e1.3"))