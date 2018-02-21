import random as rnd
import gen.genutils.common as lgu
import gen.genutils.math_polynomial as pol
import gen.genutils.math_numeric_expressions as ne
import gen.genutils.math_rnd as mrnd
import gen.genutils.math_text as mtxt
import gen.genutils.math_factors as mf
import statistics as st
import math

def postroj_v_odnoj_sisteme_koordinat_grafiki_funktsij445():
    # Построй в одной системе координат графики функций:  y = x^-2, y = x^-3 и y = x^-4
    k_min = 2 * rnd.randint(1, 4)

    return "y=x^-" + str(k_min) + ", y=x^-" + str(k_min + 1) + " и y=x^-" + str(k_min + 2), ''

def kakovyi_oblast_opredelenij_i_oblast_znachenij_funktsii444():
    # каковы область определений и область значений функции y = x^-3 (n=[0, 10])
    k = rnd.randint(2, 9)
    return "какова область определения и область значений функции y=x^-" + str(k), \
           "область определения: вся числовая ось, область значений: " + (
           "любое число" if k % 2 != 0 else "[0, +бесконечность]")

def postroj_v_odnoj_sisteme_koordinat_grafiki_funktsii():
    # построй в одной системе координат графики функции y = x^-2 и y = x^-4
    if rnd.randint(0, 1) == 0:
        k1 = 2 * rnd.randint(1, 4)
        k2 = 2 * mrnd.rnd_w(1, 4, [int(k1/2)])
    else:
        k1 = 2 * rnd.randint(1, 4) + 1
        k2 = 2 * mrnd.rnd_w(1, 4, [int((k1-1)/2)]) + 1

    return "y=x^-" + str(k1) + " и y=x^-" + str(k2), ''

def kakaya_iz_funktsii_lezhit():
    # какая из функции быстрее: убывает|возрастает на отрезке (-бесконечность, -1) | (-1, 0) | (0, 1) | (1, +бесконечность) y = x^-2 или x^-4
    uc = rnd.randint(0, 3)
    uv = rnd.randint(0, 1)
    k1 = rnd.randint(2, 9)
    k2 = mrnd.rnd_w(2, 9, [k1])

    if uc == 0:
        ucs = "(-бесконечность, -1)"
    if uc == 1:
        ucs = "(-1, 0)"
    if uc == 2:
        ucs = "(0, 1)"
    if uc == 3:
        ucs = "(1, +бесконечность)"

    uvs = ("выше" if uv == 0 else "ниже")

    f1 = "y=x^-" + str(k1)
    f2 = "y=x^-" + str(k2)

    if uc == 0:
        if uv == 0:
            answer = f1 if (k1 % 2 == 0 and k2 % 2 != 0) or ((k1 % 2 == 0 and k2 % 2 == 0) and k1 < k2) else f2
        if uv == 1:
            answer = f1 if (k1 % 2 != 0 and k2 % 2 == 0) or ((k1 % 2 != 0 and k2 % 2 != 0) and k1 < k2) else f2
    if uc == 1:
        if uv == 0:
            answer = f1 if (k1 % 2 == 0 and k2 % 2 != 0) or ((k1 % 2 == 0 and k2 % 2 == 0) and k1 > k2) else f2
        if uv == 1:
            answer = f1 if (k1 % 2 != 0 and k2 % 2 == 0) or ((k1 % 2 != 0 and k2 % 2 != 0) and k1 > k2) else f2
    if uc == 2:
        if uv == 0:
            answer = f1 if k1 > k2 else f2
        if uv == 1:
            answer = f1 if k1 < k2 else f2
    if uc == 3:
        if uv == 0:
            answer = f1 if k1 < k2 else f2
        if uv == 1:
            answer = f1 if k1 > k2 else f2

    return uvs + " на отрезке " + ucs + ": " + f1 + " или " + f2, answer

def vozrastaet_ili_ubyivaet_funktsiya441():
# y = x^-3 на участке (-бесконечность, -1) | (-1, 0) | (0, 1) | (1, +бесконечность)
    uc = rnd.randint(0, 3)
    k = rnd.randint(2, 9)

    if uc == 0:
        ucs = "(-бесконечность, -1)"
    if uc == 1:
        ucs = "(-1, 0)"
    if uc == 2:
        ucs = "(0, 1)"
    if uc == 3:
        ucs = "(1, +бесконечность)"

    if k % 2 == 0:
        answer = "возрастает " if uc not in [2, 3] else "убывает"
    else:
        answer = "убывает"

    return "y=x^-" + str(k) + " на участке " + ucs, answer


def postroj_v_odnoj_sisteme_koordinat_grafiki_funktsij440():
# Построй в одной системе координат графики функций:  y = x^2, y = x^3 и y = x^4
    k_min = 2 * rnd.randint(1, 7)

    return "y=x^" + str(k_min) + ", y=x^" + str(k_min + 1) + " и y=x^" + str(k_min + 2), ''

def kakovyi_oblast_opredelenij_i_oblast_znachenij_funktsii():
# каковы область определений и область значений функции y = x^3 (n=[0, 10])
    k = rnd.randint(2, 9)
    return "какова область определения и область значений функции y=x^" + str(k), \
           "область определения: вся числовая ось, область значений: " + ("любое число" if k % 2 != 0 else "[0, +бесконечность]")

def postroj_v_odnoj_sisteme_koordinat_grafiki_funktsij():
# построй в одной системе координат графики функции y = x^2 и y = x^4
    k1 = rnd.randint(1, 4)
    k2 = mrnd.rnd_w(1, 4, [k1])
    return "построй в одной системе координат графики функций: y=x^" + str(k1 * 2) + " и y=x^" + str(k2 * 2), ''

def kakaya_iz_funktsii_lezhit446():
# какая из функции быстрее: убывает|возрастает на отрезке (-бесконечность, -1) | (-1, 0) | (0, 1) | (1, +бесконечность) y = x^2 или x^4
    uc = rnd.randint(0, 3)
    uv = rnd.randint(0, 1)
    k1 = rnd.randint(2, 9)
    k2 = mrnd.rnd_w(2, 9, [k1])

    if uc == 0:
        ucs = "(-бесконечность, -1)"
    if uc == 1:
        ucs = "(-1, 0)"
    if uc == 2:
        ucs = "(0, 1)"
    if uc == 3:
        ucs = "(1, +бесконечность)"

    uvs = ("выше" if uv == 0 else "ниже")

    f1 = "y=x^" + str(k1)
    f2 = "y=x^" + str(k2)

    if uc == 0:
        if uv == 0:
            answer = f1 if (k1 % 2 == 0 and k2 % 2 != 0) or ((k1 % 2 == 0 and k2 % 2 == 0) and k1 > k2) else f2
        if uv == 1:
            answer = f1 if (k1 % 2 != 0 and k2 % 2 == 0) or ((k1 % 2 != 0 and k2 % 2 != 0) and k1 > k2) else f2
    if uc == 1:
        if uv == 0:
            answer = f1 if (k1 % 2 != 0 and k2 % 2 == 0) or ((k1 % 2 == 0 and k2 % 2 == 0) and k1 < k2) else f2
        if uv == 1:
            answer = f1 if (k1 % 2 != 0 and k2 % 2 == 0) or ((k1 % 2 != 0 and k2 % 2 != 0) and k1 < k2) else f2
    if uc == 2:
        if uv == 0:
            answer = f1 if k1 < k2 else f2
        if uv == 1:
            answer = f1 if k1 > k2 else f2
    if uc == 3:
        if uv == 0:
            answer = f1 if k1 > k2 else f2
        if uv == 1:
            answer = f1 if k1 < k2 else f2

    return uvs + " на отрезке " + ucs + ": y=x^" + str(k1) + " или y=x^" + str(k2), answer

def vozrastaet_ili_ubyivaet_funktsiya():
# y = x^3 на участке (-бесконечность, -1) | (-1, 0) | (0, 1) | (1, +бесконечность)
    uc = rnd.randint(0, 3)
    k = rnd.randint(2, 9)

    if uc == 0:
        ucs = "(-бесконечность, -1)"
    if uc == 1:
        ucs = "(-1, 0)"
    if uc == 2:
        ucs = "(0, 1)"
    if uc == 3:
        ucs = "(1, +бесконечность)"

    if k % 2 == 0:
        answer = "возрастает " if uc in [2, 3] else "убывает"
    else:
        answer = "возрастает " if uc in [0, 1, 2, 3] else "убывает"

    return "y=x^" + str(k) + " на участке " + ucs, answer

def ne_vyipolnyaya_postroenij_najdite_tochku_peresecheniya_grafikov_linejnoj_funktsii():
    k1 = rnd.randint(-10, 10)
    b1 = rnd.randint(-10, 10)
    k2 = rnd.randint(-10, 10)
    b2 = rnd.randint(-10, 10)

    xn, xd = mf.s_fraction((b2 - b1, k1 - k2))
    yn, yd = mf.s_fraction((k1*xn+b1*xd, xd))

    return mtxt.lin(k1, b1) + " и " + mtxt.lin(k2, b2), \
           mtxt.point(mtxt.f_t(xn, xd), mtxt.f_t(yn, yd)) if k1 != k2 else "графики не пересекаются"

def najdi_koordinatu_x_peresecheniya_grafikov_funktsij():
    k1 = rnd.randint(-10, 10)
    b1 = rnd.randint(-10, 10)
    k2 = rnd.randint(-10, 10)
    b2 = rnd.randint(-10, 10)

    n, d = mf.s_fraction((b2 - b1, k1 - k2))

    return "найди координату x, точки пересечения графиков функций " + mtxt.lin(k1, b1) + " и " + mtxt.lin(k2, b2), \
           (mtxt.f_t(n, d) if k1 != k2 else "графики не пересекаются")

def najdi_koordinatu_y_tochki():
    x0 = rnd.randint(-10, 10)
    y0 = rnd.randint(-10, 10)
    k = mrnd.rnd_w(-10, 10, [0])
    b = mrnd.rnd_w(-10, 10, [0])

    return mtxt.point(x0, "y") + ", если она принадлежит графику функции " + mtxt.lin(k, b), str(k * x0 + b)

def yavlyaetsya_li_tochka():
    x0 = rnd.randint(-10, 10)
    y0 = rnd.randint(-10, 10)

    p = rnd.randint(0, 1)
    if p == 0:
        k1 = mrnd.rnd_w(-3, 3, [0])
        b1 = y0 - k1 * x0
        k2 = mrnd.rnd_w(-3, 3, [0])
        b2 = y0 - k2 * x0
    else:
        k1 = mrnd.rnd_w(-3, 3, [0])
        b1 = mrnd.rnd_w(-5, 5, [0])
        while y0 == k1 * x0 + b1:
            k1 = mrnd.rnd_w(-3, 3, [0])
            b1 = mrnd.rnd_w(-5, 5, [0])
        k2 = mrnd.rnd_w(-3, 3, [0])
        b2 = mrnd.rnd_w(-5, 5, [0])
        while y0 == k2 * x0 + b2:
            k2 = mrnd.rnd_w(-3, 3, [0])
            b2 = mrnd.rnd_w(-5, 5, [0])

    return "является ли точка (" + str(x0) + ", " + str(y0) + ") точкой пересечения графиков функций y=" + mtxt.fc(k1) + \
           "x" + ("+" + str(b1) if b1 > 0 else str(b1)) + " и y=" + mtxt.fc(k2) + "x" + ("+" + str(b2) if b2 > 0 else str(b2)), \
           "да" if p == 0 else "нет"

def verno_li_utverzhdenie431():
    pq = rnd.randint(0, 1)
    pqs = "принадлежит" if pq == 0 else "не принадлежит"

    gn = rnd.randint(0, 1)
    gns = "обоим графикам" if gn == 0 else "одному из графиков"

    u = rnd.randint(0, 1)
    if u == 0:
        us = " всегда"
    if u == 1:
        us = ""

    return "точка пересечения двух графиков функций" + us + " " + pqs + " " + gns, ("да" if pq == 0 else "нет")

def verno_li_utverzhdenie430():
    x0 = rnd.randint(-10, 10)
    y0 = rnd.randint(-10, 10)

    p = rnd.randint(0, 1)
    if p == 0:
        k1 = mrnd.rnd_w(-3, 3, [0])
        b1 = y0 - k1 * x0
        k2 = mrnd.rnd_w(-3, 3, [0])
        b2 = y0 - k2 * x0
    else:
        k1 = mrnd.rnd_w(-3, 3, [0])
        b1 = mrnd.rnd_w(-5, 5, [0])
        while y0 == k1 * x0 + b1:
            k1 = mrnd.rnd_w(-3, 3, [0])
            b1 = mrnd.rnd_w(-5, 5, [0])
        k2 = mrnd.rnd_w(-3, 3, [0])
        b2 = mrnd.rnd_w(-5, 5, [0])
        while y0 == k2 * x0 + b2:
            k2 = mrnd.rnd_w(-3, 3, [0])
            b2 = mrnd.rnd_w(-5, 5, [0])

    pq = rnd.randint(0, 1)
    gn = rnd.randint(0, 2)

    pqs = "принадлежит" if pq == 0 else "не принадлежит"
    if gn == 0:
        gns = "обоим графикам"
    if gn == 1:
        gns = "первому графику"
    if gn == 2:
        gns = "второму графику"


    return "даны графики y=" + mtxt.fc(k1) + "x" + ("+" + str(b1) if b1 > 0 else str(b1)) + " и y=" + mtxt.fc(k2) + "x" + ("+" + str(b2) if b2 > 0 else str(b2)) + \
           ", точка (" + str(x0) + ", " + str(y0) + ") " + pqs + " " + gns, \
           ("да" if p == pq else "нет")


def reshi_uravnenie429():
    # 27*4^x - 8*9^x = 0
    a = rnd.randint(2, 9)
    b = mrnd.rnd_w(2, 9, [a])
    k = rnd.randint(2, 3)

    n, d = mf.s_fraction((a, b))

    return str(pow(b, k)) + "*" + mtxt.pow_text(a, "x") + " - " + str(pow(a, k)) + "*" + mtxt.pow_text(b, "x") + " = 0", \
           str(k)

    return '', ''

def predstavt():
    # 4/9 в виде степени с основанием 2/3
    d, k = mrnd.common_base_power()
    n = mrnd.choice_w([1, 2, 3], [d])
    return mtxt.f_t(pow(n, k), pow(d, k)) + " в виде степени с основанием " + mtxt.f_t(n, d) , mtxt.pow_text(mtxt._(mtxt.f_t(n, d)), k)

def preobrazuj_vyirazhenie_vyineseniem_za_skobki427():
    # 3^x для выражения 27*2^x - 8*3^x
    a = rnd.randint(2, 9)
    b = mrnd.rnd_w(2, 9, [a])
    k = rnd.randint(2, 3)

    n, d = mf.s_fraction((a, b))

    return mtxt.pow_text(b, "x") + " для выражения " + str(pow(b, k)) + "*" + mtxt.pow_text(a, "x") + " - " + str(pow(a, k)) + "*" + mtxt.pow_text(b, "x"), \
           mtxt.pow_text(b, "x") + " * " + mtxt._(str(pow(b, k)) +  "*" + mtxt.pow_text(mtxt._(mtxt.f_t(n, d)), "x") + " - " + str(pow(a, k)))

