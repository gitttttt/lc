def mySqrt(x):
    left, right = x/2, x
    while left < right:
        if left * left < x:
            left = (left + right) / 2
        else:
            right = (left + right) / 2