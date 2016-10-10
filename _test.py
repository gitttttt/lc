def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    base = 1
    right = 0
    origin = x
    while x > 0:
        base *= 10
        x /= 10
    base /= 10
    while origin > 0:
        left = origin / base
        right = origin % 10
        if left != right:
            return False
        origin = (origin - right - base * left) / 10
        base /= 100
        print left, right, origin
    return True

print isPalindrome(222)