def preobrazuj_vyirazhenie_vyineseniem_za_skobki():
	# 3^x для выражения 2^x - 3^x
    a = rnd.randint(2, 9)
    b = mrnd.rnd_w(2, 9, [a])

    n, d = mf.s_fraction((a, b))

    return mtxt.pow_text(b, "x") + " для выражения " + mtxt.pow_text(a, "x") + " - " + mtxt.pow_text(b, "x"), \
           mtxt.pow_text(b, "x") + " * " + mtxt._(mtxt.pow_text(mtxt._(mtxt.f_t(n, d)), "x") + " - 1")


def verno_li_utverzhdenie():
    est_net = rnd.randint(0, 1)
    r_nr = rnd.randint(0, 1)
    n = rnd.randint(2, 9)

    est_net_str = "есть такое" if est_net == 0 else "нет такого"
    r_nr_str = "равняется" if r_nr == 0 else "отлично от"

    # верно ли утверждение: (есть такое) | (нет такого) x при котором 9^x (равняется) | (отлично от) 0.
    return est_net_str + " x при котором " + mtxt.pow_text(n, "x") + " " + r_nr_str + " 0", "да" if (est_net != r_nr) else "нет"

def dokazhite_tozhdestvo():
    k1 = rnd.choice([1, 2, 3, 5, 6, 7])
    k2 = mrnd.choice_w([1, 2, 3, 5, 6, 7], [k1])
    s = rnd.randint(0, 1)

    t1s = mtxt.f_t(mtxt.k_t(mtxt.fc(k1) + "a"), mtxt._(mtxt.k_t(mtxt.fc(k1) + "a") + "+" + mtxt.k_t(mtxt.fc(k2) + "b")))
    t2s = mtxt.f_t(mtxt.k_t(mtxt.fc(k2) + "b"), mtxt._(mtxt.k_t(mtxt.fc(k1) + "a") + "-" + mtxt.k_t(mtxt.fc(k2) + "b")))
    t3s = mtxt.f_t("2" + mtxt.k_t(mtxt.fc(k1) + "ab"), mtxt._(mtxt.fc(k2) + "b" + "-" + mtxt.fc(k1) + "a"))

    right = mtxt.f_t( mtxt._(mtxt.k_t(mtxt.fc(k1) + "a") + mtxt.p0m1(1-s) + mtxt.k_t(mtxt.fc(k2) + "b")),
                      mtxt._(mtxt.k_t(mtxt.fc(k1) + "a") + mtxt.p0m1(s) + mtxt.k_t(mtxt.fc(k2) + "b")))

    return t1s + " + " + t2s + mtxt.p0m1(s) + t3s + " = " + right, ''

def privesti_k_obschemu_znamenatelyu():
    k1 = rnd.choice([1, 2, 3, 5, 6, 7])
    k2 = mrnd.choice_w([1, 2, 3, 5, 6, 7], [k1])
    s = rnd.randint(0, 1)

    if s == 0:
        answer = mtxt.f_t("2" + mtxt.pow_text((str(k1) if k1 != 1 else "") + "a", 2, True), "(" + (str(k1) if k1 != 1 else "") + "a-" + str(k2) + "b" + ")")
    else:
        answer = mtxt.f_t("2" + mtxt.pow_text((str(k2) if k2 != 1 else "") + "b", 2, True), "(" + (str(k2) if k2 != 1 else "") + "b-" + str(k1) + "a" + ")")

    return mtxt.f_t(1, "(" + mtxt.pow_text((str(k1) if k1 != 1 else "") + "a", 2, True) + "+" + mtxt.pow_text((str(k2) if k2 != 1 else "") + "b", 2, True) + ")") + mtxt.p0m1(s) + \
           mtxt.f_t(1, "(" + mtxt.pow_text((str(k1) if k1 != 1 else "") + "a", 2, True) + "-" + mtxt.pow_text((str(k2) if k2 != 1 else "") + "b", 2, True) + ")"), answer

def razlozhit_na_mnozhiteli422():
    k1 = rnd.choice([1, 2, 3, 5, 6, 7])
    k2 = mrnd.choice_w([1, 2, 3, 5, 6, 7], [k1])
    return (str(k1) if k1 != 1 else "") + "a - " + (str(k2) if k2 != 1 else "") + "b", \
           "(" + (mtxt.pow_text(str(k1) + "a", 2, True) if k1 != 1 else mtxt.pow_text("a", 2, True)) + " - " + (mtxt.pow_text(str(k2) + "b", 2, True) if k2 != 1 else mtxt.pow_text("b", 2, True)) + ") * " + \
           "(" + (mtxt.pow_text(str(k1) + "a", 2, True) if k1 != 1 else mtxt.pow_text("a", 2, True)) + " + " + (mtxt.pow_text(str(k2) + "b", 2, True) if k2 != 1 else mtxt.pow_text("b", 2, True)) + ")"

def razlozhit_na_mnozhiteli():
    k1 = rnd.choice([1, 2, 3, 5, 6, 7])
    k2 = mrnd.choice_w([1, 2, 3, 5, 6, 7], [k1])
    return (str(pow(k1, 2)) if k1 != 1 else "") + "a^2 - " +(str(pow(k2, 2)) if k2 != 1 else "") + "b^2", \
           "(" + (str(k1) if k1 != 1 else "") + "a - " +  (str(k2) if k2 != 1 else "") + "b) * " + \
           "(" + (str(k1) if k1 != 1 else "") + "a + " +  (str(k2) if k2 != 1 else "") + "b)"

def uprostit420():
    k1 = rnd.choice([1, 2, 3, 5, 6, 7])
    k2 = mrnd.choice_w([1, 2, 3, 5, 6, 7], [k1])
    s = rnd.randint(0, 1)
    return (str(k1) if k1 != 1 else "") + "a" + mtxt.p0m1(s) + "2" + mtxt.pow_text(str(k1 * k2) + "ab", 2, True) +  " + " + \
           (str(k2) if k2 != 1 else "") + "b", "(" + (mtxt.pow_text(str(k1) + "a", 2, True) if k1 != 1 else mtxt.pow_text("a", 2, True)) + mtxt.p0m1(s) + (
           mtxt.pow_text(str(k2) + "b", 2, True) if k2 != 1 else mtxt.pow_text("b", 2, True)) + ")^2"

def uprostit():
    k1 = rnd.choice([1, 2, 3, 4, 5, 6])
    k2 = mrnd.choice_w([1, 2, 3, 3, 5, 6], [k1])
    s = rnd.randint(0, 1)
    return (str(pow(k1, 2)) if k1 != 1 else "") + "a^2" + mtxt.p0m1(s) + (str(2 * k1 * k2) if k1 * k2 != 1 else "2") + "ab + " + \
           (str(pow(k2, 2) if k2 != 1 else "") + "b^2"), "(" + (str(k1) if k1 != 1 else "") + "a" + mtxt.p0m1(s) + (str(k2) if k2 != 1 else "") + "b)^2"


def reshi_uravnenie419():
    a = rnd.randint(2, 5)
    c = rnd.randint(5, 20)
    k = rnd.randint(1, 3)
    s = rnd.randint(0, 1)

    n, d = mf.s_fraction((c, pow(a, k) - 1))

    answer = str(k + 1) + "*" + mtxt.log_text(a, mtxt.f_t(n, d))

    return mtxt.pow_text(a, "(x-1)") + (" + " if s == 0 else " - ") + mtxt.pow_text(a, "(x-" + str(1 + k) + ")") + " = " + str(c),\
           answer

def reshi_uravnenie415():
    a = rnd.randint(2, 5)
    k_range = rnd.randint(1, 3)
    n = rnd.randint(1, 2)
    s = rnd.randint(0, 1)

    if s == 1:
        r = pow(a, n) * (pow(a, k_range) - 1)
    else:
        r = pow(a, n) * (pow(a, k_range) + 1)

    return mtxt.pow_text(a, "(x-1)") + (" + " if s == 0 else " - ") + mtxt.pow_text(a, "(x-" + str(1+k_range)) + ") = " + str(r), \
           str(n + k_range + 1)

def vyinesi_obschij_mnozhitel_za_skobki415():
    a = rnd.randint(2, 5)
    k_range = rnd.randint(1, 3)
    return mtxt.pow_text(a, "(x-1)") + " - " + mtxt.pow_text(a, "(x-" + str(1 + k_range) + ")"), \
           str(pow(a, k_range) - 1) + "*" + mtxt.pow_text(a, "(x-" + str(1 + k_range) +")")

def ne_proizvodya_vyichislenij_vyinesi_obschij_mnozhitel_za_skobki415():
    a = rnd.randint(2, 3)
    k_range = rnd.randint(1, 3)
    k_min = rnd.randint(k_range + 1, k_range + 3)

    return mtxt.pow_text(a, k_min + k_range) + " - " + mtxt.pow_text(a, k_min), str( pow(a, k_min) * (pow(a, k_range) - 1))

def reshi_uravnenie412():
    a = rnd.randint(2, 10)
    if a in [2, 4, 8]:
        b = mrnd.rnd_w(2, 10, [2, 4, 8])
    if a in [3, 9]:
        b = mrnd.rnd_w(2, 10, [3, 9])
    if a in [5, 6, 7, 10]:
        b = mrnd.rnd_w(2, 10, [a])


    return str(a) + "^x = 1/" + str(b), "-" + mtxt.log_text(a, b)

def predstav410():
    a = rnd.randint(2, 10)
    if a in [2, 4, 8]:
        b = mrnd.rnd_w(2, 10, [2, 4, 8])
    if a in [3, 9]:
        b = mrnd.rnd_w(2, 10, [3, 9])
    if a in [5, 6, 7, 10]:
        b = mrnd.rnd_w(2, 10, [a])

    return "1/" + str(b) + " в виде степени с основанием " + str(a), mtxt.pow_text(a, "-" + mtxt.log_text(a, b))


def predstav412():
    a = rnd.randint(2, 10)

    return "1/" + str(a) + " в виде степени с основанием " + str(a), str(a) + "^-1"

def predstav():
    a = rnd.randint(2, 10)
    if a in [2, 4, 8]:
        b = mrnd.rnd_w(2, 10, [2, 4, 8])
    if a in [3, 9]:
        b = mrnd.rnd_w(2, 10, [3, 9])
    if a in [5, 6, 7, 10]:
        b = mrnd.rnd_w(2, 10, [a])

    return str(b) + " в виде степени с основанием " + str(a), mtxt.pow_text(a, mtxt.log_text(a, b))


def v_kakuyu_stepen_nuzhno_vozvesti412():
    a = rnd.randint(2, 10)
    if a in [2, 4, 8]:
        b = mrnd.rnd_w(2, 10, [2, 4, 8])
    if a in [3, 9]:
        b = mrnd.rnd_w(2, 10, [3, 9])
    if a in [5, 6, 7, 10]:
        b = mrnd.rnd_w(2, 10, [a])

    return str(a) + " чтобы получить " + str(b), mtxt.log_text(a, b)

def vyichisli_2log2minus_3():
    a = rnd.randint(2, 10)
    if a in [2, 4, 8]:
        b = mrnd.rnd_w(2, 10, [2, 4, 8])
    if a in [3, 9]:
        b = mrnd.rnd_w(2, 10, [3, 9])
    if a in [5, 6, 7, 10]:
        b = mrnd.rnd_w(2, 10, [a])
    return mtxt.pow_text(a, mtxt.log_text(a, b)), str(b)

def reshi_uravneniya():
    n, k1 = mrnd.common_base_power()
    k2 = mrnd.rnd_w(1, 4, [k1])
    m1 = rnd.randint(2, 9)
    m2 = mrnd.rnd_w(2, 9, [m1])

    x, y = mf.s_fraction((-k2*m2, m1))

    answer = mtxt.f_t(x, y)

    return str(pow(n, k1)) + "^x" + " = " + mtxt.pow_text(mtxt._("1/" + str(pow(n, k2))), m2), answer


def privesti_stepeni_k_odinakovomu_osnovaniyu():
    n, k1 = mrnd.common_base_power()
    k2 = mrnd.rnd_w(1, 4, [k1])
    m1 = rnd.randint(2, 9)
    m2 = mrnd.rnd_w(2, 9, [m1])

    return mtxt.pow_text(pow(n, k1), m1) + " и " + mtxt.pow_text(mtxt._("1/" + str(pow(n, k2))), m2), \
           mtxt.pow_text(n, k1 * m1) + " и " + str(n) + "^" + str(-k2*m2)

def privesti_stepen_drobi_k_nuzhnomu_osnovaniyu():
    n, k = mrnd.common_base_power()
    k1 = rnd.randint(2, 9)
    return mtxt.pow_text(mtxt._("1/" + str(pow(n, k))), k1) + " к степени с ооснованием " + str(n), str(n) + "^" + str(-k*k1)

def privesti_stepen_k_nuzhnomu_osnovaniyu():
    n, k = mrnd.common_base_power()
    k1 = rnd.randint(2, 9)
    return mtxt.pow_text(pow(n, k), k1) + " к степени с ооснованием " + str(n), mtxt.pow_text(n, k * k1)

def vyichislit_vyirazhenie_s_kornyami_i_otritsatelnyimi_stepenyami():
    count = rnd.randint(3, 4)
    terms = [] #дробь, корень, перевернутый корень, пусто
    def generate_term_part():
        t = rnd.choice([1, 2, 3, 1, 2, 3, 4])
        if t == 1:
            n = rnd.randint(2, 5)
            d = mrnd.rnd_w(2, 5, [n])
            k = mrnd.rnd_w(-2, 2, [0])
        if t in [2, 3]:
            n = rnd.choice([2, 3, 5])
            k = rnd.choice([2, 4])
            d = 1
        if t == 4:
            n = 0
            d = 0
            k = 0
        return (t, n, d, k)
    def get_term_part_text(term_part):
        t, n, d, k = term_part
        if t == 1:
            ts = mtxt._(mtxt.f_t(n, d)) + ("^" + str(k) if k != 1 else "")
        if t == 2:
            ts = mtxt.pow_text(mtxt._(mtxt.pow_text(n, 2, True)), k)
        if t == 3:
            ts = mtxt.pow_text(mtxt._("1/" + mtxt.pow_text(n, 2, True)), k)
        if t == 4:
            ts = ""
        return ts
    def get_term_text(term, is_first=False):
        s, t1, t2 = term
        if t1[0] == 4 and t2[0] == 4:
            ss = ""
        else:
            if s == 1:
                ss = " - " if not is_first else "-"
            else:
                ss = (" + " if not is_first else "")
        return ss + get_term_part_text(t1) + ("*" if t1[0] != 4 and t2[0] != 4 else "") + get_term_part_text(t2)
    def get_term_part_value(term_part):
        t, n, d, k = term_part
        if t == 1:
            if k > 0:
                num = pow(n, k)
                dnum = pow(d, k)
            else:
                num = pow(d, -k)
                dnum = pow(n, -k)
        if t == 2:
            num = pow(n, int(k/2))
            dnum = 1
        if t == 3:
            num = 1
            dnum = pow(n, int(k/2))
        if t == 4:
            num = 0
            dnum = 1
        return num, dnum
    for i in range(count - 1):
        terms.append((rnd.randint(0, 1), generate_term_part(), generate_term_part()))

    text = ""
    for t in terms:
        text += get_term_text(t, terms.index(t) == 0)

    n = 0
    d = 1
    for t in terms:
        s, t1, t2 = t
        n1, d1 = get_term_part_value(t1)
        n2, d2 = get_term_part_value(t2)

        if s == 1:
            n1 = -n1
        n, d = mf.s_fraction_sum(mf.s_fraction_prod((n1, d1), (n2, d2)), (n, d))

    answer = mtxt.f_t(n, d)

    return text, answer


