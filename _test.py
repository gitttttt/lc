_VALVE = 64


def big_integer_mul(x, y):
    if x.bit_length() <= _VALVE or y.bit_length() <= _VALVE:
        return x * y

    else:
        # calculates the size of the numbers
        m = max(x.bit_length(), y.bit_length())

        # split the digit sequences about the middle
        split_half = (m + 32) // 64 * 32
        mask = (1 << split_half) - 1
        x_low = x & mask
        y_low = y & mask
        x_high = x >> split_half
        y_high = y >> split_half

        # 3 calls made to numbers approximately half the size
        z0 = big_integer_mul(x_low, y_low)
        z1 = big_integer_mul(x_low + x_high, y_low + y_high)
        z2 = big_integer_mul(x_high, y_high)

        return (((z2 << split_half) + (z1 - z2 - z0)) << split_half) + z0

a = 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111
b = 222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
print a.bit_length(), b.bit_length()
print big_integer_mul(a, b)

class a:
    def __call__(self, *args, **kwargs):
        print args, kwargs
        return 1

aa = a()
print aa(1,a=15)

