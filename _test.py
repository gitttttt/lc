i1 = 0
for i in 'abcz':
    i1 += 1 << (ord(i) - ord('a'))
print ord('a') - ord('b'), ord('a')