def vozvedenie_drobi_s_kvadratnyim_kornem_v_otritsatelnuyu_stepen():
    n, k = mrnd.common_base_power()
    t = rnd.randint(0, 1)
    if t == 0:
        k = 2 * k
        answer = str(pow(n, k))
    else:
        k = 2 * k - 1
        answer = mtxt._(str(pow(n, k - 1)) + "*" + mtxt.pow_text(n, 2, True))

    return mtxt._("1/" + mtxt.pow_text(pow(n, 2), 2, True)) + "^-" + str(k), answer


def vozvedenie_kvadratnogo_kornya_v_otritsatelnuyu_stepen():
    n, k = mrnd.common_base_power()
    t = rnd.randint(0, 1)
    if t == 0:
        k = 2 * k
        answer = "1/" + str(pow(n, k))
    else:
        k = 2 * k - 1
        answer = "1/" + mtxt._(str(pow(n, k-1)) + "*" + mtxt.pow_text(n, 2, True))

    return mtxt.pow_text(pow(n, 2), 2, True) + "^-" + str(k), answer

def vozvedenie_kvadratnogo_kornya_v_nechetnuyu_stepen():
    n, k = mrnd.common_base_power()
    k2 = 2 * k
    k = k2 - 1
    return mtxt.pow_text(pow(n, 2), 2, True) + "^" + str(k), str(pow(n, k2 - 2)) + "*" + mtxt.pow_text(n, 2, True)

def vozvedenie_kvadratnogo_kornya_v_chetnuyu_stepen():
    n, k = mrnd.common_base_power()
    k = 2 * k
    return mtxt.pow_text(pow(n, 2), 2, True) + "^" + str(k), str(pow(n, k))

def vozvedenie_drobi_v_otritsatelnuyu_stepen():
    n, k = mrnd.common_base_power()
    d = mrnd.rnd_w(2, 11, [n])
    return mtxt._(mtxt.f_t(n, d)) + "^-" + str(k), mtxt.f_t(pow(d, k), pow(n, k))

def vozvedenie_chisladrobi_v_otritsatelnuyu_stepen():
    t = rnd.randint(0, 1)
    n, k = mrnd.common_base_power()
    text = (str(n) if t == 0 else "1/" + str(n))
    if t == 1:
        text = mtxt._(text)
    text += "^-" + str(k)
    if t == 0:
        answer = "1/" + str(pow(n, k))
    else:
        answer = str(pow(n, k))
    return text, answer


def dana_funktsiya_v_kakoj_tochki_grafik_peresekaet_os():
    k = mrnd.rnd_w(-10, 10, [0])
    m = rnd.randint(1, 5)
    b = k * m
    os = rnd.randint(0, 1)

    if os == 0:
        y = 0
        x = -m
    else:
        x = 0
        y = b

    return "y = " + str(k) + "x" + (str(b) if b < 0 else "+" + str(b)) + ", в какой точке график пересекает ось " + \
           ("x" if os == 0 else "y") + "?", "(" + str(x) + ", " + str(y) + ")"

def dana_funktsiya():
    k = mrnd.rnd_w(-10, 10, [0])
    m = rnd.randint(1, 5)
    b = k * m
    os = rnd.randint(0, 1)

    if os == 0:
        answer = -m
    else:
        answer = b

    return "y = " + str(k) + "x" + (str(b) if b < 0 else "+" + str(b)) + ", чему равна координата " + \
           ("x" if os == 0 else "y") + ", если " + ("x" if os != 0 else "y") + "=0?" , str(answer)

def vernyi_li_utverzhdeniya():
    os = rnd.randint(0, 1)
    l = rnd.randint(0, 1)
    x = 0 if rnd.randint(0, 1) == 0 else rnd.randint(-10, 10)
    y = 0 if rnd.randint(0, 1) == 0 else rnd.randint(-10, 10)

    if os == 0:
        if l == 0:
            answer = True if y == 0 else False
        else:
            answer = True if y != 0 else False
    else:
        if l == 0:
            answer = True if x == 0 else False
        else:
            answer = True if x != 0 else False

    return "точка с координатами (" + str(x) + ", " + str(y) + ") " + ("лежит" if l == 0 else "не лежит") + " на оси " + \
           ("x" if os == 0 else "y"), "да" if answer else "нет"

def lezhit_li_tochka_na_osi():
    os = rnd.randint(0, 1)
    ok = rnd.randint(0, 1)
    if os == 0:
        x = rnd.randint(-20, 20)
        if ok == 0:
            y = 0
        else:
            y = rnd.randint(-20, 20)
    else:
        y = rnd.randint(-20, 20)
        if ok == 0:
            x = 0
        else:
            x = rnd.randint(-20, 20)
    return "(" + str(x) + ", " + str(y) + ") на оси " + ("x" if os == 0 else "y") + "?", "нет" if ok == 1 else "да"

def najdi_rasstoyanie_mezhdu_gorodami_na_mestnosti_esli_rasstoyanie_mezhdu_etimi_gorodami_na_karte():
    k = rnd.randint(10, 50) * 10000
    r1 = rnd.randint(10, 25)
    r2 = r1 * k
    return str(r1) + " см., а масштаб карты 1:" + str(k), str(r1 * k / 100000)

def najdi_rasstoyanie_mezhdu_gorodami_na_karte_esli_rasstoyanie_mezhdu_etimi_gorodami_na_mestnosti():
    k = rnd.randint(10, 50) * 10000
    r1 = rnd.randint(10, 25)
    r2 = r1 * k
    return str(r2 / 100000) + " км., а масштаб карты 1:" + str(k), str(r1) + " см."

def sostav_proportsiyu_mezhdu_rasstoyaniem_mezhdu_gorodami_i_masshtabom_kartyi_i_prover_ee():
    k = rnd.randint(10, 50) * 10000
    r1 = rnd.randint(10, 25)
    distortion = rnd.randint(0, 1)
    r2 = r1 * k + distortion * mrnd.rnd_w(10, 25, [r1]) * k
    return "расстояние на местности " + str(r2 / 100000) + " км., расстояние на карте " + str(r1) + " см. Мастшаб 1:" + \
           str(k), "на карте ошибка" if distortion == 1 else "все правильно"

def kakoj_masshtab_kartyi_esli_rasstoyanie_mezhdu_gorodami():
    k = rnd.randint(10, 50) * 10000
    r1 = rnd.randint(10, 25)
    r2 = r1 * k
    return str(r2 / 100000) + " км., а расстояние между ними на карте " + str(r1) + " сантиметров", '1:' + str(k)

def skolko_zarabotaet_rabochij_za():
    k = rnd.randint(3, 8) * 100
    x1 = rnd.randint(2, 8)
    x2 = mrnd.rnd_w(2, 8, [x1])
    text = str(x1) + " часов, если за " + str(x2) + " часов он зарабатывает " + str(k * x2) + " рублей? Зарплата рабочего" \
                    " прямо пропорциональна числу отработанных им часов."
    return text, str(k * x1)

def est_pryamaya_proportsionalnost_zapolni_tablitsu():
    step_count = 7

    a0 = rnd.choice([2, 3, 5, 7, 11])
    b0 = mrnd.choice_w([2, 3, 5, 7, 11], [a0])

    transformations = [(1, 0)]
    for i in range(0, step_count):
        transformations.append((rnd.choice([2, 3, 4, 5]), rnd.randint(0, 1)))

    f = []
    for k, t in reversed(transformations):
        if t == 1:
            f.extend(mf.factoring(k))
        if t == 0:
            fa = mf.factoring(k)
            for fai in fa:
                if fai in f:
                    f.remove(fai)
    a = a0
    b = b0
    for fi in f:
        a *= fi
        b *= fi

    values = []
    ar = a
    br = b
    for k, t in transformations:
        ar = (ar * k if t == 0 else int(ar / k))
        br = (br * k if t == 0 else int(br / k))
        values.append((ar, br))

    hidden = []
    base_index = rnd.randint(0, step_count - 1)
    i = 0
    for k, t in transformations:
        if i != base_index:
            hidden.append((i, rnd.randint(0, 1)))
        i += 1

    def get_str(step, value_index):
        if (step, value_index) in hidden:
            return "x"
        else:
            return str(values[step][value_index])

    x = ""
    y = ""
    for i in range(0, step_count + 1):
        x += (", " if i != 0 else "") + get_str(i, 0)
        y += (", " if i != 0 else "") + get_str(i, 1)

    answer = ""
    for hi, hv in hidden:
        answer += "(" + str(values[hi][hv]) + ")"

    return x + " | " + y, answer

def est_pryamaya_proportsionalnost_2_shaga_opredeli_neizvestnoe():
    step_count = 2

    a0 = rnd.choice([2, 3, 5, 7, 11])
    b0 = mrnd.choice_w([2, 3, 5, 7, 11], [a0])

    transformations = [(1, 0)]
    for i in range(0, step_count):
        transformations.append((rnd.randint(2, 5), rnd.randint(0, 1)))

    f = []
    f_added = []
    for k, t in transformations:
        if t == 1:
            f.extend(mf.factoring(k))
        if t == 0:
            f_added.extend(mf.factoring(k))
    for fi in f_added:
        if fi in f:
            f.remove(fi)
    a = a0
    b = b0
    for fi in f:
        a *= fi
        b *= fi

    values = []
    ar = a
    br = b
    for k, t in transformations:
        ar = (ar * k if t == 0 else int(ar / k))
        br = (br * k if t == 0 else int(br / k))
        values.append((ar, br))

    hidden = []
    base_index = rnd.randint(0, step_count)
    i = 0
    for k, t in transformations:
        if i != base_index:
            hidden.append((i, rnd.randint(0, 1)))
        i += 1

    def get_str(step, value_index):
        if (step, value_index) in hidden:
            return "неизвестна"
        else:
            return str(values[step][value_index])

    answer = ""
    for hi, hv in hidden:
        answer += "(" + str(values[hi][hv]) + ")"

    return "Первая величина была сначала " + get_str(0, 0) + ", а потом стала " + get_str(1, 0) + ", а потом стала " + get_str(2, 0)+ ". " \
           + "Вторая величина была сначала " + get_str(0, 1) + ", а потом стала " + get_str(1, 1) + ", а потом стала " + get_str(2, 1) + ". ", \
           answer

def est_pryamaya_proportsionalnost_opredeli_neizvestnoe():
    step_count = 1

    a0 = rnd.choice([2, 3, 5, 7, 11])
    b0 = mrnd.choice_w([2, 3, 5, 7, 11], [a0])

    transformations = [(1, 0)]
    for i in range(0, step_count):
        transformations.append((rnd.randint(2, 5), rnd.randint(0, 1)))

    f = []
    f_added = []
    for k, t in transformations:
        if t == 1:
            f.extend(mf.factoring(k))
        if t == 0:
            f_added.extend(mf.factoring(k))
    for fi in f_added:
        if fi in f:
            f.remove(fi)
    a = a0
    b = b0
    for fi in f:
        a *= fi
        b *= fi

    values = []
    ar = a
    br = b
    for k, t in transformations:
        ar = (ar * k if t == 0 else int(ar/k))
        br = (br * k if t == 0 else int(br/k))
        values.append((ar, br))

    hidden = []
    base_index = rnd.randint(0, step_count)
    i = 0
    for k, t in transformations:
        if i != base_index:
            hidden.append((i, rnd.randint(0, 1)))
        i += 1

    def get_str(step, value_index):
        if (step, value_index) in hidden:
            return "неизвестна"
        else:
            return str(values[step][value_index])

    answer = ""
    for hi, hv in hidden:
        answer += "(" + str(values[hi][hv]) + ")"

    return "Первая величина была сначала " + get_str(0, 0) + ", а потом стала " + get_str(1, 0) + ". "\
        + "Вторая величина была сначала " + get_str(0, 1) + ", а потом стала " + get_str(1, 1) + ". ", \
           answer

def est_li_pryamaya_proportsionalnost_mezhdu_dvumya_velichinam_2_shaga():
    steps_count = 2

    a_transformations = []
    a_transformations.append((1, 0))
    for i in range(1, steps_count + 1):
        k = rnd.randint(2, 5)
        t = rnd.randint(0, 1)
        a_transformations.append((k, t))
    f = []
    f_added = []
    for k, t in a_transformations:
        if t == 1:
            f.extend(mf.factoring(k))
        if t == 0:
            f_added.extend(mf.factoring(k))
    for fi in f_added:
        if fi in f:
            f.remove(fi)
    a0 = rnd.choice([2, 3, 5, 7, 11])
    a = a0
    for fi in f:
        a *= fi

    b_transformations = []
    b_transformations.append((1, 0))
    for i in range(1, steps_count + 1):
        if rnd.choice([0, 0, 0, 1, 0, 1]) == 0:
            k = a_transformations[i][0]
        else:
            k = rnd.randint(2, 5)
        t = rnd.randint(0, 1)
        b_transformations.append((k, t))
    f = []
    f_added = []
    for k, t in b_transformations:
        if t == 1:
            f.extend(mf.factoring(k))
        if t == 0:
            f_added.extend(mf.factoring(k))
    for fi in f_added:
        if fi in f:
            f.remove(fi)
    b0 = mrnd.choice_w([2, 3, 5, 7, 11], [a0])
    b = b0
    for fi in f:
        b *= fi

    text = "если сначала первая величина была "
    ar = a
    i = 0
    for k, t in a_transformations:
        ar = (ar * k if t == 0 else int(ar/k))
        text += str(ar) + (", а потом " if i < len(a_transformations) - 1 else ". ")
        i += 1
    text += "А вторая величина сначала была "
    br = b
    i = 0
    for k, t in b_transformations:
        br = (br * k if t == 0 else int(br/k))
        text += str(br) + (", а потом " if i < len(b_transformations) - 1 else ".")
        i += 1

    answer = "есть" if a_transformations == b_transformations else "нет"

    return text, answer

def est_li_pryamaya_proportsionalnost_mezhdu_dvumya_velichinam_1_shag():
    a1 = rnd.randint(3, 12)
    a2 = mrnd.rnd_w(3, 12, [a1])
    k1 = rnd.randint(2, 5)
    if rnd.choice([0, 0, 0, 0, 1, 0, 1]) == 0:
        k2 = k1
    else:
        k2 = mrnd.rnd_w(2, 5, [k1])
    t1 = rnd.randint(0, 1)
    t2 = rnd.randint(0, 1)

    initial_str1 = str(a1) if t1 == 0 else str(a1 * k1)
    initial_str2 = str(a2) if t2 == 0 else str(a2 * k2)
    result_str1 = str(a1) if t1 == 1 else str(a1 * k1)
    result_str2 = str(a2) if t2 == 1 else str(a2 * k2)

    text = "если первая величина была " + initial_str1 + ", а стала " + result_str1 + ". Вторая величина была " + \
           initial_str2 + ", а стала " + result_str2 + "?"
    answer = "есть" if ((k1 == k2) and (t1 == t2)) else "нет"

    return text, answer

