def restoreIpAddresses(s):
    length = len(s)
    res = []
    for i in range(1, length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):

                a, b, c, d = s[:i],s[i:j],s[j:k],s[k:]

                if isIp(a) and isIp(b) and isIp(c) and isIp(d):
                    print(a, b, c, d)
                    res.append(".".join([a,b,c,d]))
    print(res)

def isIp(x):
    return 0 <= int(x) < 266 and not (len(x) > 1 and x[0] == '0')

print("   000256 ".lstrip(" ").rstrip(" "))