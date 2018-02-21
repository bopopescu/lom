import math
import random


def get_coeff_str(x, is_zeropower = False):
    if x == 0:
        return ""
    s = ""
    if x < 0:
        x = -x
    if (math.fabs(x) != 1) or is_zeropower:
        s = s + str(x)
    return s


def get_coeff_sign_str(x, is_first = False):
    if x < 0:
        return "-"
    else:
        if not is_first:
            return "+"
        else:
            return ""

def get_power_str(p, c):
    if c == 0:
        return ""

    if p != 0:
        if p == 1:
            return "x"
        else:
            return "x^" + str(p)
    else:
        return ""


def get_one_member_str(c, p, is_first = False):
    if c == 0 and p == 0:
        return ""
    return get_coeff_sign_str(c, is_first) + get_coeff_str(c, p == 0) + get_power_str(p, c)


def get_simple_numnbers():
    return (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 3359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503)


def get_ex_simple_numbers(count = 7):
    simple_numbers = list(get_simple_numnbers()[:count])
    extended_simple_numbers = []
    for i, x in enumerate(simple_numbers):
        extended_simple_numbers += [x] * (count - i)
    return extended_simple_numbers


def get_two_numbers_with_common_factors(common=2, n1=2, n2=2):
    s = get_ex_simple_numbers(3 + common * 2)
    c = 1
    for i in range(common):
        c *= random.choice(s)
    a = c
    for i in range(n1):
        a *= random.choice(s)

    b = c
    for i in range(n2):
        b *= random.choice(s)

    return a, b

# Разложение на простые множители
def factoring(x):
    try:
        val = int(x)
    except ValueError:
        return []

    abs_x = int(math.fabs(x))
    if abs_x <= 3:
        return [1, abs_x]

    if x < 0:
        x = -x
    s = get_simple_numnbers()

    s_index = 0
    res = [1]
    value = x
    while value != 1:
        if value % s[s_index] == 0:
            res.append(s[s_index])
            value = int(value / s[s_index])
            continue
        s_index = s_index + 1

    return res

def factors_count(x):
    factors = factoring(x)
    res = {}
    for f in factors:
        res[f] += 1
    return res

def nok(x, y):
    xf = factoring(x)
    yf = factoring(y)
    all_keys = set(xf + yf)
    res = 1
    for f in all_keys:
        res *= pow(f, max(xf.count(f), yf.count(f)))
    return res

def nod(x, y):
    xf = factoring(x)
    yf = factoring(y)
    all_keys = set(xf) & set(yf)
    res = 1
    for f in all_keys:
        res *= pow(f, min(xf.count(f), yf.count(f)))
    return res


# Разложение на 2 множителя случайным образом
def factoring_rnd_2(x):

    s = factoring(x)
    if len(s) == 0:
        return []

    m1_count = random.randint(1, len(s))
    m1 = 1;
    for i in range(m1_count):
        m1_index = random.randint(0, len(s) - 1)
        m1 = m1 * s[m1_index]
        s.remove(s[m1_index])

    m2 = 1
    for i in range(0, len(s)):
        m2 = m2 * s[i]

    return [m1, m2]


def spread_out_on_terms(value, proportions):
    res = {}

    base = sum(proportions.values())
    if base == 0:
        return res
    correction = 0
    for i, p in enumerate(proportions.keys()):
        new_value_precise = (proportions[p] + correction) * value/base
        new_value = round(new_value_precise)
        correction = new_value_precise - new_value
        res[p] = new_value

    if sum(res.values()) != value:
        max_p = max(proportions, key=proportions.get)
        res[max_p] = res[max_p] + (value - sum(res.values()))

    return res


class TextParseException(Exception):
    pass


def get_close_bracket_pos(str, open_bracket_pos):
    unclosed_bracket_count = 0
    for i, symbol in enumerate(str[open_bracket_pos:]):
        if symbol == "(":
            unclosed_bracket_count += 1
        if symbol == ")":
            unclosed_bracket_count -= 1
        if symbol not in ["(", ")"]:
            continue
        if unclosed_bracket_count == 0:
            return open_bracket_pos + i
    raise TextParseException("Нет закрывающей скобки")


def get_random_fraction(mixed_possible=False, ):
    if mixed_possible and random.randint(0, 3) == 0:
        c = random.randint(0, 9)
    else:
        c = 0
    n = random.randint(1, 9)
    d = random.randint(n + 1, 15)
    return (c, n, d)

def get_fraction_str(f):
    c = f[0]
    n = f[1]
    d = f[2]
    return ("" if c == 0 else str(c) + " ")  + str(n) + "/" + str(d)

def rnd_except(s, e, exceptions):
    if (range(s, e) in exceptions):
        return None

    r = random.randint(s, e)
    while r in exceptions:
        r = random.randint(s, e)
    return r

def drob_to_dec(numerator, denominator):
    #print("---->", numerator, "/", denominator)
    result = [str(numerator//denominator) + "."]
    subresults = [numerator % denominator]          ### changed ###
    numerator %= denominator
    while numerator != 0:
        #print(numerator)
        numerator *= 10
        result_digit, numerator = divmod(numerator, denominator)
        result.append(str(result_digit))             ### moved before if-statement

        if numerator not in subresults:
            subresults.append(numerator)
            #print("appended", result_digit)

        else:
            result.insert(subresults.index(numerator) + 1, "(")   ### added '+ 1'
            #print("index", subresults.index(numerator), subresults, "result", result)
            result.append(")")
            #print("repeating", numerator)
            break
    #print(result)
    return "".join(result)