def est_li_pryamaya_proportsionalnost_v_chisle_yablok():
    a1 = rnd.randint(3, 12)
    a2 = mrnd.rnd_w(3, 12, [a1])
    k1 = rnd.randint(2, 5)
    if rnd.choice([0, 0, 0, 1, 0, 1, 0]) == 0:
        k2 = k1
    else:
        k2 = mrnd.rnd_w(2, 5, [k1])
    t1 = rnd.randint(0, 1)
    t2 = rnd.randint(0, 1)

    initial_str1 = str(a1) if t1 == 0 else str(a1*k1)
    initial_str2 = str(a2) if t2 == 0 else str(a2*k2)
    result_str1 = str(a1) if t1 == 1 else str(a1*k1)
    result_str2 = str(a2) if t2 == 1 else str(a2*k2)

    text = "Прямая пропорциональность - это если число яблок меняется в одинаковое число раз в одинаковую сторону. " \
           "У Макара было " + initial_str1 + " яблока, а стало " + result_str1 + ". А у Маши было " + initial_str2 + \
           " яблока, а стало " + result_str2 + ". Есть ли прямая пропорциональность числа яблок у детей?"
    answer = "есть" if ( (k1 == k2) and (t1 == t2) ) else "нет"

    return text, answer


def v_odnu_li_storonu_menyaetsya_chislo_yablok():
    a1 = rnd.randint(3, 12)
    a2 = mrnd.rnd_w(3, 12, [a1])
    k1 = rnd.randint(2, 5)
    if rnd.choice([0, 1, 0, 1]) == 0:
        k2 = k1
    else:
        k2 = mrnd.rnd_w(2, 5, [k1])
    t1 = rnd.randint(0, 1)
    t2 = rnd.randint(0, 1)

    change_str1 = "увеличилось" if t1 == 0 else "уменьшилось"
    change_str2 = "увеличилось" if t2 == 0 else "уменьшилось"
    initial_str1 = str(a1) if t1 == 0 else str(a1 * k1)
    initial_str2 = str(a2) if t2 == 0 else str(a2 * k2)
    result_str1 = str(a1) if t1 == 1 else str(a1 * k1)
    result_str2 = str(a2) if t2 == 1 else str(a2 * k2)

    text = "В одну ли сторону изменилось число яблок у Макара и Маши, если у Макара было " \
            + initial_str1 + " яблока, а стало " + result_str1+ ", а у Маши было " + initial_str2 \
           + ", а стало " + result_str2 + "?"
    answer = ""
    if t1 == t2:
        answer += "изменились в одинаковую сторону: " + change_str1
    else:
        answer += "изменились в разные стороны: у Макара " + change_str1 + ", а у Маши " + change_str2

    return text, answer


def v_ravnoe_li_kolichestvo_raz_izmenilos_chislo_yablok():
    a1 = rnd.randint(3, 12)
    a2 = mrnd.rnd_w(3, 12, [a1])
    k1 = rnd.randint(2, 5)
    if rnd.choice([0, 1, 0, 1]) == 0:
        k2 = k1
    else:
        k2 = mrnd.rnd_w(2, 5, [k1])
    t = rnd.randint(0, 1)

    change_str = "увеличилось" if t == 0 else "уменьшилось"
    initial_str1 = str(a1) if t == 0 else str(a1*k1)
    initial_str2 = str(a2) if t == 0 else str(a2*k2)
    result_str1 = str(a1) if t == 1 else str(a1*k1)
    result_str2 = str(a2) if t == 1 else str(a2*k2)

    text = "У Макара было " + initial_str1 + " яблока, а стало " + result_str1 + \
           " . А у Маши было " + initial_str2 + " яблока, а стало " + result_str2 + " . " \
            "У кого из детей число яблок " + change_str + " в большее число раз?"

    if k1 == k2:
        answer = change_str + " одинаково"
    else:
        if k1 > k2:
            answer = "У Макара " + change_str + " в бОльшое число раз"
        else:
            answer = "У Маши " + change_str + " в бОльшое число раз"

    return text, answer


def vo_skolko_raz_izmenilos_chislo_yablok():
    a = rnd.randint(3, 12)
    k = rnd.randint(2, 5)
    t = rnd.randint(0, 1)
    initial_str = str(a) if t == 0 else str(a*k)
    result_str = str(a) if t == 1 else str(a*k)
    change_str = "увеличилось" if t == 0 else "уменьшилось"
    text = "У Макара было " + initial_str + " яблока, а потом стало " + result_str + " яблок. Во сколько раз " + change_str + " число яблок у Макара?"
    return text, "в " + str(k) + " раз"


def uprosti_vyirazhenie_s_logarifmami():
    terms_count = rnd.randint(2, 4)
    terms = []
    a = mrnd.choice_w([2, 3, 4, 5])
    for i in range(0, terms_count):
        s = rnd.randint(0, 1) # 0  - это "+", 1 - это "-"
        an = rnd.randint(1, 3)
        bn = rnd.randint(1, 3)
        applied_bn = rnd.randint(0, 1)
        f = rnd.randint(1, 5)
        term = (s, a, an, bn, applied_bn, f)
        terms.append(term)

    text = ""

    for i, t in enumerate(terms):
        term_text = mtxt.log_text(
            mtxt.f_t(1, pow(a, t[2])),
            mtxt.f_t(1, pow(a, t[3]) if t[4] == 0 else mtxt.pow_text(a, t[3]))
        )

        text += ("-" if t[0] == 1 else ("+" if i != 0 else "")) + mtxt.pr_t(t[5], term_text)

    rak = rnd.choice([2, 3, 4])
    rbk = rnd.choice([2, 3, 4])
    rn = mrnd.choice_w([2, 3, 4], [rbk])

    text = mtxt.f_t(mtxt._(text), mtxt.log_text(
        mtxt.pow_text(a, rak, True),
        mtxt.pow_text(pow(a, rn), rbk, True),
    ))

    sfn = 0
    sfd = 1
    for t in terms:
        tsn, tsd = mf.s_fraction(((1 if t[0] == 0 else -1) * t[5] * t[3], t[2]))
        sfn, sfd = mf.s_fraction_sum((sfn, sfd), (tsn, tsd))
    n, d = mf.s_fraction((rbk * sfn, rn * rak * sfd))


    return text, mtxt.f_t(n, d)

def uprosti_raznost_logarifmov():
    a, n = mrnd.common_base_power()
    f = mrnd.choice_w([2, 3, 4, 5, 6, 7], [a])
    return  mtxt.m_t(
        mtxt.log_text(a, f * pow(a, n)),
        mtxt.log_text(a, f)
        ), str(n)

def reshi_uravnenie_proportsiya():
    nd = rnd.randint(1, 2)
    d = rnd.choice([2, 3, 5, 7, 11, 13])
    n1 = mrnd.choice_w([2, 3, 5, 7, 11, 13], [d])
    n2 = mrnd.choice_w([2, 3, 5, 7, 11, 13], [d, n1])

    an, ad = mf.s_fraction((d * (n1 if nd == 1 else n2), (n2 if nd == 1 else n1)))

    return mtxt.f_t(n1, "x" if nd == 1 else d) + " = " + mtxt.f_t(n2, "x" if nd == 2 else d), \
           mtxt.f_t(an, ad)


def umnozh_krestminusnakrest_i_sostav_uravnenie_x_v_znamenatele():
    nd = rnd.randint(1, 2)
    n = rnd.choice([2, 3, 5, 7, 11, 13])
    d1 = mrnd.choice_w([2, 3, 5, 7, 11, 13], [n])
    d2 = mrnd.choice_w([2, 3, 5, 7, 11, 13], [n, d1])

    an, ad = mf.s_fraction((n * (d1 if nd == 1 else d2), (d2 if nd == 1 else d1)))

    return mtxt.f_t("x" if nd == 1 else n, d1) + " = " + mtxt.f_t("x" if nd == 2 else n, d2), \
           mtxt.f_t(an, ad)

def umnozh_krestminusnakrest_i_sostav_uravnenie():
    nd = rnd.randint(1, 2)
    n = rnd.choice([2, 3, 5, 7, 11, 13])
    d1 = mrnd.choice_w([2, 3, 5, 7, 11, 13], [n])
    d2 = mrnd.choice_w([2, 3, 5, 7, 11, 13], [n, d1])
    return mtxt.f_t ("x" if nd == 1 else n, d1) + " = " + mtxt.f_t ("x" if nd == 2 else n, d2), \
           mtxt.pr_t("x" if nd == 1 else n, d2) + " = "  + mtxt.pr_t("x" if nd == 2 else n, d1)

def prover_ravenstvo_umnozheniem_krestminusnakrest():
    n = rnd.choice([2, 3, 5, 7, 11, 13])
    d = mrnd.choice_w([2, 3, 5, 7, 11, 13], [n])
    k = rnd.randint(2, 6)
    r = rnd.choice([0, 0, 0, 1])
    return mtxt.f_t(n, d) + " = " + mtxt.f_t(n * k + r, d * k), ("да" if r == 0 else "нет")

def verno_li_ravenstvo():
    n = rnd.choice([2, 3, 5, 7, 11, 13])
    d = mrnd.choice_w([2, 3, 5, 7, 11, 13], [n])
    k = rnd.randint(2, 6)
    r = rnd.choice([0, 0, 0, 1])
    return mtxt.f_t(n, d) + " = " + mtxt.f_t(n * k + r, d * k), ("да" if r == 0 else "нет")

def reshenie_uravneniya_mnozhitel_x_ravno_proizvedeniyu():
    a = rnd.randint(2, 30)
    b1 = rnd.randint(2, 10)
    b2 = rnd.randint(2, 10)
    n, d = mf.s_fraction((b1 * b2, a))
    return mtxt.pr_t(a, "x") + " = " + mtxt.pr_t(b1, b2), mtxt.f_t(n, d)


def reshi_uravnenie_mnozhitel_x():
    a = rnd.randint(2, 30)
    b = rnd.randint(2, 30)
    n, d = mf.s_fraction((b, a))
    return mtxt.pr_t(a, "x") + " = " + str(b), mtxt.f_t(n, d)


def uprosti_zamena_osnovaniya_vyinesenie_stepeni_argumenta_razlozhenie_argumenta():
    a, n = mrnd.common_base_power()
    kbd = rnd.randint(2, 5)
    ak = rnd.randint(2, 5)
    k1 = rnd.randint(2, 3)
    a_n, a_d = mf.s_fraction_sum((n, 1), (1, k1))
    return mtxt.log_text(
        mtxt.pow_text(a, -ak, True),
        mtxt._(mtxt.pow_text(mtxt.pr_t(pow(a, n), mtxt.pow_text(a, k1, True)), kbd, True))
    ), mtxt.f_t(a_n * kbd * ak, a_d)

def uprosti_razlozhenie_argumenta_logarifma_irratsionalnyij_mnozhitel():
    a, n = mrnd.common_base_power()
    k = rnd.randint(2, 5)
    a_n, a_d = mf.s_fraction_sum((n, 1), (1, k))
    return mtxt.log_text(a, mtxt._(mtxt.pr_t(pow(a, n), mtxt.pow_text(a, k, True)))), mtxt.f_t(a_n, a_d)

def uprosti_razlozhenie_argumenta_logarifma():
    n = rnd.randint(2, 3)
    a = rnd.choice([2, 3, 5])
    b = mrnd.choice_w([2, 3, 5, 7], [a])
    return mtxt.log_text(a, pow(a, n) * b), mtxt.p_t(n, mtxt.log_text(a, b))


def uprosti_argument_kak_proizvedenie_vyinesenie_stepeni():
    n = rnd.randint(2, 7)
    a = rnd.choice([2, 3, 5, 7])
    b = mrnd.choice_w([2, 3, 5, 7, 11, 13], [a])
    return mtxt.log_text(a, mtxt.pr_t(mtxt.pow_text(a, n), b)), mtxt.p_t(n, mtxt.log_text(a, b))

def uprosti_argument_kak_proizvedenie():
	a = rnd.choice([2, 3, 5, 7])
	b = mrnd.choice_w([2, 3, 5, 7, 11, 13], [a])
	return mtxt.log_text(a, mtxt.pr_t(a, b)), mtxt.p_t(1, mtxt.log_text(a, b))

def uprosti_zamena_osnovaniya_vyinesenie_stepeni_argumenta():
    kb_n = rnd.choice([2, 3, 5, 7])
    kb_d = mrnd.choice_w([2, 3, 5, 7], [kb_n])
    n, kb = mrnd.common_base_power()
    ka_n = rnd.choice([2, 3, 5, 7])
    ka_d = mrnd.choice_w([2, 3, 5, 7], [ka_n])

    a_n, a_d = mf.s_fraction((kb_n * kb * ka_d, kb_d * ka_n))

    return mtxt.log_text(
            mtxt.pow_text(mtxt.pow_text(n, ka_n), -ka_d, True),
            mtxt.pow_text(mtxt.pow_text(pow(n, kb), kb_n), kb_d, True)
        ), mtxt.f_t(a_n, a_d)


def uprosti_s_vyineseniem_drobnoj_stepeni():
    k_n = rnd.choice([2, 3, 5, 7])
    k_d = mrnd.choice_w([2, 3, 5, 7], [k_n])
    a = rnd.choice([2, 3, 5, 7])
    b = mrnd.choice_w([2, 3, 5, 7], [a])
    return mtxt.log_text(a, mtxt.pow_text(mtxt.pow_text(b, k_n), k_d, True)), \
           mtxt.f_t(k_n, k_d) + "*" + mtxt.log_text(a, b)


def uprosti_s_vyineseniem_stepeni():
    n = rnd.randint(2, 9)
    a = rnd.choice([2, 3, 5, 7])
    b = mrnd.choice_w([2, 3, 5, 7], [a])
    return mtxt.log_text(a, mtxt.pow_text(b, n)), str(n) + "*" + mtxt.log_text(a, b)

def vyinesi_stepen_argumenta_iz_logarifma():
	n = rnd.randint(2, 9)
	return mtxt.log_text("a", mtxt.pow_text("b", n)), str(n) + "*" + mtxt.log_text("a", "b")

def vyirazi_drobnoe_osnovanie_cherez_logarifm_po_zadannomu_osnovaniyu_i_uprosti():
    n, k = mrnd.common_base_power()
    k1 = -rnd.choice([2, 3])
    return mtxt.log_text(mtxt.pow_text(n, k1, True), pow(n, k)) + " по основанию " + str(n), str(k * k1)

def vyirazi_cherez_logarifm_po_zadannomu_osnovaniyu_i_uprosti():
    n, k = mrnd.common_base_power()
    k1 = rnd.choice([2, 3])
    return mtxt.log_text(mtxt.pow_text(n, k1, True), pow(n, k)) + " по основанию " + str(n), str(k * k1)

def vyirazi_logarifm_logaminus_b_cherez_logarifm_po_osnovaniyu():
    n = rnd.randint(2, 12)
    return str(n), mtxt.log_text(n, "a") + "/" + mtxt.log_text(n, "b")

