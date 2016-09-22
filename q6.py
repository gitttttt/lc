def convert(s, numRows):
    row, delta, res = 0, 1, [[], [], [], []]
    print(res)
    for i in s:
        res[row] += i
        row += delta
        if row >= numRows:
            row, delta = numRows-2, -1
        if row < 0:
            row, delta = 1, 1
        print(i, res)
    print(res)
convert("ABCDEFGH", 4)