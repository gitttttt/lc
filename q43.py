def multiply(num1, num2):
    flag = 1
    if num1[0] == "-":
        flag = -flag
        num1 = num1[1:]
    if "." in num1:
        num1 = float(num1)
    else:
        num1 = int(num1)
    if num2[0] == "-":
        flag = -flag
        num2 = num2[1:]
    if "." in num2:
        num2 = float(num2)
    else:
        num2 = int(num2)
    return str(flag * num1 * num2)

print(multiply('22', '21'))