def poschitaj_prostoj_logarifm():
    n, k = mrnd.common_base_power()
    return mtxt.log_text(n, pow(n, k)), str(k)


def uprosti_raznost_kvadrata_summyi_kornej_i_kornya():
    n = mrnd.rnd_w(2, 6)
    k = mrnd.rnd_w(2, 5, [4])
    n1 = n * n * k
    n2 = mrnd.rnd_w(7, n1 - 1, [x * x for x in range(2, 16)])
    act = rnd.randint(0, 1)

    return "(" + mtxt.k_t(n1) + mtxt.p0m1(act) + mtxt.k_t(n2) + ")^2" + mtxt.p0m1(1 - act) + str(2 * n) + "*" + mtxt.k_t(k * n2), \
           mtxt.k_t(n1) + mtxt.p0m1(0) + mtxt.k_t(n2)

def vozvedi_v_kvadrat_summuraznost_kornej():
    n2 = mrnd.rnd_w(3, 20)
    n1 = mrnd.rnd_w(n2 + 1, 30)
    act = rnd.randint(0, 1)
    return "(" + mtxt.k_t(n1) + mtxt.p0m1(act) + mtxt.k_t(n2) + ")^2", \
           str(n1 + n2 if act == 0 else n1 - n2) + mtxt.p0m1(act) + "2*" + mtxt.k_t(n1 * n2)

def zapishi_proizvedenie_kornej_pod_odnim_kornem():
	n1 = mrnd.rnd_w(3, 30)
	n2 = mrnd.rnd_w(3, 30)
	return mtxt.k_t(n1) + " * " + mtxt.k_t(n2), mtxt.k_t(n1 * n2)

def vyichisli_logarifm_ot_osnovaniya_v_slozhnoj_stepeni():
    n, k1 = mrnd.common_base_power()
    k2 = mrnd.rnd_w0(-10, 10)
    return mtxt.log_text(n, mtxt.pow_text(pow(n, k1), k2)), str(k1 * k2)

def poschitaj_itogovuyu_stepen_chisla():
    n = rnd.randint(2, 10)
    k1 = rnd.randint(2, 10)
    k2 = rnd.randint(2, 10)
    return mtxt.pow_text(mtxt._(mtxt.pow_text(n, k1)), k2), mtxt.pow_text(n, k1 * k2)

def predstavit_chislo_v_vide_stepeni_s_osnovaniem_umenshenie():
    n, k = mrnd.common_base_power()
    return str(pow(n, k)) + " в виде степени с основанием " + str(n), mtxt.pow_text(n, k)

def vyichisli_logarifm_ot_chisla_yavlyayuscheesya_osnovaniem_v_stepeni():
    n, k = mrnd.common_base_power()
    return mtxt.log_text(n, pow(n, k)), str(k)

def vyichisli_logarifm_ot_osnovaniya_v_stepeni():
    n, k = mrnd.common_base_power()
    return mtxt.log_text(n, mtxt.pow_text(n, k)), str(k)

def sravnit_drobi_2_7_i_2_8():
    n = rnd.randint(2, 5)
    d1 = rnd.randint(n+1, 9)
    d2 = d1 + rnd.randint(1, 2)

    s1 = lgu.get_fraction_str((0, n, d1))
    s2 = lgu.get_fraction_str((0, n, d2))

    p = rnd.randint(0, 1)

    return (s1 + " и " +  s2 if p == 0 else s2 + " и " +  s1), (s1 + " > " + s2 if p == 0 else s2 + " < " + s1)

def uprosti_k_3_plus_2_k_2():
    a = rnd.randint(5, 11)
    b = rnd.randint(1, a - 1)
    sSymb = " + " if rnd.randint(0, 1) == 0 else " - "

    a1 = math.sqrt(a)
    if a == a1 * a1:
        a_s = str(int(a1))
    else:
        a_s = "k(" + str(a) + ")"

    b1 = math.sqrt(a)
    if b == b1 * b1:
        b_s = str(int(b1))
    else:
        b_s = "k(" + str(b) + ")"

    return "k(" + str(a + b) + sSymb + "2k(" + str(a*b) + "))", a_s + sSymb + b_s

def v_kakuyu_stepen_nujno_vozvesti_2_chotby_poluchit_16():
    n = rnd.randint(2, 5)
    k = rnd.randint(2, 4)
    return str(n) + ", чтобы получилось " + str(pow(n, k)), str(k)

def ravny_ili_net_x_2_umnojit_na_3_i_2_2_3():
    l = rnd.randint(2, 6)
    f = rnd.sample([2, 2, 2, 2, 3, 3, 3,  5], l)
    n = 1
    for fe in f:
        n *= fe

    s1 = ""
    s2 = ""

    t1 = rnd.randint(1, 3)
    if t1 == 1:
        s1 = "x^" + str(n)
    if t1 == 2:
        f1 = rnd.choice(f[1:])
        s1 = "x^(" + str(f1) + "*" + str(int(n/f1)) + ")"
    if t1 == 3:
        f1 = rnd.choice(f[1:])
        s1 = "(x^" + str(f1) + ")^" + str(int(n/f1))

    dx = rnd.choice([-2, -1, 1, 2])
    w = rnd.choice([0, 1])
    if w == 0:
        dx = 0

    t2 = lgu.rnd_except(1, 3, [t1])
    if t2 == 1:
        s2 = "x^" + str(n + dx)
    if t2 == 2:
        f1 = rnd.choice(f[1:])
        s2 = "x^(" + str(f1) + "*" + str(int(n/f1) + dx) + ")"
    if t2 == 3:
        f1 = rnd.choice(f[1:])
        s2 = "(x^" + str(f1) + ")^" + str(int(n/f1) + dx)

    if dx == 0:
        symb = " = "
    if dx > 0:
        symb = " < "
    if dx < 0:
        symb = " > "

    return s1 + " и " + s2, s1 + symb + s2

def uprosti_2_4_a():
    n = rnd.randint(2, 5)
    k = rnd.randint(2, 4)
    return "(" + str(n) + "^" + str(k) + ")^a", str(pow(n, k)) + "^a"

def chemu_raven_x_v_a_32_a_x_16():
    l = rnd.randint(2, 6)
    f = rnd.sample([2, 2, 2, 2, 3, 3, 3,  5], l)
    n = 1
    for fe in f:
        n *= fe
    x = rnd.choice(f)

    return "a^" + str(n) + " = (a^" + "x" + ")^" + str(int(n/x)), str(x)

def predstav_vyrajenie_2_32_v_vide_stepeni_s_osnovaniem_16():
    n = rnd.randint(2, 5)

    l = rnd.randint(2, 6)
    f = rnd.sample([2, 2, 2, 2, 3, 3], l)
    k = 1
    for fe in f:
        k *= fe

    kf = rnd.sample(f, 2)
    k1 = 1
    for fe in kf:
        k1 *= fe

    k2 = int(k/k1)

    return str(n) + "^" + str(k) + " в виде степени с основанием " + str(pow(n, k1)), str(pow(n, k1)) + "^" + str(k2)


def vychislit_2_v_stepeni_3():
    n = rnd.randint(2, 4)
    k = rnd.randint(2, 5)
    return str(n) + "^" + str(k), str(pow(n, k))

def sravnit_stepeni_chisla():
    n = rnd.randint(2, 10)
    k1 = rnd.randint(2, 5)
    k2 = rnd.randint(2, 5)
    dk = rnd.randint(0, 4)
    if dk != 0:
        dk = 0
    else:
        dk = rnd.choice([1, 2])

    s1 = str(n) + "^(" + str(k1) + "*" + str(k2) + ")"
    s1v = pow(n, k1 * k2)

    if rnd.randint(0, 1) == 1:
        s2 = "(" + str(n) + "^" + str(k1 + dk) + ")^" + str(k2)
        s2v = pow(pow(n, k1 + dk), k2)
    else:
        s2 = "(" + str(n) + "^" + str(k2) + ")^" + str(k1 + dk)
        s2v = pow(pow(n, k2), k1 + dk)

    if s1v == s2v:
        symb = " = "
    else:
        if s1v < s2v:
            symb = " < "
        else:
            symb = " > "

    return s1 + " и " + s2, s1 + symb + s2

def uprostit_koren_iz_a_v_stepeni_v_stepeni():
    k1 = rnd.choice(lgu.get_simple_numnbers()[:4])
    k2 = lgu.rnd_except(2, 10, [k1])

    return "(k^" + str(k1) + "(a)^"+str(k2) + ")^"+str(k1), "a^" + str(k2)

def vychislit_2_v_stepeni_log_2_3():
    n = rnd.randint(2, 5)
    k = lgu.rnd_except(2, 5, [n])
    return str(n) + "^(log"+str(n) + "->" + str(k) + ")", str(k)

def vychislit_e_v_stepeni_ln_3():
    k = rnd.randint(2, 9)
    return "e^(ln"+str(k) + ")", str(k)

def vychislit_10_v_stepeni_lg_3():
    k = rnd.randint(2, 9)
    return "10^(lg"+str(k) + ")", str(k)

def vychislit_e_v_stepeni_minus2_umnojit_na_ln_3():
    k1 = rnd.randint(2, 5)
    k2 = rnd.randint(2, 5)

    return "e^(-" + str(k1) + "ln" + str(k2) + ")", lgu.get_fraction_str((0, 1, pow(k2, k1)))


def vychislit_stepen_k_5_32():
    n = rnd.randint(2, 5)
    k = rnd.randint(2, 8-n)
    return "k^" + str(k) + "(" + str(pow(n, k)) + ")", str(n)

def vychislit_stepen_32_1_5():
    n = rnd.randint(2, 5)
    k = rnd.randint(2, 8-n)
    return str(pow(n, k)) + "^(1/" + str(k) + ")", str(n)

def vychislit_stepen_32_2_5():
    n = rnd.randint(2, 5)
    kd = rnd.randint(2, 8-n)
    kn = lgu.rnd_except(2, 8-n, [kd])
    return str(pow(n, kd)) + "^(" + str(kn) + "/" + str(kd) + ")", str(pow(n, kn))

def vychislit_stepen_32_4_10():
    n = rnd.randint(2, 5)
    kd = rnd.choice([2, 5])
    kn = lgu.rnd_except(2, 8-n, [kd])
    f = int(10/kd)
    return str(pow(n, kd)) + "^(" + str(kn * f) + "/" + str(kd * f) + ")", str(pow(n, kn))

def vychislit_stepen_32_0_4():
    n = rnd.randint(2, 5)
    kd = rnd.choice([2, 5])
    kn = lgu.rnd_except(2, 8-n, [kd])
    f = int(10/kd)
    return str(pow(n, kd)) + "^(" + str(kn/kd) + ")", str(pow(n, kn))

def vychislit_stepen_2_minus_2():
    n = rnd.randint(2, 5)
    k = rnd.randint(1, 3)
    return str(n) + "^(-" + str(k) + ")", "1/" + str(pow(n, k))

def vychislit_stepen_32_minus_0_4():
    n = rnd.randint(2, 5)
    kd = rnd.choice([2, 5])
    kn = lgu.rnd_except(2, 8-n, [kd])
    f = int(10/kd)
    return str(pow(n, kd)) + "^(-" + str(kn/kd) + ")", "1/" + str(pow(n, kn))

def vychislit_stepen_1_32_minus_0_4():
    n = rnd.randint(2, 5)
    kd = rnd.choice([2, 5])
    kn = lgu.rnd_except(2, 8-n, [kd])
    f = int(10/kd)
    return "1 / " + str(pow(n, kd)) + "^(-" + str(kn/kd) + ")", str(pow(n, kn))

def vnesti_drobnuy_mnojitel_pod_znak_kornya():
    n = rnd.randint(4, 10)
    k = rnd.randint(2, 5)
    return lgu.get_fraction_str((0, 1, k)) + " * k(" + str(n * n * k * k) + ")", str(n)

def sravnit_dva_kornya_iz_celyh_chisel():
    n1 = lgu.rnd_except(20, 80, [x * x for x in range(5, 8)])
    n2 = n1 + rnd.randint(-5, 5)
    if n2 == n1:
        sym = " = "
    else:
        sym = " > " if n1 > n2 else " < "
    return "k(" + str(n1) + ") и k(" + str(n2) + ")", "k(" + str(n1) + ")" + sym + "k(" + str(n2) + ")"

def raspolojit_chisla_v_poryadke_vozrostaniya_korni():
    count = rnd.randint(4, 7)
    numbers = []
    rep = rnd.randint(40, 60)
    while len(numbers) < count:
        dx = rnd.randint(-count, count)
        if rep + dx not in numbers:
            numbers.append(rep + dx)

    numbers = sorted(numbers, reverse=True)

    numbers_s = []
    for n in numbers:
        fs = lgu.factoring(n)
        if len(fs) == 2:
            numbers_s.append("k(" + str(n) + ")")
            continue

        df = list(set(fs))
        dfs = sorted(df)
        f2 = 0
        for f in dfs:
            if fs.count(f) >= 2:
                f2 = f
                break
        if f2 == 0:
            k = rnd.randint(2, 4)
            numbers_s.append(lgu.get_fraction_str((0, 1, k)) + "*k(" + str(n*k*k) + ")")
        else:
            numbers_s.append(str(f2) + "*k(" + str(int(n/(f2 * f2))) + ")")

    shuffled_numers_s = numbers_s.copy()
    rnd.shuffle(shuffled_numers_s)
    return str(shuffled_numers_s), str(numbers_s)

def vychisli_koren_iz_chisla_kvadrat():
    k = rnd.randint(3, 19)
    return "k(" + str(k * k) + ")", str(k)

def vychisli_koren_iz_proizvedenia_chisel():
    k1 = rnd.randint(3, 19)
    k2 = lgu.rnd_except(3, 19, [k1])
    return "k(" + str(k1 * k1) + "*" + str(k2 * k2) + ")", str(k1 * k2)

def vychisli_koren_iz_proizvedenia_chisel_odno_iz_chisel_ne_kvadrat():
    k1 = rnd.randint(3, 19)
    k2 = lgu.rnd_except(3, 30, [x * x for x in range(2, 7)])
    pos = rnd.choice([0, 1])
    return "k(" + (str(k1 * k1) if pos else str(k2)) + '*' + (str(k2) if pos else str(k1 * k1)) + ")", str(k1) + "*k(" + str(k2) + ")"

def razloji_chislo_na_proizvedenia_kvadrata_i_ne_kvadrata():
    k1 = rnd.randint(3, 7)
    k2 = lgu.rnd_except(3, 25, [x * x for x in range(2, 6)])
    return str(k1 * k1 * k2), str(k1 * k1) + " * " + str(k2)

def vynesti_mnojitel_iz_pod_znaka_kornya():
    k1 = rnd.randint(3, 6)
    k2 = lgu.rnd_except(3, 25, [x * x for x in range(2, 6)])
    return "k(" + str(k1 * k1 * k2) + ")", str(k1) + " * k(" + str(k2) + ")"

def koren_iz_chego_raven_chislu():
    k = rnd.randint(3, 20)
    return str(k), str(k * k)

