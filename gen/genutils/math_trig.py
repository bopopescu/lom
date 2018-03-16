import gen.genutils.math_factors as mf

def reduce2r(n, d):
    return n - n // (2 * d) * (2 * d), d

def invert_a(n, d):
    if n < 0:
        return mf.s_fraction((2 * d - n, d))
    else:
        return n, d

def get_table_sin(n, d):

    n, d = reduce2r(n, d)
    n, d = invert_a(n, d)

    if n == 0 or (d == 1):
        return "0"

    if d == 2:
        return "0" if n % 2 == 0 else ("1" if n % 4 == 1 else "-1")

    if d == 3:
        if n in [3]:
            return "0"
        if n in [1, 2]:
            return "k(3)/2"
        if n in [4, 5]:
            return "-k(3)/2"

    if d == 4:
        if n in [4]:
            return "0"
        if n in [2]:
            return "1"
        if n in [6]:
            return "-1"
        if n in [1, 3]:
            return "k(2)/2"
        if n in [5, 7]:
            return "-k(2)/2"

    if d == 6:
        if n in [6]:
            return "0"
        if n in [3]:
            return "1"
        if n in [9]:
            return "-1"
        if n in [1, 5]:
            return "1/2"
        if n in [7, 11]:
            return "-1/2"
        if n in [2, 4]:
            return "k(3)/2"
        if n in [8, 10]:
            return "-k(3)/2"

def get_table_cos(n, d):

    n, d = reduce2r(n, d)
    n, d = invert_a(n, d)

    if d == 1:
        return "1" if n == 0 else "-1"

    if d == 2:
        return "0" if n % 2 == 1 else ("1" if n % 4 == 0 else "-1")

    if d == 3:
        if n in [0]:
            return "1"
        if n in [1, 5]:
            return "1/2"
        if n in [2, 4]:
            return "-1/2"
        if n in [3]:
            return "-1"

    if d == 4:
        if n in [2, 6]:
            return "0"
        if n in [0]:
            return "1"
        if n in [4]:
            return "-1"
        if n in [1, 7]:
            return "k(2)/2"
        if n in [3, 5]:
            return "-k(2)/2"

    if d == 6:
        if n in [3, 9]:
            return "0"
        if n in [0]:
            return "1"
        if n in [6]:
            return "-1"
        if n in [1, 11]:
            return "k(3)/2"
        if n in [2, 10]:
            return "1/2"
        if n in [4, 8]:
            return "-1/2"
        if n in [5, 7]:
            return "-k(3)/2"

def cs_table(c, n, d):
    if c == 0:
        return get_table_cos(n, d)
    else:
        return get_table_sin(n, d)