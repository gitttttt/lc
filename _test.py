def gen():
    for x in xrange(4):
        tmp = yield x
        if tmp == 'hello':
            print 'world'
        else:
            print str(tmp)

a = gen()
print a.next()
print()
print type(gen)
print a.next()