def vnesti_mnojitel_pod_znak_kornya():
    k1 = rnd.randint(3, 6)
    k2 = lgu.rnd_except(3, 25, [x * x for x in range(2, 6)])
    return str(k1) + " * k(" + str(k2) + ")", "k(" + str(k1 * k1 * k2) + ")"

def vynesti_mnt_iz_znaka_kornya_i_vnesti_pod_drugoy_koren():
    k1 = rnd.randint(3, 20)
    k1f = lgu.factoring(k1)
    while len(k1f) < 2:
        k1 = rnd.randint(3, 20)
        k1f = lgu.factoring(k1)
    k2 = rnd.randint(3, 20)
    return "k(" + str(int(k1 * k1 / k1f[1])) + ") * k(" + str(k2 * k2 * k1f[1]) + ")", str(k1 * k2)

def sravnit_drobi_5_6_i_6_7():
    d1 = rnd.randint(3, 15)
    d2 = d1 + rnd.choice([-1, 1])
    n1 = d1 - 1
    n2 = d2 - 1

    a1_str = lgu.get_fraction_str((0, n1, d1))
    a2_str = lgu.get_fraction_str((0, n2, d2))

    return a1_str + " и " + a2_str, a1_str + (" < " if d1 < d2 else " > ") + a2_str

def ot_kakoy_drobi_do_1_dalshe():
    d1 = rnd.randint(3, 8)
    d2 = d1 + rnd.choice([-1, 1])
    n1 = d1 - 1
    n2 = d2 - 1

    a1_str = lgu.get_fraction_str((0, n1, d1))
    a2_str = lgu.get_fraction_str((0, n2, d2))

    return "от " + a1_str + " или от " + a2_str, "от " + (a1_str if n1 < n2 else a2_str)

def skolko__nehvataetot_n_m_do_1():
    n = rnd.randint(3, 9)

    return "от " + lgu.get_fraction_str((0, n-1, n)), lgu.get_fraction_str((0, 1, n))

def skolko_budet_esli_vzyat_1_m_n_raz():
    d = rnd.randint(3, 8)
    n = rnd.randint(2, d-1)
    return lgu.get_fraction_str((0, 1, d)) + " взять " + str(n) + " раз", ne.Division(elements=(ne.Number(n), ne.Number(d))).simplify().get_text()

def ot_kakogo_torta_kuski_bolshe():
    n1 = rnd.randint(2, 12)
    n2 = rnd.randint(2, 12)
    while n2 == n1:
        n2 = rnd.randint(2, 12)

    ans = "первого" if n1 < n2 else "второго"

    return "первый торот разрезали на " + str(n1) + ", а второй на " + str(n2) + " кусков", "Кусок от " + ans + " торта больше"

def narisuy_krug_razdelenny_na_chasti():
    return "на " + str(rnd.randint(2, 8)) + " частей", "рисунок"

def reshi_uravnenie_s_modulem_vida_m3x_minus_4_ravno_5():
    a = rnd.randint(-10, 10)
    while a == 0:
        a = rnd.randint(-10, 10)
    b = rnd.randint(-10, 10)
    p = pol.Polynomial([a, b], [1, 0])
    d = rnd.randint(0, 20)

    d1 = ne.Number(a)

    x1 = ne.Division(elements=(ne.Number(d-b), d1)).simplify()
    x2 = ne.Division(elements=(ne.Number(-d-b), d1)).simplify()

    return "|" + p.get_str()  + "| = " + str(d), x1.get_text() + " и " + x2.get_text()

def reshi_uravnenie_s_modulem_vida_mx_minus_4_ravno_5():
    b = rnd.randint(-10, 10)
    p = pol.Polynomial([1, b], [1, 0])
    d = rnd.randint(0, 20)
    return "|" + p.get_str()  + "| = " + str(d), str(d-b) + " и " + str(-d-b)

def reshi_uravnenie_s_modulem_vida_mx_ravno_3():
    d = rnd.randint(0, 30)
    return "|x| = " + str(d), str(- d) + " и " + str(d)

def kakoe_chislo_nahoditsya_na_rasstoyanii_ot_chisla_0():
    d = rnd.randint(1, 10)
    return "на расстоянии " + str(d), str(- d) + " и " + str(d)

def kakoe_chislo_nahoditsya_na_rasstoyanii_ot_drugogo_chisls():
    a = rnd.randint(-10, 10)
    d = rnd.randint(1, 10)
    return str(d) + " от числа " + str(a), str(a - d) + " и " + str(a + d)

def narisuy_chislovuyu_os_i_otmet_na_ney_chislo():
    return "Отметь число " + str(rnd.randint(-10, 10)), "рисунок"

def perevesti_obyknovennuyu_drob_v_desyatichnuyu():
    n = rnd.randint(1, 10)
    d = rnd.randint(2, 20)
    return str(n) + " / " + str(d), lgu.drob_to_dec(n, d)

def naydi_period_decyatichnoy_drobi():
    n = rnd.randint(1, 10)
    d = rnd.randint(2, 20)
    while d % 2 == 0 or d % 5 == 0 or n % d == 0:
        d = rnd.randint(1, 20)

    return str(n) + " / " + str(d), lgu.drob_to_dec(n, d)

def razdeli_poka_cifry_ne_nachnut_povtoryatsya():
    n = rnd.randint(1, 10)
    d = rnd.randint(2, 20)
    while d % 2 == 0 or d % 5 == 0 or n % d == 0:
        d = rnd.randint(1, 20)

    return str(n) + " / " + str(d), lgu.drob_to_dec(n, d)

def slojit_logarithmy_s_odinakovymy_osnovaniyami_chisla():
    osn = rnd.choice(lgu.get_simple_numnbers()[:4])
    ps1 = rnd.choice([-1, 1])
    p1 = rnd.randint(2, 4)
    ps2 = rnd.choice([-1, 1])
    p2 = rnd.randint(2, 4)

    if ps1 == -1:
        n1 = 1
        d1 = pow(osn, rnd.randint(1, 2))
        p1_s = lgu.get_fraction_str((0, 1, d1))
    else:
        n1 = pow(osn, p1)
        d1 = 1
        p1_s = str(n1)

    if ps2 == -1:
        n2 = 1
        d2 = pow(osn, rnd.randint(1, 2))
        p2_s = lgu.get_fraction_str((0, 1, d2))
    else:
        n2 = pow(osn, p2)
        d2 = 1
        p2_s = str(n2)

    a = ne.Division(elements=(ne.Number(n1 * n2), ne.Number(d1 * d2))).simplify()


    return "log" + str(osn) + "->" + p1_s + " + " + "log" + str(osn) + "->" + p2_s, "log" + str(osn) + "->" + a.get_text()

def razdeli_v_stolbik_cherez_zapyatuty():
    n = rnd.choice([1,3,5,7,9,11,13,17])
    d = pow((5 if rnd.randint(0, 1) == 1 else 2), rnd.randint(1, 4))

    return str(n) + " : " + str(d), str(n/d)

def razdeli_v_stolbik():
    n = rnd.randint(200, 2000)
    k = rnd.randint(1, 9)

    return str(n * k) + " : " + str(k), str(n)

def vydeli_celuyu_chast_iz_drobi():
    x = rnd.randint(3, 20)
    k = rnd.randint(2, 5)
    return str(x * k + rnd.randint(0, x-1)) + "/" + str(x), str(k)

def skolko_raz_chislo_umeshaetsya_v_chisle():
    x = rnd.randint(3, 20)
    k = rnd.randint(2, 5)
    return "число " + str(x) + " в числе " + str(x * k + rnd.randint(0, x-1)), str(k) + " раз"

def umnoj_odnochlen_na_mnogochlen():
    p1 = pol.Polynomial([rnd.randint(1, 12)], [rnd.randint(0, 4)])

    n1 = rnd.randint(7, 12)
    n2 = rnd.randint(4, n1-1)
    n3 = rnd.randint(0, n2-1)
    p2 = pol.Polynomial([rnd.randint(1, 5), rnd.randint(1, 5), rnd.randint(1, 5)], [n1, n2, n3])

    s = pol.Polynomial.product(polynomials=(p1, p2)).get_str()

    return p1.get_str(shuffle=True) + " на " + p2.get_str(shuffle=True), s

def slojit_logarithmy_s_raznymy_osnovaniyami():
    osn = rnd.choice(lgu.get_simple_numnbers()[:5])
    po = rnd.randint(1, 3)
    p1 = rnd.randint(1, 3)
    p2_d = po
    p2_n = rnd.randint(1, 3)

    a = ne.Division(elements=(ne.Number(p2_n), ne.Number(p2_d))).simplify()

    if type(a) == ne.Division:
        n = a.elements[0].n
        d = a.elements[1].n
        a_n = p1 * d + n
        a_d = d
        s = lgu.get_fraction_str((0, a_n, a_d))
    else:
        s = str(p1 + a.n)

    return "log" + str(osn) + "->" + str(pow(osn, p1)) + " + log" + str(pow(osn, po)) + "->" + str(pow(osn, p2_n)), s

def preobrazovat_obyknovennuyu_drob_v_desyatichnuyu():
    # Сгенерируем дробь
    n = rnd.choice(lgu.get_simple_numnbers()[:6])
    d = rnd.choice(lgu.get_simple_numnbers()[:4])
    while d == n:
        d = rnd.choice(lgu.get_simple_numnbers()[:4])

    return lgu.get_fraction_str((0, n, d)), lgu.drob_to_dec(n, d)

def zapishi_vyrajenie_v_vide_stepeni_s_rac_pokazatelem():

    # Сгеренирвем условие
    n1 = rnd.randint(1, 3)
    d1 = 1

    n2 = rnd.choice(lgu.get_simple_numnbers()[:4])
    d2 = rnd.choice(lgu.get_simple_numnbers()[:4])
    while d2 == n2:
        d2 = rnd.choice(lgu.get_simple_numnbers()[:4])

    n3 = rnd.choice(lgu.get_simple_numnbers()[:4])
    d3 = rnd.choice(lgu.get_simple_numnbers()[:4])
    while d3 == n3:
        d3 = rnd.choice(lgu.get_simple_numnbers()[:4])

    # Получим строку условия
    t = "x^" + str(n1) + " * " + str(d2) + "^к(x^" + str(n2) + ")/(" + str(d3) + "^к(x^" + str(n3) + "))"

    # Посчитаем ответ
    an_ = n2 * d3 - n3 * d2
    ad_ = d2 * d3

    an = n1 * ad_ + an_
    ad = ad_

    a = ne.Division(elements=(ne.Number(an), ne.Number(ad))).simplify().get_text()

    return t, "x^" + a

def poschitay_logarifm_mul():
    n1 = rnd.randint(1, 3)

    sign2 = rnd.choice([-1, 1])
    n2 = rnd.randint(2, 7)
    d2 = rnd.randint(2, 7)
    while d2 == n2:
        d2 = rnd.randint(2, 7)

    base = rnd.randint(2, 5)

    b1 = pow(base, n1)
    b2_str = ("1/" if sign2 == -1 else "") + str(d2) + "^" + "к" + "(" + str(base) + "^" + str(n2) + ")"

    r_n = n1 * d2 + sign2 * n2
    r_d = d2

    return "log" + str(base) + "->" + str(b1) + "*" + b2_str, lgu.get_fraction_str((0, r_n, r_d))

def postoit_graphik_funkcii_y_mod_x_2_smesh_sdvig():
    a = rnd.randint(1, 3)
    b = rnd.randint(1, 3)

    a1 = a * a
    b1 = 2 * a * b
    c1 = b * b - rnd.randint(1, 5)

    if rnd.randint(0, 1) == 0:
        sign_symb = "+"
    else:
        sign_symb = "-"

    c_str = ""
    if c1 != 0:
        if c1 > 0:
            c_str = "+" + str(c1)
        else:
            c_str = "-" + str(int(math.fabs(c1)))

    return "y = |" + ("" if a1 == 1 else str(a1)) + "x^2" + sign_symb + str(b1) + "|x|" + c_str + "|", "нет ответа"

def naydi_nok_dvuh_chisel():
    x, y = lgu.get_two_numbers_with_common_factors(2, 2, 2)
    return str(x) + ", " + str(y), str(lgu.nok(x, y))

def naydi_nod_dvuh_chisel():
    x, y = lgu.get_two_numbers_with_common_factors(2, 2, 2)
    return str(x) + ", " + str(y), str(lgu.nod(x, y))

def otmet_tochku_na_grafike():
    return "(" + str(rnd.randint(-7, 7)) + ", " + str(rnd.randint(-7, 7)) + ")", ""

def naydi_smeshenie_po_verticali_mejdu_dvumya_tochkami():
    x1 = rnd.randint(-7, 7)
    y1 = rnd.randint(-7, 7)
    x2 = rnd.randint(-7, 7)
    y2 = rnd.randint(-7, 7)
    return "(" + str(x1) + ", " + str(y1) + ") и (" + str(x1) + ", " + str(y2) + ")", str(y1-y2)

def naydi_smeshenie_po_gorizontali_mejdu_dvumya_tochkami():
    x1 = rnd.randint(-7, 7)
    y1 = rnd.randint(-7, 7)
    x2 = rnd.randint(-7, 7)
    y2 = rnd.randint(-7, 7)
    return "(" + str(x1) + ", " + str(y1) + ") и (" + str(x1) + ", " + str(y2) + ")", str(x1-x2)

def naydi_naklon_mejdu_dvumya_tochkami():
    k = rnd.randint(-5, 5)
    x1 = rnd.randint(-7, 7)
    y1 = rnd.randint(-7, 7)
    l = rnd.randint(2, 5)
    x2 = x1 + k * l
    y2 = y1 + k * l
    return "(" + str(x1) + ", " + str(y1) + ") и (" + str(x1) + ", " + str(y2) + ")", str(k)

def naydi_naklon_pryamoy_po_dvum_tochkam():
    k = rnd.randint(-5, 5)
    x1 = rnd.randint(-7, 7)
    y1 = rnd.randint(-7, 7)
    l = rnd.randint(2, 5)
    x2 = x1 + k * l
    y2 = y1 + k * l
    return "(" + str(x1) + ", " + str(y1) + ") и (" + str(x1) + ", " + str(y2) + ")", str(k)

def bez_postroeniya_opredeli_prohodit_li_grafik_cherez_tochku():
    task_type = rnd.randint(0, 1)

    x1 = rnd.randint(-7, 7)
    y1 = rnd.randint(-7, 7)
    l = list(range(-5, 0)) + list(range(1, 6))
    k = rnd.choice(l)

    b = {
        0: y1 - k * x1,
        1: y1 - k * x1 + rnd.randint(1, 4)
    }[task_type]

    answer = "проходит" if task_type == 0 else "не проходит"

    return "функция y = " + pol.Polynomial([k, b], [1, 0]).get_str() + ", точка: (" + str(x1) + ", " + str(y1) + ")", answer

def opredeli_smeshenie_i_naklon_grafika_funcii():
    l = list(range(-5, 0)) + list(range(1, 6))
    k = rnd.choice(l)
    b = rnd.randint(-7, 7)
    return "y = " + pol.Polynomial([k, b], [1, 0]).get_str(), "наклон = " + str(k) + " смещение = " + str(b)

