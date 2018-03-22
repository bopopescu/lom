def log_text(base, x):
    return "log" + str(base) + "->" + str(x)

def pow_text(base, x, k=False, numerator=False):
    pre = ("1" if not numerator else "") + "/"
    if not k:
        a = str(base) + (("^" + str(x)) if (x != 1 and x != -1) else "")
    else:
        if isinstance(x, int):
            if x < 0:
                p = -x
            else:
                p = x
        else:
            p = x
        a = k_t(base, p)

    if isinstance(x, int):
        res = (pre if x < 0 else "") + a
    else:
        res = a

    return res

def k_t(x, p=2):
    if p != 1:
        res = "k" + ("^" + str(p) if p != 2 else "") + _(str(x))
    else:
        res = str(x)
    return res

def f_t(n, d):
    if d == 0:
        return ""
    if n == 0:
        return "0"

    if isinstance(n, int):
        nt = n if n > 0 else -n
    else:
        nt = n
    if isinstance(d, int):
        dt = d if d > 0 else -d
    else:
        dt = d


    if isinstance(n, int) and not isinstance(d, int):
        s = "-" if n < 0 else ""
    if not isinstance(n, int) and isinstance(d, int):
        s = "-" if d < 0 else ""
    if isinstance(n, int) and isinstance(d, int):
        s = "" if (n < 0 and d < 0) or (n > 0 and d > 0) else "-"
    if not isinstance(n, int) and not isinstance(d, int):
        s = ""
    return s + str(nt) + ("/" + str(dt) if dt != 1 else "")

def pr_t(a, b):
    if isinstance(a, int):
        astr = "" if a == 1 else str(a)
    else:
        astr = str(a)

    if isinstance(b, int):
        bstr = "" if b == 1 else str(b)
    else:
        bstr = str(b)

    return astr + ("*" if astr != "" else "") + bstr

def p_t(a, b):
    return str(a) + "+" + str(b)

def m_t(a, b):
    return str(a) + "-" + str(b)

def _(x):
    return "(" + str(x) + ")"

def p0m1(x, spaces=True):
    s = " " if spaces else ""
    return s + ("+" if x == 0 else "-") + s

def fc(a, is_first = True):
    if a == 1:
        if is_first:
            return ""
        else:
            return "+"
    if a == -1:
        return "-"

    if not is_first and a > 0:
        return "+" + str(a)

    return str(a)

def point(x, y):
    return "(" + str(x) + "; " + str(y) + ")"

def lin(k, b):
    if k == 0:
        return "y=" + str(b)
    if b == 0:
        return "y=" + fc(k) + "x"
    return "y=" + fc(k) + "x" + ("+" + str(b) if b > 0 else str(b))

def mp(symb, p):
    text = ""
    for i in range(0, p):
        text += ("" if i == 0 else "*") + symb
    return text

def get_k(symb, p):
    int_p = p // 2
    k_p = p % 2
    int_p_str = symb + ("^" + str(int_p) if int_p > 1 else "") if int_p > 0 else ""
    k_p_str = k_t(symb) if k_p == 1 else ""
    return int_p_str + k_p_str

def mod(exp):
    return "|" + str(exp) + "|"

def s(a):
    if a == 0:
        return ""
    else:
        return ("+" if a > 0 else "") + str(a)

def ug(n, d):
    if d == 1:
        return "0" if n == 0 else ((str(n) if n not in [1, -1] else "") + "pi")
    else:
        return "0" if n == 0 else ((str(n) if n not in [1, -1] else "") + "pi/" + str(d))

def quad_pol_to_str(coeffs):
    an, ad, bn, bd, cn, cd = coeffs
    return "x^2" + ("+" if bn > 0 else "") +f_t(bn, bd) + "x" + ("+" if cn > 0 else "") + f_t(cn, cd)