def naydi_smeshenie_esli_izvesten_naklon_i_tochka():
    l = list(range(-5, 0)) + list(range(1, 6))
    k = rnd.choice(l)

    x1 = rnd.randint(-7, 7)
    y1 = rnd.randint(-7, 7)

    b = y1 - k * x1

    return "k = " + str(k) + " точка: (" + str(x1) + ", " + str(y1) + ")", str(b)

def nayti_lineynuyu_funkciyi_po_dvum_tochkam():
    type_id = rnd.randint(1, 2)
    l = list(range(-6, -1)) + list(range(1, 6))
    k = rnd.choice(l)
    b = rnd.randint(-5, 5)

    x1 = rnd.randint(-10, 10)
    y1 = k * x1 + b
    x2 = rnd.choice(list(range(-10, x1)) + list(range(x1 + 1, 11)))
    y2 = k * x2 + b

    answer = "y = " + pol.Polynomial([k, b], [1, 0]).get_str()
    res = ("график этой функции проходит через точки (" + str(x1) + ", " + str(y1) + ") и (" + str(x2) + ", " + str(y2) + ")", answer)
    return res

def postroy_ryad_po_tekstu():
    x = rnd.randint(3, 7)
    y = rnd.randint(1, 5)
    answer = [1 + (n-1) * y for n in range(1, x+1)]
    text = "В семье " + str(x) + " брата. Отец выдал первому брату 1 конфету, второму на " + str(y) + \
    " конфет больше чем первому, третьему на " + str(y) + " конфет больше чем второму, и так раздал конфеты всем детям. Составь ряд чисел, который бы " \
                                                           "показывал сколько конфет у каждого брата."
    return text, str(answer)

def poschitay_medianu_po_tekstu():
    x = rnd.randint(3, 7)
    y = rnd.randint(1, 5)
    answer = [1 + (n-1) * y for n in range(1, x+1)]
    text = "В семье " + str(x) + " брата. Отец выдал первому брату 1 конфету, второму на " + str(y) + \
    " конфет больше чем первому, третьему на " + str(y) + " конфет больше чем второму, и так раздал конфеты всем детям. Найди медиану конфет у детей."

    return text, str(st.median(answer))

def sravnit_mediany_po_tekstu():
    x = rnd.randint(3, 7)
    n = rnd.randint(2, 3)
    y = rnd.randint(x + 3*n, 40)

    v1 = [y // x + (1 if ((y // x) * x + n <= y) else 0) for n in range(1, x + 1)]
    v2 = [1] * x
    v2 = [min(n * k, max(y - x - (n * sum(range(1, k))), 0)) + v2[k-1] for k in range(1, x + 1)]
    m1 = st.median(v1)
    m2 = st.median(v2)

    ans = ""
    if m1 == m2:
        ans = "медианы одинаковы"
    else:
        if m1 > m2:
            ans = "при втором способе"
        else:
            ans = "при первом способе"

    return "В семье " + str(x) + " сестры. Отец купил в магазине " + str(y) + " яблок. Когда он ехал из магазина домой, " \
            "то думал, что раздаст яблоки сестрам так: сначала всем по одной, потом еще по одной и так пока не кончатся" \
            " яблоки. " + ("При этом, возможно, получится не поровну. " if y % x != 0 else "") + "А когда приехал раздал " \
            "так: сначала всем по одному яблоку, а потом первой сестре добавил еще " + str(n) + " яблок, второй сестре добавил на " + \
            str(n) + " яблок больше чем первой и т.д. пока яблоки не кончились. При каком способе раздачи медиана яблок " \
            "по сестрам будет минимальной?", ans

def yavlyaetsya_li_funkciya_lineynoy():
    res = ""
    type_id = rnd.randint(1, 9)
    a1 = rnd.choice([-6, -2] + [2, 6])
    a2 = rnd.choice([-6, -2] + [2, 6])
    b = rnd.randint(-5, 5)
    res = {
        1: "y = " + pol.get_str([a1, b], [1, 0]),
        2: "y = " + pol.get_str([a1, b], [rnd.randint(2, 5), 0]),
        3: "y = " + pol.get_str([b, a1], [0, 1]),
        4: "y = 1/x" + pol.get_str([b], [0]),
        5: "y = (" + pol.get_str([a1, b], [1, 0]) + ") / " + str(a2),
        6: "y = " + str(a1) + "/(" + pol.get_str([a2, b], [1, 0]) + ")",
        7: "y = " + str(a1) + "/(" + pol.get_str([b, a2], [0, 1]) + ")",
        8: "y = (" + pol.get_str([b, int(math.fabs(a1))], [0, 1]) + ") / " + str(a2),
        9: "y = (" + pol.get_str([b, -int(math.fabs(a1))], [0, 1]) + ") / " + str(a2),
    }[type_id]

    return res, "да" if type_id in [1, 3, 5, 8, 9] else "нет"

def naydi_lineynuyu_funkciyu_esli_izvesnto_chto():
    type_id = rnd.randint(1, 2)
    l = list(range(-6, -1)) + list(range(1, 6))
    k = rnd.choice(l)
    b = rnd.randint(-5, 5)

    x1 = rnd.randint(-10, 10)
    y1 = k * x1 + b
    x2 = rnd.choice(list(range(-10, x1)) + list(range(x1 + 1, 11)))
    y2 = k * x2 + b

    answer = "y = " + pol.Polynomial([k, b], [1, 0]).get_str()

    res = {
        1: ("график этой функции параллелен графику функции y = " + pol.Polynomial([k, rnd.randint(10, 10)], [1, 0]).get_str() +
            " и, этот график проходит через точку (" + str(x1) + ", " + str(y1) + ")", answer),
        2: ("график этой функции проходит через точки (" + str(x1) + ", " + str(y1) + ") и (" + str(x2) + ", " + str(y2) + ")", answer),
    }[type_id]

    return res

def naydi_neizvestnye_koefficienty_mnogochlrnov():
    l = list(range(-7, 0)) + list(range(1, 8))
    a1 = rnd.choice(l)
    b1 = rnd.choice(l)
    a2 = rnd.choice(l)
    b2 = rnd.choice(l)
    p1 = pol.Polynomial([a1, b1], [rnd.randint(0, 2), rnd.randint(3, 7)])
    p2 = pol.Polynomial([a2, b2], [rnd.randint(0, 2), rnd.randint(3, 7)])
    p = pol.Polynomial.product(polynomials=[p1, p2])


    def replace(s):
        replace_index = rnd.randint(0, 1)
        c = p1.monomials[replace_index].coefficient
        power = p1.monomials[replace_index].power
        replace_str = ""

        if c < 0:
            replace_str += "-"
            if math.fabs(c) != 1:
                replace_str += str(int(math.fabs(c)))
        else:
            if replace_index == 1:
                replace_str += "+"
            if math.fabs(c) != 1:
                replace_str += str(c)

        replace_coeff_str = replace_str
        if power != 0:
            if power == 1:
                replace_str += "x"
            else:
                replace_str += "x^" + str(power)
        if replace_index == 1:
            replace_str += ")"
        else:
            replace_str = "(" + replace_str

        p1_str = "(" + p1.get_str() + ")"
        r_index = p1_str.index(replace_str) + (1 if replace_index == 0 else 0)
        return p1_str.replace(p1_str[r_index: r_index + len(replace_coeff_str)], "__", 1)

    p1_str = replace("(" + p1.get_str() + ")")
    p2_str = "(" + p2.get_str() + ")"#replace("(" + p2.get_str() + ")")

    res = p1_str + " * " + p2_str + " = " + p.get_str()

    return res, p1.get_str()

def naydi_nod_chislitelya_i_znamenatelya_i_sokrati_na_nego():
    s = list(lgu.get_simple_numnbers())[:3:]
    common_factor = rnd.choice(s) + rnd.choice(s)
    n = rnd.choice(s)
    s.remove(n)
    d = rnd.choice(s)
    return lgu.get_fraction_str((0, n * common_factor, d * common_factor)), lgu.get_fraction_str((0, n, d))

def skolko_poluchitsya_esli_vzyat_1_n_n_raz():
    n = rnd.randint(2, 7)
    return lgu.get_fraction_str((0, 1, n)) + " взять " + str(n) + " раз", str(1)

def skolko_poluchitsya_esli_vzyat_1_n_mn_raz():
    n = rnd.randint(2, 5)
    m = rnd.randint(2, 5)
    return lgu.get_fraction_str((0, 1, n)) + " взять " + str(n * m) + " раз", str(m)

def skolko_drobey_vida_1_n_soderjitsya_v_1():
    n = rnd.randint(2, 7)
    return lgu.get_fraction_str((0, 1, n)), str(n)

def skolko_drobey_vids_1_n_soderjitsya_v_m():
    n = rnd.randint(2, 7)
    m = rnd.randint(2, 7)
    return lgu.get_fraction_str((0, 1, n)) + " содержится в " + str(m), str(n * m)

def umnoj_drob_vida_1_n_na_n():
    n = rnd.randint(2, 7)
    return lgu.get_fraction_str((0, 1, n)) + " на " + str(n), str(1)

def umnoj_drob_vida_m_n_na_n():
    m = rnd.randint(2, 5)
    n = rnd.randint(m + 1, 7)
    return lgu.get_fraction_str((0, m, n)) + " на " + str(n), str(m)



def razdeli_krug_i_podpishi_kajduyu_chast():
    n = rnd.randint(2, 8)
    return "на " + str(n) + " частей", "рисунок"

def naydi_nok_nod_dvuh_chisel():
    # Получаем массив с простыми числами для выборки
    simple_numbers_count = 7
    simple_numbers = list(lgu.get_simple_numnbers()[:simple_numbers_count])
    extended_simple_numbers = []
    for i, x in enumerate(simple_numbers):
        extended_simple_numbers += [x] * (simple_numbers_count - i)

    # Получаем общие множители
    common_factors_count = rnd.choice([0, 1, 1, 2, 2, 3])
    common_factors = []
    for i in range(common_factors_count):
        x = rnd.choice(extended_simple_numbers)
        common_factors.append(x)

    # Получаем множители 1-го числа
    n1_factors_count = rnd.randint(0, 4 - common_factors_count)
    n1_factors = []
    for i in range(n1_factors_count):
        x = rnd.choice(extended_simple_numbers)
        n1_factors.append(x)

    # Получаем множители 2-го числа
    n2_factors_count = rnd.randint(0, 4 - common_factors_count)
    n2_factors = []
    for i in range(n2_factors_count):
        x = rnd.choice(extended_simple_numbers)
        n2_factors.append(x)

    # Получаем числа
    n1 = 1
    for x in common_factors + n1_factors:
        n1 *= x
    n2 = 1
    for x in common_factors + n2_factors:
        n2 *= x

    # Считаем правильный ответ
    nod, nok = 1, 1
    for x in common_factors:
        nod *= x
        nok *= x

    factors = n1_factors
    for x in n2_factors:
        t = factors.count(x) - n2_factors.count(x)
        if t < 0:
            factors.append(x)

    for x in factors:
        nok *= x

    return str(n1) + ', ' + str(n2), "НОК = " + str(nok) + " НОД = " + str(nod)

def sokrati_drobi():
    s = list(lgu.get_simple_numnbers())[:7]
    n = rnd.choice(s)
    s.remove(n)
    d = rnd.choice(s)
    f = rnd.randint(3, 30)

    ans = str(n) + "/" + str(d)

    return str(n * f) + "/" + str(d * f), ans

def sravni_drobi_l1():
    d1 = rnd.randint(5, 20)
    d2 = d1 - rnd.randint(1, 4)
    d = [d1, d2]
    rnd.shuffle(d)

    if d[0] < d[1]:
        ans = "1/" + str(d[0]) + " > " + "1/" + str(d[1])
    if d[0] > d[1]:
        ans = "1/" + str(d[0]) + " < " + "1/" + str(d[1])
    if d[0] == d[1]:
        ans = "1/" + str(d[0]) + " = " + "1/" + str(d[1])

    return "1/" + str(d[0]) + "   " + "1/" + str(d[1]), ans

def sravni_drobi_l2():
    s = list(lgu.get_simple_numnbers())[:5] + [1]
    n = rnd.choice(s)
    s.remove(n)
    d = rnd.choice(s)
    f = rnd.randint(3, 30)
    d1_str = str(n * f) + "/" + str(d * f)
    d1 = n / d

    n = rnd.choice(s)
    s.remove(n)
    d = rnd.choice(s)
    d2_str = str(n) + "/" + str(d)
    d2 = n / d

    drobi = [d1_str, d2_str]
    rnd.shuffle(drobi)

    if d1 == d2:
        ans = d1_str + " = " + d2_str
    else:
        ans = d1_str + " > " + d2_str if d1 > d2 else d1_str + " < " + d2_str

    return drobi[0] + "   " + drobi[1], ans

def privedi_drob_k_nujnomu_znamenatelyu():
    n = rnd.randint(0, 50)
    d = rnd.randint(1, 20)
    c = rnd.randint(2, 10)
    nd = d * c

    ans = lgu.get_fraction_str((0, n * c, d * c))

    return str(n) + "/" + str(d) + " к знаменателю " + str(nd), ans

def kakoy_obshiy_znamenatel_u_drobey():
    n1 = rnd.randint(1, 10)
    n2 = rnd.randint(1, 10)

    d1, d2 = lgu.get_two_numbers_with_common_factors(rnd.randint(0, 2), rnd.randint(1, 2), rnd.randint(1, 2))

    ans = str(lgu.nok(d1, d2))

    return str(n1) + "/" + str(d1) + " и " + str(n2) + "/" + str(d2), ans

def privedi_drobi_k_obshemu_znamenatelyu():
    simple_numbers_count = 7
    simple_numbers = list(lgu.get_simple_numnbers()[:simple_numbers_count])
    extended_simple_numbers = []
    for i, x in enumerate(simple_numbers):
        extended_simple_numbers += [x] * (simple_numbers_count - i)

    common_factors_count = rnd.randint(0, 2)
    common_factors = [rnd.choice(extended_simple_numbers) for x in range(common_factors_count)]

    d1_factors_count = rnd.randint(0, 2)
    d1_factors = [rnd.choice(extended_simple_numbers) for x in range(d1_factors_count)] + common_factors

    d2_factors_count = rnd.randint(0, 2)
    d2_factors = [rnd.choice(extended_simple_numbers) for x in range(d2_factors_count)] + common_factors

    d1 = 1
    for x in d1_factors:
        d1 *= x

    d2 = 1
    for x in d2_factors:
        d2 *= x

    n1 = rnd.randint(1, 15)
    n2 = rnd.randint(1, 15)

    nk = lgu.nok(d1, d2)

    ans = lgu.get_fraction_str((0, n1 * int(nk / d1), d1)) + " и " + lgu.get_fraction_str((0, n2 * int(nk / d2), d2))

    return str(n1) + "/" + str(d1) + " и " + str(n2) + "/" + str(d2), ans

def reshi_uravnenie_s_modulem_l1():
    a = rnd.choice([-1, 1])
    b = rnd.randint(-15, 15)
    p = pol.Polynomial([a, b], [1, 0])
    c = rnd.randint(0, 20)

    x1 = ne.Division(elements=(ne.Number(c - b), ne.Number(a))).simplify().get_text()
    x2 = ne.Division(elements=(ne.Number(-c - b), ne.Number(a))).simplify().get_text()

    return "|" + p.get_str(shuffle=True) + "| = " + str(c), x1 + ", " + x2

def reshi_uravnenie_s_modulem_l2():
    r = list(range(-10, 10))
    r.remove(0)

    a1 = rnd.choice(r)
    b1 = rnd.choice(r)
    a2 = rnd.choice(r)
    b2 = rnd.choice(r)

    p1 = pol.Polynomial([a1, b1], [1, 0])
    p2 = pol.Polynomial([a2, b2], [1, 0])
    c1 = rnd.choice(r)
    c1_str = "+" + str(c1) if c1 > 0 else str(c1)
    c2 = rnd.randint(0, 20)

    a = a1 + c1 * a2
    b = b1 + c1 * b2

    if a != 0:
        x1 = ne.Division(elements=(ne.Number(c2 - b), ne.Number(a))).simplify().get_text()
        x2 = ne.Division(elements=(ne.Number(-c2 - b), ne.Number(a))).simplify().get_text()
        ans = x1 + ", " + x2
    else:
        ans = "нет корней"

    return "|" + p1.get_str(shuffle=True) + c1_str + "(" + p2.get_str(shuffle=True) + ")| = " + str(c2), ans

def reshi_uravnenie_s_modulem_l3():
    a1 = rnd.choice([rnd.randint(-10, 0), rnd.randint(1, 11)])
    b1 = rnd.choice([rnd.randint(-10, 0), rnd.randint(1, 11)])
    a2 = rnd.choice([rnd.randint(-10, 0), rnd.randint(1, 11)])
    b2 = rnd.choice([rnd.randint(-10, 0), rnd.randint(1, 11)])

    p1 = pol.Polynomial([a1, b1], [1, 0])
    p2 = pol.Polynomial([a2, b2], [1, 0])

    a = a1 - a2
    b = b2 - b1
    if a != 0:
        x1 = b/a
        if x1 * a2 + b2 < 0 :
            x1_str = ""
        else:
            x1_str = ne.Division(elements=(ne.Number(b), ne.Number(a))).simplify().get_text() + ", "
    else:
        x1_str = ""

    a = a1 + a2
    b = -b2 - b1
    if a != 0:
        x2 = b/a
        if x2 * a2 + b2 < 0 :
            x2_str = ""
        else:
            x2_str = ne.Division(elements=(ne.Number(b), ne.Number(a))).simplify().get_text()
    else:
        x2_str = ""

    ans = x1_str + x2_str
    if ans == "":
        ans = "нет корней"
    return "|" + p1.get_str(shuffle=True) + "| = " + p2.get_str(shuffle=True), ans

def reshi_lineynoe_uravnenie():
    r = list(range(-10, 10))
    r.remove(0)

    l = rnd.randint(3, 6)

    p1c = rnd.sample(population=r, k=l)
    p1p = rnd.sample(population=[0]*5 + [1]*5, k=l)

    p1 = pol.Polynomial(p1c, p1p)
    r_count = int(l/2)
    r_indicies = rnd.sample(range(0, l-1), r_count)
    replacement_pols = {x:pol.Polynomial([rnd.choice(r), rnd.choice(r)], [1, 0]) for x in r_indicies}
    left_str = p1.get_replaced_str(replacements=replacement_pols)

    a1 = 0
    b1 = 0
    for x in range(l):
        if x in r_indicies:
            a1 += p1c[x] * pol.Polynomial.simplify(replacement_pols[x].monomials).get_c_by_p(1)
            b1 += p1c[x] * pol.Polynomial.simplify(replacement_pols[x].monomials).get_c_by_p(0)
        else:
            if p1p[x] == 1:
                a1 += p1c[x]
            else:
                b1 += p1c[x]

    l = rnd.randint(3, 4)
    p2c = rnd.sample(population=r, k=l)
    p2p = rnd.sample(population=[0]*5 + [1]*5, k=l)

    p1 = pol.Polynomial(p2c, p2p)
    r_count = int(l/2)
    r_indicies = rnd.sample(range(0, l-1), r_count)
    replacement_pols = {x:pol.Polynomial([rnd.choice(r), rnd.choice(r)], [1, 0]) for x in r_indicies}
    right_str = p1.get_replaced_str(replacements=replacement_pols)

    a2 = 0
    b2 = 0
    for x in range(l):
        if x in r_indicies:
            a2 += p2c[x] * pol.Polynomial.simplify(replacement_pols[x].monomials).get_c_by_p(1)
            b2 += p2c[x] * pol.Polynomial.simplify(replacement_pols[x].monomials).get_c_by_p(1)
        else:
            if p2p[x] == 1:
                a2 += p2c[x]
            else:
                b2 += p2c[x]

    ans = "не известно"
    if a1 == a2 and b1 == b2:
        ans = "корень - любое число"
    if a1 == a2 and b1 != b2:
        ans = "нет корней"
    if a1 != a2 and b1 != b2:
        ans =  ne.Division(elements=(ne.Number(b2 - b1), ne.Number(a1 - a2))).simplify().get_text()

    return left_str + " = " + right_str, ans

def naydi_harakteristiki_ryada():
    mod_count = rnd.randint(0, 3)
    res = rnd.sample(range(-100, 100), rnd.randint(3, 13))
    for i in range(1, mod_count):
        r = [rnd.randint(-100, 100)] * (i + 1)
        res += r

    rnd.shuffle(res)
    ans = "СА = " + ne.Division(elements=(ne.Number(sum(res)), ne.Number(len(res)))).simplify().get_text() + ", "
    ans += "Размах = " + str(max(res) - min(res)) + ", "

    cnt = {x: res.count(x) for x in set(res)}
    m = 0
    xm = 0
    for x in cnt.keys():
        if cnt[x] > m:
            m = cnt[x]
            xm = x
    ans += "нет моды " if list(cnt.values()).count(m) > 1 else "Мода = " + str(xm) + ", "
    ans += "Медиана = " + str(st.median(res)) + ", "
    return str(res), ans

def postroy_grafiki_funkciy():
    ans = "нет ответа"
    return str(["y = " + pol.Polynomial([rnd.randint(-5, 5), rnd.randint(-5, 5)], [1, 0]).get_str() for x in range(rnd.randint(2, 3))]), ans

def vychisli():
    k = rnd.randint(-50, 50)
    n = ne.Number(k)
    n = ne.spread_out(n, 0, 4)

    n.remove_brackets()
    n.brackets = False

    ans = str(k)

    return n.get_text(), ans

def narisuy_os_i_sdelay_na_ney_operacii():
    x = rnd.randint(-10, 10)
    res = str(x)

    ops_count = rnd.randint(4, 7)
    for i in range(ops_count):
        v = rnd.randint(-10, 10)
        res += " + " if v > 0 else " - "
        if v < 0:
            v = -v
        res += str(v)

    ans = "нет ответа"

    return res, ans

def narisuy_os_i_naydi_rasstoyanie_mejdy_tochkami():
    x1 = rnd.randint(-10, 10)
    x2 = rnd.randint(-10, 10)
    return str(x1) + " и " + str(x2), str(int(math.fabs(x2 - x1)))

def reshi_uravnenie():

    ur_type = rnd.randint(0, 0)

    res = ""
    if ur_type == 0: # 200 - 4(300 - 2(2x - 4)) = 300
        x = rnd.randint(10, 30)
        t1 = rnd.randint(2, 5)
        t2 = rnd.randint(1, 10)
        res += "(" + str(t1) + " * x" + " - "+ str(t2) + ")"
        t = t1*x - t2
        t3 = rnd.randint(2, 4)
        res = str(t3) + " * " + res
        t = t*t3
        t4 = t + rnd.randint(1, 100)
        t = t4 - t
        res = "(" + str(t4) + " - " + res + ")"
        t5 = rnd.randint(2, 5)
        res = str(t5) + " * " + res
        t = t5 * t
        t6 = t + rnd.randint(1, 100)
        res = str(t6) + " - " + res
        t = t6 - t

        res = res + " = " + str(t)

    ans = "нет ответа"

    return res, ans

def reshi_uravnenie_ax_b__cx_d():
    x = rnd.choice([2, 10])
    a = rnd.randint(1, 5)
    b = rnd.choice([1, a - 1] + [a + 1, 10])
    c = x * (a - b)
    c1 = rnd.choice([c - 10, c - 1] + [c + 1, c + 10])
    c2 = c - c1
    p1 = pol.Polynomial([a, -c1], [1, 0])
    p2 = pol.Polynomial([b, c2], [1, 0])
    return p1.get_str() + " = " + p2.get_str(), "x = " + str(x)

def raspoloji_drobi_v_poryadke_vozrostania():
    c = rnd.randint(5, 10)
    ans = "нет ответа"
    return str([str(rnd.randint(1, 10)) + "/" + str(rnd.randint(2, 20)) for i in range(c)]), ans

def reshi_equation_system_m1():
    ans = "нет ответа"
    return "", ans

def sloji_drobi():
    c1 = rnd.randint(1, 10)
    c2 = rnd.randint(1, 10)
    n1 = rnd.randint(1, 10)
    n2 = rnd.randint(1, 10)
    d1 = rnd.randint(n1 + 1, 20)
    d2 = rnd.randint(n2 + 1, 20)

    ans = "нет ответа"

    return ("" if c1 == 1 else str(c1) + " ")  + str(n1) + "/" + str(d1) + (" + " if rnd.randint(0, 1) == 0 else " - ") + ("" if c2 == 1 else str(c2) + " ") + str(n2) + "/" + str(d2), ans

def umnoj_drobi():
    c1 = rnd.randint(1, 10)
    c2 = rnd.randint(1, 10)
    n1 = rnd.randint(1, 10)
    n2 = rnd.randint(1, 10)
    d1 = rnd.randint(n1 + 1, 20)
    d2 = rnd.randint(n2 + 1, 20)

    ans = "нет ответа"

    return ("" if c1 == 1 else str(c1) + " ")  + str(n1) + "/" + str(d1) + " * " + ("" if c2 == 1 else str(c2) + " ") +  str(n2) + "/" + str(d2), ans

def naydi_drob_ot_chisla():
    d_type = rnd.randint(1, 5)
    c = rnd.randint(2, 10) if d_type == 1 else 1
    n = rnd.randint(1, 10)
    d = rnd.randint(n + 1, 15)

    if rnd.randint(0, 1) == 0:
        n2 = rnd.randint(1, 10) * d
    else:
        n2 = rnd.randint(1, 50)

    ans = "нет ответа"

    return ("" if c == 1 else str(c) + " ") + str(n) + "/" + str(d) + " от " + str(n2), ans

def naydi_procent_ot_chisla():
    n1 = rnd.randint(0, 9)
    c = rnd.randint(1, 10)
    if c in [1, 2, 3, 4, 5]:
        n = n1 * 10
    if c in [6, 7, 8]:
        n = n1 * 10 + 5
    if c in [9, 10]:
        n = n1 * 10 + rnd.randint(1, 10)

    n1 = rnd.randint(0, 9)
    c = rnd.randint(1, 10)
    if c in [1, 2, 3, 4, 5]:
        n2 = n1 * 100
    if c in [6, 7, 8]:
        n2 = n1 * 100 + rnd.randint(1, 9) * 10
    if c in [9]:
        n2 = n1 * 100 + rnd.randint(1, 9) + 5
    if c in [10]:
        n2 = n1 * 100 + rnd.randint(1, 99)

    if rnd.randint(0, 1) == 0:
        n2 = rnd.randint(1, 10) * 100
    else:
        n2 = rnd.randint(1, 50)

    ans = "нет ответа"

    return str(n) + "%" + " от " + str(n2), ans

def vychisli_drobi():
    terms_count = rnd.randint(2, 3)
    res = ""
    for i in range(terms_count):
        operation = rnd.randint(0, 1)
        bracket = rnd.randint(0, 1)
        operation_in_bracket = rnd.randint(0, 1)
        d1 = lgu.get_random_fraction(mixed_possible=True)
        d2 = lgu.get_random_fraction(mixed_possible=True)
        d3 = lgu.get_random_fraction(mixed_possible=True)
        if i > 0:
            res += " + " if operation == 0 else " - "
        res += lgu.get_fraction_str(d1)
        if bracket:
            res += "(" + lgu.get_fraction_str(d2) + " " + ("+" if operation_in_bracket == 0 else "-") + " " + lgu.get_fraction_str(d3) + ")"

    ans = "нет ответа"

    return res, ans

def graph_naydi_tochku_peresecheniya():
    ans = "нет ответа"
    return str(["y = " + pol.Polynomial([rnd.randint(-5, 5), rnd.randint(-5, 5)], [1, 0]).get_str() for x in range(rnd.randint(2, 3))]), ans

def vychisli_stepen_drobnogo_chisla():
    d_type = rnd.randint(0, 1)
    p = rnd.randint(2, 3)

    if d_type == 0:
        d_str = lgu.get_fraction_str(lgu.get_random_fraction(mixed_possible=True))
    else:
        d_str = str(rnd.randint(1, 20)/10)

    ans = "нет ответа"

    return "(" + ("" if rnd.randint(0, 1) == 0 else "-") + d_str + ")^" + str(p), ans

def sravni_stepeni_drobey():
    ans = "нет ответа"
    res = vychisli_stepen_drobnogo_chisla()[0] + " и " + vychisli_stepen_drobnogo_chisla()[0]
    return res, ans

def umnoj_mnogochleny():
    powers_available = [0, 1, 2, 3, 4, 5, 6]
    coeffs_available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    monomials_count = rnd.randint(2, 4)

    p1 = pol.Polynomial(rnd.sample(coeffs_available, monomials_count), rnd.sample(powers_available, monomials_count))
    p2 = pol.Polynomial(rnd.sample(coeffs_available, monomials_count), rnd.sample(powers_available, monomials_count))

    ans = "нет ответа"

    return p1.get_str(shuffle=True) + " и " + p2.get_str(shuffle=True), ans

def umnoj_drobi_sokrasheniem():
    n_unique_factors_count = rnd.randint(0, 1)
    d_unique_factors_count = rnd.randint(0, 1)

    s = list(lgu.get_ex_simple_numbers(6))
    rnd.shuffle(s)

    n_unique_factors = [s[x] for x in range(n_unique_factors_count)]
    d_unique_factors = [s[n_unique_factors_count + x] for x in range(d_unique_factors_count)]

    f_count = rnd.randint(2, 4)
    common_factors = []
    for i in range(f_count):
        t = s[i]
        common_factors.extend([t]*rnd.randint(1, 2))

    n_factors = common_factors + n_unique_factors
    d_factors = common_factors + d_unique_factors

    terms_count = rnd.randint(2, 4)
    n_terms = [1] * terms_count
    d_terms = [1] * terms_count
    for x in n_factors:
        t = rnd.randint(0, terms_count - 1)
        n_terms[t] *= x
    for x in d_factors:
        t = rnd.randint(0, terms_count - 1)
        d_terms[t] *= x

    res = ""
    for i in range(terms_count):
        res += str(n_terms[i]) + "/" + str(d_terms[i])
        if i != terms_count - 1:
            res += " * "

    ans = "нет ответа"

    return res, ans