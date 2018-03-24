import random as rnd
import gen.genutils.common as lgu
import gen.genutils.math_polynomial as pol
import gen.genutils.math_numeric_expressions as ne
import gen.genutils.math_rnd as mrnd
import gen.genutils.math_text as mtxt
import gen.genutils.math_factors as mf
import gen.genutils.math_trig as tr
import statistics as st
import math

def proizvedenie_dvuh_posledovatelnyih_natrualnyih_chisel():
# Произведение двух последовательных натруальных чисел:
    # на 6 больше меньшего | большего из них
    # равно 6
    # на 6 меньше суммы квадратов этих числел
    # на 6 больше разности квадратов этих чисел

    t = rnd.randint(0, 3)
    x = rnd.randint(2, 11)

    if t == 0:
        m = rnd.randint(0, 1)
        if m == 0: #меньшего
            text = "на " + str(pow(x, 2)) + " больше меньшего из них"
        if m == 1:
            text = "на " + str(pow(x, 2) - 1) + " больше большего из них"

    if t == 1:
        text = "равно " + str(pow(x, 2) + x)

    if t == 2:
        text = "на " + str(pow(x, 2) + x + 1) + " меньше суммы квадратов этих чисел"

    if t == 3:
        text = "на " + str(pow(x, 2) - x - 1) + " больше разности квадратов этих чисел"

    return text + ". Найдите эти числа", str(x) + ", " + str(x + 1)


def reshite_uravnenie666():
# Решите уравнение: (x^2 - x)/2 + x/3 = -1

    x1 = mrnd.rnd_w(-10, 10, [0])
    x2 = mrnd.rnd_w(-10, 10, [0, x1])
    a =mrnd.rnd_w(-3, 3, [0, x1, x2])
    b = mrnd.rnd_w(-10, 10, [0])
    d = rnd.randint(2, 5)
    c = b * d - a * d * (x1 + x2)
    pn, pd = mf.s_fraction((a * x1 * x2, a * d * (x1 + x2) - b*d))

    return mtxt._(mtxt.fc(a) + "x^2" + mtxt.fc(-b, is_first=False) + "x") + "/" + (mtxt._(c) if c < 0 else str(c)) + " + x/" +str(d) + "=" + mtxt.f_t(pn, pd), \
           str(x1) + ", " + str(x2)


def reshite_uravnenie665():
# Решите уравнение: (x - 1)(x + 2) = 2x + 3
    x1 = mrnd.rnd_w(-10, 10, [0])
    x2 = mrnd.rnd_w(-10, 10, [0, x1])
    a = mrnd.rnd_w(-10, 10, [0, x1, x2])
    b = mrnd.rnd_w(-10, 10, [0, x1, x2, a])
    p = x1 + x2 - (a + b)
    q = a * b - x1 * x2

    return mtxt._("x" + mtxt.s(-a)) + mtxt._("x" + mtxt.s(-b)) + "=" + mtxt.fc(p) + "x" + mtxt.s(q), \
           str(x1) + ", " + str(x2)


def reshite_uravnenie664():
# Решите уравнение: (x - 1)(x+3/2)(x^2 - 6x - 7) = 0
    c = rnd.randint(2, 4)
    pk = rnd.randint(0, c - 1)

    res = [] #(v, answer)
    for i in range(c):
        if i == pk:
            t = rnd.randint(0, 2)
            if t == 0:
                a = ""
                bu = mrnd.rnd_w(-10, 10, [0])
                au = mrnd.rnd_w(-10, 10, [0, bu])
                cu = int(pow(bu, 2) / (4 * au)) + rnd.randint(2, 5)
                v = mtxt.fc(au) + "x^2" + mtxt.fc(bu, is_first=False) + "x" + mtxt.s(cu)

            if t == 1:
                t1 = rnd.randint(0, 1)
                if t1 == 0:
                    x = mrnd.rnd_w(-10, 10, [0])
                    a = str(x)
                    v = "x^2" + mtxt.fc(2 * x, is_first=False) + "x" + mtxt.s(pow(x, 2))
                if t1 == 1:
                    xn, xd = mf.s_fraction((mrnd.rnd_w(-5, 5, [0]), rnd.randint(2, 7)))
                    a = mtxt.f_t(xn, xd)
                    bun, bud = mf.s_fraction((2 * xn, xd))
                    cun, cud = mf.s_fraction((pow(xn, 2), pow(xd, 2)))
                    v = "x^2" + ("+" if bun > 0 else "") + mtxt.f_t(bun, bud) + "x" + ("+" if cun > 0 else "") + mtxt.f_t(cun, cud)
            if t == 2:
                t1 = rnd.randint(0, 1)
                if t1 == 0:
                    x1 = mrnd.rnd_w(-10, 10, [0])
                    x2 = mrnd.rnd_w(-10, 10, [0, x1])
                    a = ", ".join([str(x1), str(x2)])
                    v = "x^2" + mtxt.fc(-(x1 + x2), is_first=False) + "x" + mtxt.s(x1 * x2)

                if t1 == 1:
                    x1n = mrnd.rnd_w(-5, 5, [0])
                    x1d = mrnd.rnd_w(2, 5, [0, 1, x1n])
                    x1n, x1d = mf.s_fraction((x1n, x1d))
                    x2n = mrnd.rnd_w(-5, 5, [0, x1n])
                    x2d = mrnd.rnd_w(2, 5, [0, 1, x2n, x2n])
                    x2n, x2d = mf.s_fraction((x2n, x2d))

                    a = ", ".join([mtxt.f_t(x1n, x1d), mtxt.f_t(x2n, x2d)])

                    bun, bud = mf.s_fraction((-(x1n*x2d + x1d*x2n), x1d * x2d))
                    cun, cud = mf.s_fraction((x1n * x2n, x1d * x2d))
                    v = "x^2" + ("+" if bun > 0 else "") + mtxt.f_t(bun, bud) + "x" + ("+" if cun > 0 else "") + mtxt.f_t(cun, cud)
        else:
            t = rnd.randint(0, 1)
            if t == 0:
                r = mrnd.rnd_w(-10, 10, [0])
                v = "x" + mtxt.s(-r)
                a = str(r)
            else:
                k = mrnd.rnd_w(1, 5, [0])
                n = mrnd.rnd_w(-10, 10, [0])
                d = mrnd.rnd_w(2, 10, [0, n])
                n, d = mf.s_fraction((n, d))
                v = mtxt.fc(k) + "x" + ("+" if n < 0 else "") + mtxt.f_t(-n, d)
                n, d = mf.s_fraction((n, d * k))
                a = mtxt.f_t(n, d)

        res.append((v, a))

    return "".join(["(" + str(x[0]) + ")" for x in res]), ", ".join([x for x in set(x[1] for x in res) if x != ""])


def sravnite():
# Сравните tg3 и ctg2 // в радианах через pi
    t = rnd.randint(0, 2)

    f1 = rnd.randint(0, 1)
    f2 = rnd.randint(0, 1)

    n1 = rnd.randint(-3, 3)
    d1 = rnd.randint(2, 6)
    n1, d1 = mf.s_fraction((n1, d1))

    n2 = rnd.randint(-3, 3)
    d2 = rnd.randint(2, 6)
    n2, d2 = mf.s_fraction((n2, d2))

    v1 = ("tg" if f1 == 0 else "ctg") + mtxt._(mtxt.f_t(n1, d1) + "*pi")
    v2 = ("tg" if f2 == 0 else "ctg") + mtxt._(mtxt.f_t(n2, d2) + "*pi")

    if (f1 == 0 and d1 == 2 and n1 % 2 == 1) or (f1 == 1 and (d1 == 1 or n1 == 0)):
        answer = v1 + " не существует"
    elif (f2 == 0 and d2 == 2 and n2 % 2 == 1) or (f2 == 1 and (d2 == 1 or n2 == 0)):
        answer = v2 + " не существует"
    else:
        a1 = math.tan(n1 / d1 * math.pi) if f1 == 0 else 1 / math.tan(n1 / d1 * math.pi)
        a2 = math.tan(n2 / d2 * math.pi) if f2 == 0 else 1 / math.tan(n2 / d2 * math.pi)
        answer = v1 + (" > " if a1 > a2 else (" < " if a1 < a2 else "=")) + v2

    return v1 + " и " + v2, answer

def otmette_na_osi():
# Отметьте на оси tg|ctg точки +- k(3)|1|2|k(3)/3
    c = rnd.randint(0, 1)
    s = rnd.choice([-1, 1])
    t = rnd.randint(0, 1)

    v = ("-" if s < 0 else "") + "k(3)" if t == 0 else "1/k(3)"

    return ("tg" if c == 0 else "ctg") + " точки " + v, "график"

def otmette_na_edinichnoj_okruzhnosti_ugol_dlya_kotorogo():
# Отметьте на единичной окружности угол для которого tg|ctg = +|- 1/2|1/3|1/4|1|2|3|4|5
    c = rnd.randint(0, 1)
    t = rnd.randint(0, 1)
    s = rnd.choice([-1, 1])

    if t == 0:
        v = str(s * rnd.randint(0, 5))
    else:
        v = mtxt.f_t(s, rnd.randint(2, 4))

    return ("tg" if c == 0 else "ctg") + "=" + v, "график"

def suschestvuet_li():
# Существует ли: tg|ctg для угла 2pi/3 // взять любые и углы и те где нет tg или ctg
    c = rnd.randint(0, 1)
    t = rnd.randint(0, 1)

    if t == 0:
        if c == 1:
            n = rnd.randint(1, 6)
            d = mrnd.rnd_w(n + 1, 7, [2 * n])
            k = rnd.randint(-3, 3)
            n, d = mf.s_fraction((n + 2 * k * d, d))
        else:
            n = rnd.randint(1, 6)
            d = rnd.randint(n + 1, 7)
            k = rnd.randint(-3, 3)
            n, d = mf.s_fraction((n + 2 * k * d, d))
    else:
        if c == 0:
            n = 1
            d = 2
            k = rnd.randint(-5, 5)
            n, d = mf.s_fraction((n + k * d, d))
        else:
            n = 0
            d = 1
            k = rnd.randint(-5, 5)
            n, d = mf.s_fraction((n + k * d, d))

    return ("tg" if c == 0 else "ctg") + " для угла " + mtxt.f_t(n, d) + "*pi", "да" if t == 0 else "нет"

def vyichislite659():
# Вычислите arccos(cos(+/-9)) // тоже самое с arcsin
    c = rnd.randint(0, 1)
    x = mrnd.rnd_w(-10, 10, [0])

    # Определяем в какой четверти лежит угол x
    xgrad = x * 180 / math.pi
    ch360 = int(xgrad) % 360
    if ch360 > 0:
        ch = 1 if ch360 < 90 else (2 if ch360 < 180 else (3 if ch360 < 270 else 4))
    else:
        ch = 4 if -ch360 < 90 else (3 if -ch360 < 180 else (2 if -ch360 < 270 else 1))

    def get_n(a):
        if a > 0:
            return int(a // 1)
        else:
            return -int((-a + 1) // 1)

    answer = ""
    if c == 0:
        if ch in [1, 2]:
            n = get_n(x/(2 * math.pi))
            answer = str(x) + ((mtxt.fc(int(-2 * n), False) + "pi") if n != 0 else "")
        if ch == 3:
            n = get_n(x/(4 * math.pi) - 1/4)
            nsh = get_n(x/(2 * math.pi) - 1/2 - 2 * n)
            answer = ((mtxt.fc(int(2 + 4 * n + 2 * nsh)) + "pi") if ((2 + 4 * n + 2 * nsh) != 0) else "") + mtxt.s(-x)
        if ch == 4:
            n = get_n(x/(4 * math.pi) + 1/8)
            nsh = get_n(x/(2 * math.pi) + 1/4 - 2 * n)
            answer = ((mtxt.fc(int(4 * n + 2 * nsh)) + "pi") if (4 * n + 2 * nsh != 0) else "") + mtxt.s(-x)

    if c == 1:
        if ch in [4, 1]:
            n = get_n(x/(2 * math.pi) + 1/4)
            answer = str(x) + ((mtxt.fc(int(-2 * n), False) + "pi") if n != 0 else "")
        if ch == 2:
            n = get_n(x/(4 * math.pi) - 1/8)
            nsh = get_n(x/(2 * math.pi) - 1/4 - 2 * n)
            answer = ((mtxt.fc(int(1 + 4 * n + 2 * nsh)) + "pi") if (1 + 4 * n + 2 * nsh != 0) else "") + mtxt.s(-x)
        if ch == 3:
            n = get_n(x/(4 * math.pi) + 1/4)
            nsh = get_n(x/(2 * math.pi) + 3/4 - 2 * n)
            answer = ((mtxt.fc(int(-1 + 4 * n + 2 * nsh)) + "pi") if (-1 + 4 * n + 2 * nsh != 0) else "") + mtxt.s(-x)


    return ("arccos" if c == 0 else "arcsin") + mtxt._(("cos" if c == 0 else "sin") + mtxt._(x)), \
          answer

def vyichislite658():
# Вычислите arccos(cos(7pi/4)) // тоже самое с arcsin
    c = rnd.randint(0, 1)

    d = rnd.randint(2, 6)
    n = (rnd.randint(1, d - 1)) if c == 0 else (rnd.choice([-1, 1]) * rnd.randint(1, d //2))

    n, d = mf.s_fraction((n, d))
    answer = mtxt.f_t(n, d) + "*pi"

    n += rnd.randint(1, 3) * 2 * d
    txt = mtxt.f_t(n, d) + "*pi"

    return ("arccos" if c == 0 else "arcsin") + mtxt._(("cos" if c == 0 else "sin") + txt), answer

def verno_li_utverzhdenie657():
# Верно ли утверждение: arcsin|arccos(sin|cos(2pi/3)) = 2pi/3
    c = rnd.randint(0, 1)
    t = rnd.randint(0, 1)

    if c == 0:
        d = rnd.randint(2, 10)
        if t == 0:
            n = rnd.randint(1, d - 1)
        else:
            if rnd.randint(0, 1):
                n = rnd.randint(d + 1, 12)
            else:
                n = -rnd.randint(1, d - 1)

    if c == 1:
        d = rnd.randint(2, 10)
        if t == 0:
            n = rnd.choice([-1, 1]) * rnd.randint(1, d // 2)
        else:
            n = rnd.choice([-1, 1]) * rnd.randint(d // 2 + 1,  12)

    n, d = mf.s_fraction((n, d))
    v = mtxt.f_t(n, d) + "*pi"

    return ("arccos" if c == 0 else "arcsin") + mtxt._(("cos" if c == 0 else "sin") + mtxt._(v)) + " = " + v, \
           "да" if t == 0 else "нет"

def reshite_neravenstvo656():
# Решите неравенство: sin|cos(x) <|> +|- 1/2 // Все табличные значения и некоторые дроби
    c = rnd.randint(0, 1)
    lr = rnd.randint(0, 1)
    vs = ["-1", "-k(3)/2", "-k(2)/2", "-1/2", "-1/3", "-1/4", "-1/5", "0", "1/5", "1/4", "1/3", "1/2", "k(2)/2", "k(3)/2", "1"]
    v = rnd.choice(vs)

    v1 = {
        "-1": "pi" if c == 0 else "3pi/2",
        "-k(3)/2": "5pi/6" if c == 0 else "4pi/3" ,
        "-k(2)/2": "3pi/4" if c == 0 else "5pi/4",
        "-1/2": "2pi/3" if c == 0 else "7pi/6",
        "-1/3": "arccos(-1/3)" if c == 0 else "pi + arcsin(1/3)",
        "-1/4": "arccos(-1/4)" if c == 0 else "pi + arcsin(1/4)",
        "-1/5": "arccos(-1/5)" if c == 0 else "pi + arcsin(1/5)",
        "0": "pi/2" if c == 0 else "0",
        "1/5": "arccos(1/5)" if c == 0 else "arcsin(1/5)",
        "1/4": "arccos(1/4)" if c == 0 else "arcsin(1/4)",
        "1/3": "arccos(1/3)" if c == 0 else "arcsin(1/3)",
        "1/2": "pi/3" if c == 0 else "pi/6",
        "k(2)/2": "pi/4" if c == 0 else "pi/4",
        "k(3)/2": "pi/6" if c == 0 else "pi/3",
        "1": "0" if c == 0 else "pi/2",
    }[v]

    v2 = {
        "-1": "3pi" if c == 0 else "7pi/2",
        "-k(3)/2": "7pi/6" if c == 0 else "5pi/3",
        "-k(2)/2": "5pi/4" if c == 0 else "7pi/4",
        "-1/2": "4pi/3" if c == 0 else "11pi/6",
        "-1/3": "pi + arccos(1/3)" if c == 0 else "2pi - arcsin(1/3)",
        "-1/4": "pi + arccos(1/4))" if c == 0 else "2pi - arcsin(1/4)",
        "-1/5": "pi + arccos(1/5)" if c == 0 else "2pi - arcsin(1/5)",
        "0": "3pi/2" if c == 0 else "pi",
        "1/5": "2pi - arccos(1/5)" if c == 0 else "pi - arcsin(1/5)",
        "1/4": "2pi - arccos(1/4)" if c == 0 else "pi - arcsin(1/4)",
        "1/3": "2pi - arccos(1/3)" if c == 0 else "pi - arcsin(1/3)",
        "1/2": "5pi/3" if c == 0 else "5pi/6",
        "k(2)/2": "7pi/4" if c == 0 else "3pi/4",
        "k(3)/2": "11pi/6" if c == 0 else "2pi/3",
        "1": "2pi" if c == 0 else "5pi/2",
    }[v]

    if v in ["1", "-1"]:
        answer = "нет решений" if lr == 0 and v == "1" or lr == 1 and v == "-1" else ("любое кроме " + v1 + "+2pi*n")
    else:
        if lr == 0 or v == "0":
            answer = "[" + v2 + "+2pi*(n-1), " + v1 + "+2pi*n" + "], n - целое"
        else:
            answer = "[" + v1 + "+2pi*n, " + v2 + "+2pi*n" + "], n - целое"

    return ("cos" if c == 0 else "sin") + "(x)" + (">" if lr == 0 else "<") + v, answer

def zashtrihujte_vse_uglyi_a_dlya_kotoryih_verno():
# Заштрихуйте все углы альфа, для которых верно sin|cos(альфа) >|< k(2)/2|1/3
    c = rnd.randint(0, 1)
    vs = ["-1", "-k(3)/2", "-k(2)/2", "-1/2", "-1/3", "-1/4", "-1/5", "0", "1/2", "1/5", "1/4", "1/3", "k(2)/2", "k(3)/2", "1"]
    v = rnd.choice(vs)
    s = rnd.randint(0, 1)

    return ("cos" if c == 0 else "sin") + mtxt._("a") + (">" if s == 0 else "<") + v, 'график'


def vyirazite_ugol_a_cherez():
# Выразите угол a через: arccos|arcsin , если cos|sin(a)=m (m>0|m<0) и -pi/2<=a<=pi/2 // сделать разные интервалы
    ac = rnd.randint(0, 1)
    if rnd.randint(0, 3) != 0:
        c = 1-ac
    else:
        c = ac
    s = rnd.randint(0, 1)

    if ac == c:
        answer = ("arccos" if ac == 0 else "arcsin") + "(m)"
    else:
        if c == 0:
            answer = "pi - arcsin(1-m^2)" if s == 1 else "arcsin(1-m^2)"
        else:
            answer = "-arccos(1-m^2)" if s == 1 else "arccos(1-m^2)"

    return ("arccos" if ac == 0 else "arcsin") + ", если " + ("cos" if c == 0 else "sin") + "(a)=m " +\
           "(m" + (">" if s == 0 else "<") + "0) и " + ("-pi/2<=a<=pi/2" if c == 1 else "0<=a<=pi"),\
           answer

def vyichislite653():
# Вычислите sin|cos(arcsin|arccos) k(2)/2
    c = rnd.randint(0, 1)
    ac = rnd.randint(0, 1)

    vs = ["-1", "-k(3)/2", "-k(2)/2", "-1/2", "0", "1/2", "k(2)/2", "k(3)/2", "1"]
    v = rnd.choice(vs)

    def aac(c, ca, a):
        if c == ca:
            return a
        else:
            return {
                "-1": "0",
                "-k(3)/2": "1/2",
                "-k(2)/2": "k(2)/2",
                "-1/2": "k(3)/2",
                "0": "1",
                "1/2": "k(3)/2",
                "k(2)/2": "k(2)/2",
                "k(3)/2": "1/2",
                "1": "0",
            }[a]

    return ("cos" if c == 0 else "sin") + mtxt._(("arccos" if ac == 0 else "arcsin") + mtxt._(v)), aac(c, ac, v)

def najdite_otrezki_gde_y_0_yravno0_i_y_0_dlya_funktsii():
# Для функции: y = -|x - 4| - 2 найдите отрезки где y<0; y=0 и y>0 // модуль, параблоа, корень, гипербола
    t = rnd.randint(1, 4)

    s = rnd.randint(0, 1)
    text = "y = "

    if t == 1:  # модуль
        b = mrnd.rnd_w(-7, 7, [0])
        c = rnd.randint(-7, 7)
        text += ("" if s == 0 else "-") + mtxt.mod("x" + mtxt.s(b)) + mtxt.s(c)
        answer = "y = 0 " + ("ни в одной точке" if (s == 0 and c > 0 or s == 1 and c < 0) else \
            (("в точке " + str(-b)) if c == 0 else \
            ("в точках " + str(-c-b) + " и " + str(c-b)))) + "; "
        answer += "y > 0 на " + ("пустом множестве" if (s == 1 and c < 0) else \
            ("(-oo; +oo)" if (s == 0 and c > 0) else \
            ("(-oo; " + str(c-b) + ")U(" + str(-c-b) + "; +oo)") if s==0 else \
            ("(" + str(-c-b) + "; " + str(c-b) + ")"))) + "; "
        answer += "y < 0 на" + ("пустом множестве" if (s == 0 and c > 0) else \
            ("(-oo; +oo)" if (s == 1 and c < 0) else \
            ("(-oo; " + str(c-b) + ")U(" + str(-c-b) + "; +oo)") if s==1 else \
            ("(" + str(-c-b) + "; " + str(c-b) + ")")))


    if t == 2:  # парабола
        a = rnd.randint(1, 3)
        b = mrnd.rnd_w(-7, 7, [0])
        c = mrnd.rnd_w(-3, 3, [0])

        text += ("" if s == 0 else "-") + mtxt.fc(a) + mtxt._("x" + mtxt.s(b)) + "^2" + mtxt.s(c)

        c1, a1 = mf.s_fraction((c, a))
        c1 = int(math.fabs(c1))
        com = mtxt.k_t(mtxt.f_t(c1, a1))
        x1 = str(-b) + "-" + com
        x2 = str(-b) + "+" + com

        answer = "y = 0 " + ("ни в одной точке" if (s == 0 and c > 0 or s == 1 and c < 0) else \
            (("в точке " + str(-b)) if c == 0 else \
            ("в точках " + x1 + " и " + x2))) + "; "
        answer += "y > 0 на " + ("пустом множестве" if (s == 1 and c < 0) else \
            ("(-oo; +oo)" if (s == 0 and c > 0) else \
            ("(-oo; " + x2 + ")U(" + x1 + "; +oo)") if s==0 else \
            ("(" + x1 + "; " + x2 + ")"))) + "; "
        answer += "y < 0 на" + ("пустом множестве" if (s == 0 and c > 0) else \
            ("(-oo; +oo)" if (s == 1 and c < 0) else \
            ("(-oo; " + x2 + ")U(" + x1 + "; +oo)") if s==1 else \
            ("(" + x1 + "; " + x2 + ")")))

    if t == 3:  # корень
        b = rnd.randint(-7, 7)
        text += ("" if s == 0 else "-") + mtxt.k_t("x" + mtxt.s(b))
        answer = "y = 0 в точке " + str(-b) + "; "
        answer += "y > 0 на " + (("(" + str(-b) + "; +oo)") if s == 0 else "пустом множестве") + "; "
        answer += "y < 0 на " + (("(" + str(-b) + "; +oo)") if s == 1 else "пустом множестве") + ";"

    if t == 4:  # гипербола
        a = mrnd.rnd_w(-3, 3, [0])
        b = mrnd.rnd_w(-7, 7, [0])
        c = mrnd.rnd_w(-3, 3, [0])

        text += str(a) + "/" + mtxt._("x" + mtxt.s(b)) + mtxt.s(c)

        a1, c1 = mf.s_fraction((-a - b * c, c))
        x1 = mtxt.f_t(a1, c1)
        answer = "y = 0 в точке " + x1 + "; "\
            "y > 0 на " + (("(" + x1 + "; +oo)") if s == 0 else ("(-oo; " + x1 + ")")) + "; "\
            "y < 0 на " + (("(" + x1 + "; +oo)") if s == 1 else ("(-oo; " + x1 + ")")) + ";"

    return text, answer


def opredelite_otrezki_gde_vozrastaet_i_ubyivaet_funktsiya():
# Для функции: y = -|x - 4| - 2 определите отрезки где функция возрастает и убывает // модуль, параблоа, корень, гипербола
    t = rnd.randint(1, 4)

    s = rnd.randint(0, 1)
    text = "y = "

    if t == 1: # модуль
        b = mrnd.rnd_w(-7, 7, [0])
        c = mrnd.rnd_w(-7, 7, [0])
        text += ("" if s == 0 else "-") + mtxt.mod("x" + mtxt.s(b)) + mtxt.s(c)
        if s == 0:
            answer = "возрастает на [" + str(-b) + "; +oo), убывает на (-oo; " + str(-b) + "]"
        else:
            answer = "возрастает на (-oo; " + str(-b) + "], убывает на [" + str(-b) + " ; +oo)"

    if t == 2: #парабола
        a = rnd.randint(1, 3)
        b = mrnd.rnd_w(-7, 7, [0])
        c = mrnd.rnd_w(-3, 3, [0])
        text += ("" if s == 0 else "-") + mtxt.fc(a) + mtxt._("x" + mtxt.s(b)) + "^2" + mtxt.s(c)
        if s == 0:
            answer = "возрастает на [" + str(-b) + "; +oo), убывает на (-oo; " + str(-b) + "]"
        else:
            answer = "возрастает на (-oo; " + str(-b) + "], убывает на [" + str(-b) + " ; +oo)"

    if t == 3: #корень
        b = rnd.randint(-7, 7)
        text += ("" if s == 0 else "-") + mtxt.k_t("x" + mtxt.s(b))
        if s == 0:
            answer = "возрастает на [" + str(-b) + "; +oo)"
        else:
            answer = "убывает на [" + str(-b) + "; +oo)"

    if t == 4: #гипербола
        a = rnd.randint(1, 3)
        b = mrnd.rnd_w(-7, 7, [0])
        c = mrnd.rnd_w(-3, 3, [0])
        text += ("" if s == 0 else "-") + str(a) + "/" + mtxt._("x" + mtxt.s(b)) + mtxt.s(c)
        if s == 0:
            answer = "убывает на (-oo; " + str(-b) + ") U (" + str(-b) + "; +oo)"
        else:
            answer = "возрастает на (-oo; " + str(-b) + ") U (" + str(-b) + "; +oo)"

    return text, answer


def postrojte_grafik_funktsii650():
# Постройте график функции: y = k(x^2 + 10x + 25) //корень из полного квадрата
    a = mrnd.rnd_w(-3, 3, [0])
    b = mrnd.rnd_w(-7, 7, [0])
    return "y = k(" + mtxt.fc(pow(a, 2)) + "x^2" + mtxt.fc(2 * a * b, False) + "x" + mtxt.s(pow(b, 2)) + ")", "график"


def postrojte_grafik_funktsii649():
# Постройте график функции: y = 3x^2 + 24x + 46 //вынести множитель и получить полный квадрат, добавить и отнять
    a = mrnd.rnd_w(-3, 3, [0])
    b = mrnd.rnd_w(-7, 7, [0])
    c = mrnd.rnd_w(-5, 5, [0])
    k = mrnd.rnd_w(-3, 3, [0, 1])

    return "y = " + mtxt.fc(k * pow(a, 2)) + "x^2" + mtxt.fc(2 * k * a * b, False) + "x" + mtxt.s(k * pow(b, 2) + c) , "график"


def reshite_uravnenie648():
# Решите уравнение: 2/(x-2)=k(x+1) // гипербола = корень, a>0
    r = rnd.randint(1, 2)

    p = rnd.randint(-3, 3)

    if r == 1:
        m = rnd.randint(2, 4)
        x = p + pow(m, 2)
        b = rnd.randint(-5, p - 1)
        c = rnd.randint(1, m - 1)
        a = m * p - c * p + pow(m, 3) - pow(m, 2) * c - b * m + b * c
        answer = str(x)

    if r == 2:
        m1 = rnd.randint(1, 4)
        m2 = m1 + 2
        a = int((pow(m2, 2) - pow(m1, 2))/2)
        c = int((m1 + m2)/2)
        b = p + int((pow(m2, 2) + pow(m1, 2))/2)
        x1 = b - a
        x2 = b + a
        answer = str(x1) + " и " + str(x2)

    text = str(a) + "/" + mtxt._("x" + mtxt.s(-b)) + mtxt.s(c) + "=" + mtxt.k_t("x" + mtxt.s(-p))

    return text, answer

def reshite_uravnenie647():
# Решите уравнение: -3/(x-3)=1-x // гипербола = прямая
    t = rnd.choice([0, 2, 2, 2])

    a = mrnd.rnd_w(-5, 5, [0])
    b = mrnd.rnd_w(-5, 5, [0])
    c = mrnd.rnd_w(-5, 5, [0])

    if t == 0:
        p = rnd.randint(-7, 0)
        q = c - p * b;
        r = 1
        answer = "нет решений"

    if t == 2:
        r = rnd.randint(1, 6)

        if r == 1:
            p = -1
            q = c - 1 - a + b
            x1 = b-a
            x2 = b-1
        if r == 2:
            p = -1
            q = c + 1 + a + b
            x1 = b+a
            x2 = b+1
        if r == 3:
            p = 1
            q = c - 1 + a - b
            x1 = b-a
            x2 = b+1
        if r == 4:
            p = 1
            q = c + 1 - a - b
            x1 = b-a
            x2 = b+1
        if r == 5:
            p = a
            q = c - a - a * (b-1)
            x1 = b-1
            x2 = b+1
        if r == 6:
            ma = a if a > 0 else -a
            p = a
            qn, qd = mf.s_fraction(((a*c - b), a))
            x1 = b-a
            x2 = b+a


        answer = (str(x1) + " и " + str(x2)) if x1 != x2 else str(x1)

    if r != 6:
        text = str(a) + "/" + mtxt._("x" + mtxt.s(-b)) + mtxt.s(c) + "=" + mtxt.fc(p) + "x" + mtxt.s(q)
    else:
        text = str(1 if a > 0 else -1) + "/" + mtxt._(str(ma) + "x" + mtxt.s(-b * ma)) + mtxt.s(c) + "=" \
               + mtxt.fc(p) + "x" + ("+" if qn * qd > 0 else "") + mtxt.f_t(qn, qd)

    return text, answer

def reshite_uravnenie():
# Решите уравнение: 2(x-1)^2=2x+2 // парабола = прямая
    t = rnd.randint(0, 2)

    if t in [0, 1]:
        a = mrnd.rnd_w(-3, 3, [0])
        m = mrnd.rnd_w(-2, 2, [0])
        k1 = a * m
        k = 2 * k1
        b = rnd.randint(1, 5) if k1 * a < 0 else rnd.randint(-5, -1)
        c = int(-2 * b * k1 - pow(k1, 2)/a)
        if t == 0:
            c += -rnd.randint(3, 8) if a>0 else rnd.randint(3, 8)
        answer = str(b + m) if t == 1 else "нет решений"

    if t == 2:
        x1 = mrnd.rnd_w(-5, 2, [0])
        x2 = mrnd.rnd_w(x1 + 1, 5, [0])
        a = mrnd.rnd_w(-3, 3, [0])
        b = mrnd.rnd_w(-3, 3, [0])
        k = a * (x1 + x2 - 2*b)
        c = a * pow(b, 2) + a * b * (b-1) * (x1 + x2) - a*x1*x2
        answer = str(x1) + " и " + str(x2)

    text = mtxt.fc(a) + mtxt._("x" + mtxt.s(-b)) + "^2=" + mtxt.fc(k) + "x" + mtxt.s(c)

    return text, answer

def najdite_naibolshee_i_naimenshee_znachenie_funktsii645():
# Найдите наибольшее и наименьшее значение функции: y = -|x - 4| на отрезке х[-2; 1] // модуль, параблоа, корень, гипербола
    t = rnd.randint(1, 4)
    s = rnd.randint(0, 1)
    shx = rnd.randint(-5, 5)
    shy = rnd.randint(-5, 5)

    x1 = rnd.randint(-6, 3)
    x2 = rnd.randint(x1 + 1, 6)

    if t == 1:
        text = ("-" if s == 1 else "") + mtxt.mod("x" + mtxt.s(shx)) + mtxt.s(shy)
        f1 = (1 if s == 0 else -1) * int(math.fabs(x1 + shx)) + shy
        f2 = (1 if s == 0 else -1) * int(math.fabs(x2 + shx)) + shy
        if (x1 < -shx) and (x2 > -shx):
            f3 = shy
        else:
            f3 = f2

    if t == 2:
        text = ("-" if s == 1 else "") + mtxt._("x" + mtxt.s(shx)) + "^2" + mtxt.s(shy)
        f1 = (1 if s == 0 else -1) * pow(x1 + shx, 2) + shy
        f2 = (1 if s == 0 else -1) * pow(x2 + shx, 2) + shy
        if (x1 < -shx) and (x2 > -shx):
            f3 = shy
        else:
            f3 = f2

    if t == 3:
        x2min = 0
        if rnd.randint(0, 1) == 0:
            x1 = -shx - rnd.randint(0, 5)
            f1 = shy
        else:
            x2min = rnd.randint(1, 3)
            x1 = pow(x2min, 2) - shx
            f1 = (1 if s == 0 else -1) * math.sqrt(x1 + shx) + shy

        x2 = pow(rnd.randint(x2min + 1, 6), 2) - shx
        text = ("-" if s == 1 else "") + mtxt.k_t("x" + mtxt.s(shx)) + mtxt.s(shy)

        f2 = (1 if s == 0 else -1) * math.sqrt(x2 + shx) + shy
        f3 = f1

    if t == 4:
        b = rnd.randint(0, 1)
        if b == 0:
            x1 = -shx - rnd.randint(1, 5)
            x2 = -shx + rnd.randint(1, 5)
            answer = "минимум: -oo; максимум: +oo"
        else:
            if rnd.randint(0, 1) == 0:
                x2 = -shx - rnd.randint(1, 3)
                x1 = x2 - rnd.randint(1, 3)
            else:
                x1 = -shx + rnd.randint(1, 3)
                x2 = x1 + rnd.randint(1, 3)
            if s == 0:
                answer = "минимум:" + mtxt.f_t((1 if s == 0 else -1), x2 + shx) + "; максимум:" + mtxt.f_t((1 if s == 0 else -1), x1 + shx)
            else:
                answer = "минимум:" + mtxt.f_t((1 if s == 0 else -1), x1 + shx) + "; максимум:" + mtxt.f_t((1 if s == 0 else -1), x2 + shx)


        text = ("-1" if s == 1 else "1") + "/" + mtxt._("x" + mtxt.s(shx)) + mtxt.s(shy)

    text += " на отрезке [" + str(x1) + "; " + str(x2) + "]"
    if t in [1, 2, 3]:
        fs = [f1, f2, f3]
        answer = "минимум:" + str(min(fs)) + "; максимум:" + str(max(fs))

    return text, answer

def zadaj_formulami_uglyi_dlya_kotoryih():
# Задай формулами углы для которых: синус|косинус равен (+-) 1/3
    c = rnd.randint(0, 1)
    s = rnd.randint(0, 1)
    n = rnd.randint(1, 3)
    d = rnd.randint(n + 1, 10)
    n, d = mf.s_fraction((n, d))

    dr = ("-" if s == 1 else "") + mtxt.f_t(n, d)

    return ("косинус" if c == 0 else "синус") + " равен " + dr, \
           (("+-arccos" + mtxt._(dr) + "+2pi*k") if c == 0 else ("(-1)^k*arcsin" + mtxt._(dr) + "+pi*k")) + ", к-целое"


def postrojte_uglyi():
# Постройте углы: (""|pi) (+-) arcsin(1/3)
    a = rnd.choice(["", "pi", "pi/2", "-pi/2"])
    s = rnd.randint(0, 1)
    c = rnd.randint(0, 1)
    n = rnd.randint(1, 3)
    d = rnd.randint(n + 1, 5)
    n, d = mf.s_fraction((n, d))

    return a + ("" if a == "" and s == 0 else mtxt.p0m1(s, False)) + ("arccos" if c == 0 else "arcsin") + mtxt._(mtxt.f_t(n, d)), \
           "график"

def vyichislite():
# Вычислите: arcsin(+-)(1: -1; 0; k(2)/2; k(3)/2; 1/2)
    c = rnd.randint(0, 1)

    vs = ["-1", "-k(3)/2", "-k(2)/2", "-1/2", "0", "1/2", "k(2)/2", "k(3)/2", "1"]
    v = rnd.choice(vs)

    def ac(c, a):
        return {
            "-1": "pi" if c == 0 else "-pi/2",
            "-k(3)/2": "5pi/6" if c == 0 else "-pi/3",
            "-k(2)/2": "3pi/4" if c == 0 else "-pi/4",
            "-1/2": "2pi/3" if c == 0 else "-pi/6",
            "0": "pi/2" if c == 0 else "0",
            "1/2": "pi/3" if c == 0 else "pi/6",
            "k(2)/2": "pi/4" if c == 0 else "pi/4",
            "k(3)/2": "pi/6" if c == 0 else "pi/3",
            "1": "0" if c == 0 else "pi/2",
        }[a]

    return ("arccos" if c == 0 else "arcsin") + mtxt._(v), ac(c, v)

def suschestvut_li():
# Существут ли: arcsin(pi/2; 1; k(5)/2; -1/2)
    c = rnd.randint(0, 1)
    vs = ["pi/4", "pi/2", "1", "3/2", "-1", "k(5)/2", "k(3)/2", "2", "0", "-pi/2", "-1/2", "180", "1/3"]
    v = rnd.choice(vs)
    return ("arccos" if c == 0 else "arcsin") + mtxt._(v), "да" if vs.index(v) % 2 == 0 else "нет"

def reshi_uravnenie640():
# Реши уравнение: (sin|cos)a = (+-)(1/2; k(2)/2;k(3)/2; )
    c = rnd.randint(0, 1)
    vs = ["-k(3)/2", "-k(2)/2", "-1/2", "1/2", "k(2)/2", "k(3)/2"]
    v = rnd.choice(vs)

    answer = \
        {
            0: {
                "-k(3)/2": "pi +-pi/6 + 2pi*n",
                "-k(2)/2": "pi +-pi/4 + 2pi*n",
                "-1/2": "pi +-pi/3 + 2pi*n",
                "1/2": "+-pi/3 + 2pi*n",
                "k(2)/2": "+-pi/4 + 2pi*n",
                "k(3)/2": "+-pi/6 + 2pi*n",
            },

            1: {
                "-k(3)/2": "-pi/2 +-pi/6 + 2pi*n",
                "-k(2)/2": "-pi/2 +-pi/4 + 2pi*n",
                "-1/2": "-pi/2 +-pi/3 + 2pi*n",
                "1/2": "pi/2 +-pi/3 + 2pi*n",
                "k(2)/2": "pi/2 +-pi/4 + 2pi*n",
                "k(3)/2": "pi/2 +-pi/6 + 2pi*n",
            }
        }[c][v]

    return ("cos" if c == 0 else "sin") + mtxt._("x") + "=" + v, \
           answer

def reshi_uravnenie639():
# Реши уравнение: (sin|cos)a = (0;1;-1)
    c = rnd.randint(0, 1)
    vs = [-1, 0, 1]
    v = rnd.choice(vs)

    answer = \
        {
            1: {
                -1: "-pi/2 + 2pi*n",
                0: "pi*n",
                1: "pi/2 + 2pi*n",
            },

            0: {
                -1: "pi + 2pi*n",
                0: "pi/2 + 2pi*n",
                1: "2pi*n",
            }
        }[c][v]

    return ("cos" if c == 0 else "sin") + mtxt._("x") + "=" + str(v), \
           answer

def chemu_raven():
# Чему равен: (sin|cos)a, если (cos|sin)a = (+-)1/3 и  pi/2<a<pi
    c = rnd.randint(0, 1)
    ch = rnd.randint(1, 4)
    vn = rnd.randint(1, 3)
    vd = rnd.randint(vn + 1, 10)
    vn, vd = mf.s_fraction((vn, vd))

    sg = "" if (c == 1 and (ch in [1, 4]) or c == 0 and (ch in [1, 2])) else "-"
    chs = "0<a<pi/2" if ch == 1 else ("pi/2<a<pi" if ch == 2 else ("pi<a<3pi/2" if ch == 3 else "3pi/2<a<2pi"))

    answer = "" if (c == 0 and (ch in [1, 4]) or c == 1 and (ch in [1, 2])) else "-"
    answer += mtxt.f_t("k(" + str(pow(vd, 2) - pow(vn, 2)) + ")", vd)

    return ("cos" if c == 0 else "sin") + mtxt._("a") + ", если " + ("cos" if c == 1 else "sin") + mtxt._("a") + "=" + \
        sg + mtxt.f_t(vn, vd) + " и " + chs, answer

def verno_li_utverzhdenie637():
# Верно ли утверждение:
#    (существует|не существует) угол a для которого (sin|cos)a = (+-)(k(3)|0|1-k(1/2));
#    (наибольшее|наименьшее) значение для sin|cos равно (0|-1|1|pi|2pi|k(2))
    t = rnd.randint(1, 2)

    if t == 1:
        sh = rnd.randint(0, 1)
        c = rnd.randint(0, 1)
        vs = ["k(3)", "0", "-1.2", "1", "1-2k(2)", "1-k(3)", "3/2", "3 - 2k(2)", "1/2 + k(2), -1 + k(2)", "-2", "k(50)/8", "k(50)/7"]
        v = rnd.choice(vs)

        text = ("" if sh == 0 else "не ") + "существует угол а, для которого " + \
               ("cos" if c == 0 else "sin") + mtxt._("a") + " равен " + v
        answer = ("да" if vs.index(v) % 2 == 1 else "нет") if sh == 0 else \
            ("нет" if vs.index(v) % 2 == 1 else "да")

    if t == 2:
        n = rnd.randint(0, 1)
        c = rnd.randint(0, 1)
        vs = ["-1", "1", "0", "-oo", "+oo"]
        v = rnd.choice(vs)
        text = ("наибольшее" if n == 0 else "наименьшее") + " значение для " + \
               ("cos" if c == 0 else "sin") + mtxt._("x") + " равно " + v
        answer = "да" if (n == 0 and vs.index(v) == 1 or n == 1 and vs.index(v) == 0) else "нет"

    return text, answer

def uprosti_vyirazhenie():
# упрости выражение: 2sin(-5pi/6) + 11cos(-7pi/3) + sin(7pi/6) - 8cos(2pi/3)
    ts = []
    text = ""
    l = 3

    for i in range(l):
        n = rnd.randint(-30, 30)
        d = 4 if rnd.randint(0, 1) == 0 else 6
        n, d = mf.s_fraction((n, d))
        k = mrnd.rnd_w(-10, 10, [0])
        c = rnd.randint(0, 1)
        ts.append((k, c, n, d))
        text += mtxt.fc(k, i == 0) + ("cos" if c == 0 else "sin") + mtxt._(mtxt.ug(n, d))

    def v(ac, an, ad):
        if an == 0:
            return (1 if ac == 0 else 0), 1, 0
        if ad == 1:
            return (-1 if ac == 0 else 0), 1, 0
        if ad == 2:
            if ac == 0:
                return (0 if an in [1, 3] else 1), 1, 0
            else:
                return (0 if an == 2 else (1 if an == 1 else -1)), 1, 0
        if ad == 3:
            if ac == 0:
                return (1, 2, 1) if an in [1, 5] else ((-1, 2, 1) if an in [2, 4] else 1)
            else:
                return (1, 2, 3) if an in [1, 5] else ((-1, 2, 3) if an in [2, 4] else 1)
        if ad == 4:
            if ac == 0:
                return (1, 2, 2) if an in [1, 7] else ((-1, 2, 2) if an in [3, 5] else 1)
            else:
                return (1, 2, 2) if an in [1, 3] else ((-1, 2, 2) if an in [5, 7] else 1)
        if ad == 6:
            if ac == 0:
                return (1, 2, 3) if an in [1, 11] else ((-1, 2, 3) if an in [5, 7] else 1)
            else:
                return (1, 2, 1) if an in [1, 5] else ((-1, 2, 1) if an in [7, 11] else 1)

    answer = ""
    m = [0, 0, 0, 0]
    for i in range(l):
        n, d = tr.reduce2r(ts[i][2], ts[i][3])
        n, d = tr.invert_a(n, d)
        c = ts[i][1]
        k = ts[i][0]

        r = v(c, n, d)
        tp = r[2]
        m[tp] += k * r[0]

    answer = ""

    # рациональная часть
    c1n, c1d = mf.s_fraction((2*m[0] + m[1], 2))
    answer += mtxt.f_t(c1n, c1d) if c1n != 0 else ""

    # k(2) часть
    c2n, c2d = mf.s_fraction((m[2], 2))
    if m[2] != 0:
        answer += ("+" if m[2] > 0 else "") if answer != "" else ""
        answer += (mtxt.f_t(c2n, c2d) if not (c2n in [-1, 1] and c2d == 1) else ("" if c2n == 1 else "-")) + "k(2)"

    # k(3) часть
    c3n, c3d = mf.s_fraction((m[3], 2))
    if m[3] != 0:
        answer += ("+" if m[3] > 0 else "") if answer != "" else ""
        answer += (mtxt.f_t(c3n, c3d) if not (c3n in [-1, 1] and c3d == 1) else ("" if c3n == 1 else "-")) + "k(3)"

    return text, answer

def opredeli_chto_bolshe():
# определи что больше: cos(13pi/4) или sin(-pi/2)
    t = rnd.randint(1, 2)

    if t == 1: # разные знаки
        v = rnd.randint(0, 1)
        if v == 0:
            t1 = "cos" + mtxt._(rnd.choice(['pi/5', 'pi/7', '-pi/6', '-pi/3', '7pi/4']))
            t2 = "sin" + mtxt._(rnd.choice(['5pi/4', '-pi/2', '7pi/6', '-4pi/5', '-pi/10']))
        else:
            t1 = "cos" + mtxt._(rnd.choice(['13pi/25', '-9pi/5', '-7pi/6', '-2pi/3', '3pi/4']))
            t2 = "sin" + mtxt._(rnd.choice(['3pi/4', '3pi/5', '6pi/7', '4pi/5', '9pi/10']))

    if t == 2: # одна и та же функция
        v = rnd.randint(0, 1)
        n = rnd.randint(3, 10)
        if v == 0:
            t1 = "cos" + mtxt._('pi/' + str(n))
            t2 = "cos" + mtxt._('pi/' + str(n + 1))
        else:
            t1 = "sin" + mtxt._('pi/' + str(n))
            t2 = "sin" + mtxt._('pi/' + str(n + 1))

    if t == 1:
        answer = t1 if v == 0 else t2
    if t == 2:
        answer = t2 if v == 0 else t1

    return t1 + " или " + t2, answer


def opredelite_znak_proizvedeniya():
# oпределите знак произведения: cos(11pi/4) * sin(-17pi/3)
    c1 = rnd.randint(0, 1)
    d1 = 4 if rnd.randint(0, 1) == 0 else 6
    n1 = rnd.randint(-30, 30)
    n1, d1 = mf.s_fraction((n1, d1))

    n12, d12 = tr.reduce2r(n1, d1)
    n12, d12 = tr.invert_a(n12, d12)
    k1 = n12 / d12


    c2 = rnd.randint(0, 1)
    d2 = 4 if rnd.randint(0, 1) == 0 else 6
    n2 = rnd.randint(-30, 30)
    n2, d2 = mf.s_fraction((n2, d2))

    n22, d22 = tr.reduce2r(n2, d2)
    n22, d22 = tr.invert_a(n22, d22)
    k2 = n22 / d22

    if ((k1 in [1/2, 3/2] and c1 == 0) or (k1 in [0, 1] and c1 == 0)) or \
        ((k2 in [1/2, 3/2] and c2 == 0) or (k2 in [0, 1] and c2 == 0)):
        answer = "0"
    else:
        s1 = 1 if ((k1 > 0 and k1 < 1/2) or (k1 > 1/2 and k1 < 1 and c1 == 1) or (k1 > 3/2 and k1 < 2 and c1 == 0)) else -1
        s2 = 1 if ((k2 > 0 and k2 < 1/2) or (k2 > 1/2 and k2 < 1 and c2 == 1) or (k2 > 3/2 and k2 < 2 and c2 == 0)) else -1
        answer = "+" if s1 == s2 else "-"

    return ("cos" if c1 == 0 else "sin") + mtxt._(mtxt.ug(n1, d1)) + "*" + \
        ("cos" if c2 == 0 else "sin") + mtxt._(mtxt.ug(n2, d2)), \
        answer


def opredeli_znak():
# определи знак: sin|cos -17pi/3
    c = rnd.randint(0, 1)
    d = 4 if rnd.randint(0, 1) == 0 else 6
    n = rnd.randint(-30, 30)
    n, d = mf.s_fraction((n, d))

    n1, d1 = tr.reduce2r(n, d)
    n1, d1 = tr.invert_a(n1, d1)

    k = n1 / d1

    if (k in [1/2, 3/2] and c == 0) or (k in [0, 1] and c == 0):
        answer = "0"
    else:
        if k >= 0 and k <= 1 / 2:
            answer = "+"
        if k >= 1 / 2 and k <= 1:
            answer = "-" if c == 0 else "+"
        if k >= 1 and k <= 3 / 2:
            answer = "-"
        if k >= 3 / 2 and k <= 2:
            answer = "+" if c == 0 else "-"

    return ("cos" if c == 0 else "sin") + mtxt._(mtxt.ug(n, d)), answer

def v_kakoj_chetverti_lezhit_ugol():
# в какой четверти лежит угол -17pi
    c = rnd.randint(0, 1)
    d = 4 if rnd.randint(0, 1) == 0 else 6
    n = rnd.randint(-30, 30)

    n, d = mf.s_fraction((n, d))

    n1, d1 = tr.reduce2r(n, d)
    n1, d1 = tr.invert_a(n1, d1)

    k = n1/d1

    if k in [0, 0.5, 1, 1.5, 2]:
        answer = "лежит на оси"
    else:
        if k > 0 and k < 1/2:
            ch = "в первой"
        if k > 1/2 and k < 1:
            ch = "во второй"
        if k > 1 and k < 3/2:
            ch = "в третьей"
        if k > 3/2 and k < 2:
            ch = "в четвертой"
        answer = "лежит " + ch + " четверти"

    return mtxt.ug(n, d), answer

def najdi631():
# найди: (sin|cos) все кратное pi/4 и pi/6 + (pi*k|2pi*k)
    c = rnd.randint(0, 1)
    d = 4 if rnd.randint(0, 1) == 0 else 6
    n = rnd.randint(-30, 30)

    n, d = mf.s_fraction((n, d))

    answer = tr.cs_table(c, n, d)

    return ("cos" if c == 0 else "sin") + mtxt._("0" if n == 0 else mtxt.f_t((str(n) if n != 1 else "") + "pi", d)), \
            answer

def narisuj_na_edinichnoj_okruzhnosti_ugol():
# нарисуй на единичной окружности угол: (+-)(pi/6|pi/4|0|pi/3) (+-) (pi|2pi|pi/2|3pi/2)
    s = rnd.randint(0, 1)
    k = rnd.randint(0, 1)
    n = rnd.randint(0, 30)

    if k == 0: #pi/4
        n1, d1 = mf.s_fraction((n, 4))
    else:
        n1, d1 = mf.s_fraction((n, 6))

    return "0" if n == 0 else (("" if s == 0 else "-") + mtxt.f_t((str(n1) if n1 != 1 else "") + "pi", d1)), 'график'

def najdi629():
# найди: sin|cos (+-)(pi/2|pi|0|-pi|-pi/2) (+-) pi*k
    c = rnd.randint(0, 1)
    s = rnd.randint(0, 1)
    n = rnd.randint(0, 10)

    n1, d1 = mf.s_fraction((n, 2))

    if s == 1:
        n = 4 - (n % 4)

    if c == 0:
        answer = "0" if n % 2 == 1 else ("1" if n % 4 == 0 else "-1")
    if c == 1:
        answer = "0" if n % 2 == 0 else ("1" if n % 4 == 1 else "-1")

    return ("cos" if c == 0 else "sin") + mtxt._("0" if n1 == 0 else (("" if s == 0 else "-") + mtxt.f_t((str(n1) if n1 != 1 else "") + "pi", d1) )), \
           answer

def verno_li_utverzhdenie628():
# Верно ли утверждение:
#    число равное ординате|абсциссе точки на единичной окружности называется синусом|косинусом угла, соответствующему данной точке;
#    точка на единичной окружности, соответствующая a имеет координаты (1|0|sin(a)|cos(a));
#    sin(a)|cos(a) = 0 для (любых a|a=pi*n|pi/2+pi*n| pi + pi/2*n|pi/2*n);

    t = rnd.randint(1, 3)

    if t == 1:
        a = rnd.randint(0, 1)
        c = rnd.randint(0, 1)
        text = "число равное " + ("абсциссе" if a == 0 else "ординате") + " точки на единичной окружности, назвается " + \
               ("косинусом" if c == 0 else "синусом") + ", угла соответствующего данной точке"
        answer = "да" if a == c else "нет"

    if t == 2:
        v = rnd.randint(0, 1)
        if v == 0:
            x = "cos(a)"
            y = "sin(a)"
        else:
            tt = rnd.randint(1, 5)
            if tt == 1:
                x = 0
                y = 0
            if tt == 2:
                x = 1
                y = 1
            if tt == 3:
                x = 0
                y = 1
            if tt == 4:
                x = "sin(a)"
                y = "cos(a)"
            if tt == 5:
                x = "-cos(a)"
                y = "sin(a)"
        text = "точка на единичной окружности, соответствующая углу a имеет координаты " + mtxt.point(x, y)
        answer = "да" if v == 0 else "нет"

    if t == 3:
        c = rnd.randint(0, 1)
        tt = rnd.randint(1, 3)
        text = ("cos(a)" if c == 0 else "sin(a)") + "=0 " + ("для любых a" if tt == 1 else ("при a=pi*n" if tt == 2 else("при a=pi/2+pi*n" if tt == 3 else ("при a=pi+pi/2*n" if tt == 4 else "при a=pi/2*n"))))
        answer = "да" if ((c==0 and tt==3) or (c==1 and tt==2)) else "нет"

    return text, answer

def najdi627():
# найди: (sin|cos) (0; -30 градусов; pi/4 и тд) // все кратное pi/4 и pi/6
    f = rnd.randint(0, 1)
    s = rnd.randint(0, 1)
    k = rnd.randint(0, 1)
    if k == 0:
        n = rnd.randint(0, 8)
        if s == 1:
            n = 8 - n
    else:
        n = rnd.randint(0, 12)
        if s == 1:
            n = 12 - n

    if f == 0:
        if k == 0:
            if n in [2, 6]:
                answer = "0"
            if n in [0, 8]:
                answer = "1"
            if n == 4:
                answer = "-1"
            if n in [1, 7]:
                answer = "k(2)/2"
            if n in [3, 5]:
                answer = "-k(2)/2"
        else:
            if n in [3, 9]:
                answer = "0"
            if n in [0, 12]:
                answer = "1"
            if n == 6:
                answer = "-1"
            if n in [1, 11]:
                answer = "k(3)/2"
            if n in [2, 10]:
                answer = "1/2"
            if n in [4, 8]:
                answer = "-1/2"
            if n in [5, 7]:
                answer = "-k(3)/2"

    if f == 1:
        if k == 0:
            if n in [0, 4, 8]:
                answer = "0"
            if n == 2:
                answer = "1"
            if n == 6:
                answer = "-1"
            if n in [1, 3]:
                answer = "k(2)/2"
            if n in [5, 7]:
                answer = "-k(2)/2"
        else:
            if n in [0, 6, 12]:
                answer = "0"
            if n == 3:
                answer = "1"
            if n == 9:
                answer = "-1"
            if n in [2, 4]:
                answer = "k(3)/2"
            if n in [1, 5]:
                answer = "1/2"
            if n in [7, 11]:
                answer = "-1/2"
            if n in [8, 10]:
                answer = "-k(3)/2"

    return ("cos" if f == 0 else "sin") + " угла в " + ("" if (s == 0) or (n == 0) else "-") + str((45 if k == 0 else 30) * n) + " градусов", \
           answer

def najdi626():
# найди: (sin|cos) (0; 270 градусов; -pi/2 и тд) // все кратное pi/2
    f = rnd.randint(0, 1)
    n = rnd.randint(0, 4)
    s = rnd.randint(0, 1)

    if s == 1:
        n = 4 - n

    if f == 0:
        if n in [1, 3]:
            answer = "0"
        if n in [0, 4]:
            answer = "1"
        if n == 2:
            answer = "-1"
    if f == 1:
        if n in [0, 2, 4]:
            answer = "0"
        if n == 1:
            answer = "1"
        if n == 3:
            answer = "-1"

    return ("cos" if f == 0 else "sin") + " угла в " + ("" if (s == 0) or (n == 0) else "-") + str(90 * n) + " градусов", \
           answer


def opredeli_znaki_sina_i_cosa_esli_tochka_sootvetstvuyuschaya_uglu_a_lezhit_v():
# определи знаки sin(a) и cos(a), если точка соответствующая углу a лежит в: I четверти
    ch = rnd.randint(1, 4)
    return str(ch) + " четверти" , "sin(a) " + (">" if ch in [1, 2] else "<") + " 0; cos(a) " + (">" if ch in [1, 4] else "<") + " 0;"


def kakie_iz_chisel_yavlyayutsya_otritstalnyimi_polozhitelnyimi_neotritsatelnyimi_i_nepolozhitelnyimi():
# Какие из чисел являются отрицтальными, положительными, неотрицательными и неположительными: 3; -6; -2и1/3; 4,7; 9/16; 0; -5,2; 10,14; 5/8
    res = []
    for mn in mrnd.mns:
        c = rnd.randint(1, 4)
        for i in range(c):
            res.append(mrnd.get_ch_mn(mn))
    rnd.shuffle(res)

    return " ".join([x[0] for x in res]), \
        "положительные: " + " ".join([x[0] for x in res if 'положительные' in x[1]]) + "; " + \
        "отрицательные: " + " ".join([x[0] for x in res if 'отрицательные' in x[1]]) + "; " + \
        "неположительные: " + " ".join([x[0] for x in res if 'неположительные' in x[1]]) + "; " + \
        "неотрицательные: " + " ".join([x[0] for x in res if 'неотрицательные' in x[1]]) + "; "


def kakie_iz_chisel_nepolozhitelnyie():
# какие из чисел неположительные: -1; 10; 4/3; -5/9; -1,0; 0; 3
    res = []
    for mn in mrnd.mns:
        c = rnd.randint(1, 4)
        for i in range(c):
            res.append(mrnd.get_ch_mn(mn))
    rnd.shuffle(res)

    return " ".join([x[0] for x in res]), " ".join([x[0] for x in res if 'неположительные' in x[1]])


def kakie_iz_chisel_neotritstalnyie():
# какие из чисел неотрицтальные: -1; 10; 4/3; -5/9; -1,0; 0; 3
    res = []
    for mn in mrnd.mns:
        c = rnd.randint(1, 4)
        for i in range(c):
            res.append(mrnd.get_ch_mn(mn))
    rnd.shuffle(res)

    return " ".join([x[0] for x in res]), " ".join([x[0] for x in res if 'неотрицательные' in x[1]])



def kakie_iz_chisel_polozhitelnyie():
# какие из чисел положительные: -1; 10; 4/3; -5/9; -1,0; 0; 3
    res = []
    for mn in mrnd.mns:
        c = rnd.randint(1, 4)
        for i in range(c):
            res.append(mrnd.get_ch_mn(mn))
    rnd.shuffle(res)

    return " ".join([x[0] for x in res]), " ".join([x[0] for x in res if 'положительные' in x[1]])


def kakie_iz_chisel_otritsatelnyie():
# какие из чисел отрицтальные: -1; 10; 4/3; -5/9; -1,0; 0; 3
    res = []
    for mn in mrnd.mns:
        c = rnd.randint(1, 4)
        for i in range(c):
            res.append(mrnd.get_ch_mn(mn))
    rnd.shuffle(res)

    return " ".join([x[0] for x in res]), " ".join([x[0] for x in res if 'отрицательные' in x[1]])

def vyichislite_ploschad_secheniya_shara_ploskostyu_prohodyaschej_cherez_tsentr_shara_esli_radius_shara_raven():
# Вычислите площадь сечения шара плоскостью, проходящей через центр шара, если радиус шара равен: 3 см
    r = rnd.randint(1, 7)
    return str(r) + " см", "{0:.2f}".format(3.14 * pow(r, 2)) + " см^2"

def najdite_ploschad_bokovoj_grani_tsilindra_esli():
# Найдите площадь боковой грани цилиндра, если: длина образующей равна 6 см, а радиус основания 3 см
    r = rnd.randint(1, 5)
    h = rnd.randint(2, 6)
    return "длина обращзующей равна " + str(h) + " см, а радиус основания " + str(r) + " см" , "{0:.2f}".format(2 * 3.14 * r * h) + " см^2"

def najdite_ploschad_pryamougolnika_esli_odna_ego_storona_ravna():
# найдите площадь прямоугольника, если одна его сторона равна: 3 см, а другая 4,2 см
    a = rnd.randint(2, 8)
    b = rnd.randint(30, 100) / 10
    return str(a) + " см, а другая " + str(b) + " см", str(a * b) + " см^2"

def kak_izmenitsya_radius_okruzhnosti_esli_dlinu_etoj_okruzhnosti_uvelichit_na():
# Как измениться радиус окружности, если длину этой окружности увеличить на: 9.42 см?
    dr = rnd.randint(1, 7)
    return "{0:.2f}".format(2 * 3.14 * dr) + " см", "увеличиться на " + str(dr) + " см"

def vyirazi_raznitsu_radiusov_okruzhnostej_esli_dlina_odnoj_okruzhnosti():
# вырази разницу радиусов окружностей, если длина ожной окружности 18,84 см, а другой 12,56 см
    r1 = rnd.randint(1, 6)
    r2 = rnd.randint(r1 + 1, 10)
    return "{0:.2f}".format(2 * 3.14 * r1) + " см, а другой " + "{0:.2f}".format(2 * 3.14 * r2) + " см", str(r2 - r1)  + " см"

def radius_okruzhnosti_uvelichili_na():
# Радиус окружности увеличили на: 1 см, на сколько увеличилась длина окружности?
    dr = rnd.randint(1, 5)
    return str(dr) + " см, на сколько увеличилась длина окружности?" , "{0:.2f}".format(2 * 3.14 * dr) + " см"

def vyirazi_raznitsu_dlin_okruzhnostej_cherez_pi_esli_radius_odnoj_okruzhnosti():
# вырази разницу длин окружностей через pi, если радиус одной окружности: 2 см, а другой 3 см
    r1 = rnd.randint(1, 6)
    r2 = rnd.randint(r1 + 1, 10)

    return str(r1) + " см, а другой " + str(r2) + " см", str(2 * (r2 - r1)) + "*pi"

def vyichislite_radius_okruzhnosti_esli_ploschad_etoj_okruzhnosti_ravna():
# Вычислите радиус окружности, если площадь этой окружности равна: 314 см^2
    r = rnd.randint(1, 10)
    return "{0:.2f}".format(3.14 * pow(r, 2)) + " см^2", str(r) + " см"

def vyichislite_ploschad_okruzhnosti_esli_ee_radius_raven():
# Вычислите площадь окружности, если ее радиус равен: 3 см
    r = rnd.randint(1, 7)
    return str(r) + " см" , "{0:.2f}".format(3.14 * pow(r, 2)) + " см^2"

def vyichislite_radius_okruzhnosti_esli_dlina_etoj_okruzhnosti_ravna():
# Вычислите радиус окружности, если длина этой окружности равна: 18,84 см
    pi = 3.14
    r = rnd.randint(1, 7)
    return "{0:.2f}".format(2 * 3.14 * r) + " см", str(r) + " см"

def ispolzuya_grafiki_funktsij609():
# Используя графики функций: y=2/x и y = -x + 2 решите неравенство: 2/x <= -x+2

    lr = rnd.randint(0, 1)

    t = rnd.randint(0, 2)

    if t == 0:
        k = mrnd.rnd_w(-5, 5, [0])
        a = rnd.randint(-10, -1) if k > 0 else rnd.randint(1, 10)
        b = 0

        answer = "(-oo; 0)" if (k < 0 and lr == 0 or k > 0 and lr == 1) else "(0; +oo)"

    if t == 1:
        a = mrnd.rnd_w(-5, 5, [0])
        k = -a
        b = int(math.sqrt(-4 * a * k))
        x1 = int(-b / 2 / a)
        answer = "(-oo; 0)" if (k < 0 and lr == 0 or k > 0 and lr == 1) else "(0; +oo)"

    if t == 2:
        x1 = mrnd.rnd_w(-5, 3, [0])
        x2 = mrnd.rnd_w(x1 + 1, 5, [0])

        a, b, k = mf.quad_pol_by_roots((x1, 1), (x2, 1))
        k = -k

        if x2 < 0:
            x3 = 0
        if x2 > 0 and x1 < 0:
            x3 = x2
            x2 = 0
        if x1 > 0:
            x3 = x2
            x2 = x1
            x1 = 0

        def get_sk(ts, x):
            if ts == 0:
                if x == 0:
                    return "("
                else:
                    return "["
            else:
                if x == 0:
                    return ")"
                else:
                    return "]"

        answer = (get_sk(0, x1) + str(x1) + "; " + str(x2) + get_sk(1, x2) + " U " + get_sk(0, x3) + str(x3) + "; +oo)") if ((lr == 1 and a > 0) or (lr == 0 and a < 0)) else \
            ("(-oo; " + str(x1) + get_sk(1, x1) + " U " + get_sk(0, x2) + str(x2) + "; " + str(x3) + get_sk(1, x3))


    return "y=" + str(k) + "/x и y=" + mtxt.fc(a) + "x" + mtxt.s(b) + " решите неравенство " + str(k) + "/x " + (">=" if lr == 0 else "<=") + " " + mtxt.fc(a) + "x" + mtxt.s(b), \
            answer

def reshi_graficheski_uravnenie608():
# Реши графически уравнение: 2/x = -x/2 // пересечение линейной и обратной функции
    t = rnd.randint(1, 3)

    if t == 1:
        k = mrnd.rnd_w(-5, 5, [0])
        a = rnd.randint(-10, -1) if k > 0 else rnd.randint(1, 10)
        b = 0
        answer = "нет решений"

    if t == 2:
        a = mrnd.rnd_w(-5, 5, [0])
        k = -a
        b = int(math.sqrt(-4*a*k))
        x1 = int(-b/2/a)
        answer = str(x1)

    if t == 3:
        x1 = mrnd.rnd_w(-5, 5, [0])
        x2 = mrnd.rnd_w(-5, 5, [0, x1])

        a, b, k = mf.quad_pol_by_roots((x1, 1), (x2, 1))
        k = -k
        answer = str(x1) + " и " + str(x2)

    return str(k) + "/x = " + mtxt.fc(a) + "x" + mtxt.s(b), answer

def najdite_naibolshee_i_naimenshee_znachenie_funktsii():
# Найдите наибольшее и наименьшее значение функции: y = -2/x на отрезке [-2; -1] //Возможно нужно рассмаотреть случай с перекрытием нуля
    k = mrnd.rnd_w(-3, 3, [0])
    x1 = mrnd.rnd_w(-7, 5, [0])
    x2 = mrnd.rnd_w(x1 + 1, 7, [0])

    if x1 * x2 > 0:
        n1, d1 = mf.s_fraction((k, x1))
        n2, d2 = mf.s_fraction((k, x2))

        if k > 0:
            vmin = mtxt.f_t(n2, d2)
            vmax = mtxt.f_t(n1, d1)
        else:
            vmin = mtxt.f_t(n1, d1)
            vmax = mtxt.f_t(n2, d2)

        answer = "min = " + vmin + ", max = " + vmax
    else:
        answer = "min = -oo, max = +oo"

    return "y = " + str(k) + "/x на отрезке [" + str(x1) + "; " + str(x2) + "]", \
           answer

def kakomu_promezhutku_prinadlezhit_x_esli():
# Какому промежутку принадлежит x, если: y принадлежить промежутку [-1/2; 2] для функции y = 1/x
    k = mrnd.rnd_w(-5, 5, [0])

    x1n = mrnd.rnd_w(-3, 3, [0])
    x1d = rnd.choice([5, 7, 11])

    x2n = rnd.randint(1, 3)
    x2d = 1

    if k > 0:
        n, d = mf.s_fraction((k, x2n))
        n1, d1 = mf.s_fraction((k * x1d, x1n))
        if x1n > 0:
            answer = "[" + mtxt.f_t(n, d)  + "; "  + mtxt.f_t(n1, d1) + "]"
        else:
            answer = "[" + mtxt.f_t(n1, d1) + "; 0) U (0; " + mtxt.f_t(n, d) + "]"
    else:
        n, d = mf.s_fraction((k, x2n))
        n1, d1 = mf.s_fraction((k * x1d, x1n))
        if x1n > 0:
            answer = "[" + mtxt.f_t(n1, d1)  + "; "  + mtxt.f_t(n, d) + "]"
        else:
            answer = "[" + mtxt.f_t(n, d) + "; 0) U (0; " + mtxt.f_t(n1, d1) + "]"

    return "y принадлежит промежутку [" + mtxt.f_t(x1n, x1d) + "; " + str(x2n) + "] для функции y=" + str(k) + "/x", \
           answer

def v_kakih_chetveryath_raspolozhen_grafik_funktsii():
# В каких четверятх расположен график функции: y = 3/x
    k = mrnd.rnd_w(-7, 7, [-1, 0, 1])
    return "y=" + str(k) + "/x", "I и III" if k > 0 else "II и IV"

def postroj_grafik_funktsii604():
# построй график функции: y = (+|-)3/x
    k = mrnd.rnd_w(-7, 7, [-1, 0, 1])
    return "y=" + str(k) + "/x", "график"

def chemu_ravno603():
# чему равно: -3/x, если x = 0 | +oo | -oo
    k = mrnd.rnd_w(-7, 7, [-1, 0, 1])
    t = rnd.randint(1, 4)
    if t == 1:
        s = "положительное и почти 0"
        answer = ("+" if k > 0 else "-") + "oo"
    if t == 2:
        s = "отрицательное и почти 0"
        answer = ("-" if k > 0 else "+") + "oo"
    if t == 3:
        s = "+oo"
        answer = ("положительное" if k > 0 else "отрицательное") + " и почти 0"
    if t == 4:
        s = "-oo"
        answer = ("отрицательное" if k > 0 else "положительное") + " и почти 0"

    return str(k) + "/x, если x = " + s, answer

def chemu_ravno602():
# чему равно: -3/x, если x = (+|-) 3 | 1/3
    k = mrnd.rnd_w(-7, 7, [-1, 0, 1])
    obr = rnd.choice([True, False])
    x = k if k > 0 else -k
    s = rnd.randint(0, 1)
    return str(k) + "/x, если x = " + (str(x * (1 if s == 0 else -1)) if not obr else (("" if s == 0 else "-") + ("1/" + str(x))) ) , \
           str((x * x * (1 if (k * (1 if s == 0 else -1) > 0) else -1 )) if obr else ((1 if (k * (1 if s == 0 else -1) > 0) else -1) ))

def postrojte_grafik_funktsii601():
# Постройте график функции: y = (2x^3 + 2x^2)/(x+1)
    x1 = mrnd.rnd_w(-7, 7, [0])
    k = mrnd.rnd_w(-3, 3, [0])
    s = rnd.randint(0, 1)
    return mtxt._(mtxt.fc(k) + "x^3" + mtxt.fc(k * x1, is_first=False) + "x^2") + "/" + mtxt._("x" + mtxt.s(x1)), \
           "график"

def uprostite_vyirazhenie600():
# упростите выражение: (2x^3 + 2x^2)/(x+1), при условии, что x не равен -1
    x1 = mrnd.rnd_w(-7, 7, [0])
    k = mrnd.rnd_w(-3, 3, [0])
    s = rnd.randint(0, 1)
    return mtxt._(mtxt.fc(k) + "x^3" + mtxt.fc(k * x1, is_first=False) + "x^2") + "/" + mtxt._("x" + mtxt.s(x1)) + " при условии, что x не равен " + str(-x1), \
           mtxt.fc(k) + "x^2, если x не равен " + str(-x1)

def skolko_reshenij_imeet_uravnenij_fxravnop_v_zavisimosti_ot_p_esli():
# Сколько решений имеет уравнений f(x)=p в зависимости от p, если: f(x) = {x + 3, если -4<=x<=-1; 2x^2, если -1<x<=1; -x + 3, если 1<x<=3}
    n = mrnd.rnd_w(-2, 2, [0])
    xp1 = mrnd.rnd_w(-4, 2, [0])
    xp2 = mrnd.rnd_w(xp1 + 1, 4, [0])
    k1 = mrnd.rnd_w(-2, 2)
    k2 = mrnd.rnd_w(-2, 2, [k1])

    b1 = n * pow(xp1, 2) - k1 * xp1
    b2 = n * pow(xp2, 2) - k2 * xp2

    x1 = rnd.randint(xp1 - 5, xp1 - 2)
    x2 = rnd.randint(xp2 + 2, xp2 + 5)

    # n = 2
    # xp1 = -1
    # xp2 = 1
    # k1 = 2
    # k2 = 0
    # b1 = 4
    # b2 = 2
    # x1 = -4
    # x2 = 3

    ys = [k1 * x1 + b1]
    if k1 != 0:
        ys.append(k1 * xp1 + b1)
    if xp1 < 0 and xp2 > 0:
        ys.append(0)
    ys.append(k2 * xp2 + b2)
    if k2 != 0:
        ys.append(k2 * x2 + b2)
    ysz = zip(ys, ys[1:], ys[2:])

    ysr = [ys[0]]
    for y1, y2, y3 in ysz:
        if (y1 < y2 and y2 > y3) or (y1 > y2) and (y2 < y3):
            ysr.append(y2)
    ysr.append(ys[len(ys) - 1])

    ysr_sorted = sorted(ysr)
    ysr_sorted_z = zip(ysr_sorted, ysr_sorted[1:])

    res = []

    for y1z, y2z in ysr_sorted_z:
        c = 0
        ysr_z = zip(ysr, ysr[1:])
        for y1, y2 in ysr_z:
            c += 1 if ((y1 <= y1z and y2 >= y2z) or (y2 <= y1z and y1 >= y2z)) else 0
        res.append((y1z, y2z, c))

    answer = ""
    for i, r in enumerate(res):
        answer += str(r[2]) + " при " + str(r[0]) + ("<=" if (i == 0 and k1 != 0) else "<") + "p" + ("<=" if (i == len(res) - 1) and k2 != 0 else "<") + str(r[1]) + "; "
        if i > 0 and i < len(res) - 1:
            answer += str(r[2] - 1) + " при p=" + str(r[0]) + "; "

    if k1 == 0:
        answer += "бесконеч. решений при p=" + str(b1)
    if k2 == 0:
        answer += "бесконеч. решений при p=" + str(b2)


    return "f(x) = {" + ((mtxt.fc(k1) + "x") if k1 != 0 else "") + mtxt.s(b1) + ", если " + str(x1) + " <= x <= " + str(xp1) + "; " + \
           mtxt.fc(n) + "x^2, если " + str(xp1) + " < x <= " + str(xp2) + "; " + ((mtxt.fc(k2) + "x") if k2 != 0 else "") + mtxt.s(b2) + ", если " + \
           str(xp2) + " < x <= " + str(x2) + "}", "ответ не правильный: " + answer

def postrojte_grafik_funktsii598():
# постройте график функции: f(x) = {x + 3, если -4<=x<=-1; 2x^2, если -1<x<=1; -x + 3, если 1<x<=3}
    n = mrnd.rnd_w(-3, 3, [0])
    xp1 = mrnd.rnd_w(-4, 2, [0])
    xp2 = mrnd.rnd_w(xp1 + 1, 4, [0])
    k1 = mrnd.rnd_w(-4, 4)
    k2 = mrnd.rnd_w(-4, 4, [k1])

    b1 = n * pow(xp1, 2) - k1 * xp1
    b2 = n * pow(xp2, 2) - k2 * xp2

    x1 = rnd.randint(xp1 - 5, xp1 - 2)
    x2 = rnd.randint(xp2 + 2, xp2 + 5)


    return "f(x) = {" + ((mtxt.fc(k1) + "x") if k1 != 0 else "") + mtxt.s(b1) + ", если " + str(x1) + " <= x <= " + str(xp1) + "; " + \
           mtxt.fc(n) + "x^2, если " + str(xp1) + " < x <= " + str(xp2) + "; " + ((mtxt.fc(k2) + "x") if k2 != 0 else "") + mtxt.s(b2) + ", если " + \
           str(xp2) + " < x <= " + str(x2) + "}", 'график'

def postrojte_grafik_funktsii597():
# постройте график функции: f(x) = {x + 3, если -2<=x<=-1; 2x^2, если -1<x<=2}
    n = mrnd.rnd_w(-3, 3, [0])
    xp = mrnd.rnd_w(-3, 3, [0])
    k = mrnd.rnd_w(-6, 6)

    b = n * pow(xp, 2) - k * xp

    x1 = rnd.randint(xp - 5, xp - 2)
    x2 = rnd.randint(xp + 2, xp + 5)

    return "f(x) = {" + ((mtxt.fc(k) + "x") if k != 0 else "") + mtxt.s(b) + ", если " + str(x1) + " <= x <= " + str(xp) + "; " +\
        mtxt.fc(n) + "x^2, если " + str(xp) + " < x <= " + str(x2) + "}", 'график'

def pust():
# Пусть: f(x)=x^2 + 6x - 1, постройте график функции: f(x) = 0,3f(x-3) + 3 // преобразуется к f(x)=ax^2
    kn = 1
    kd = rnd.choice([2, 3, 4, 5])

    a = mrnd.rnd_w(-5, 5, [0])
    b = 2 * a * mrnd.rnd_w(-2, 2, [0])
    c = mrnd.rnd_w(-5, 5, [0])

    d = int(-b/(2 * a))
    mn = -kn * (a * pow(d, 2) + b * d + c)
    md = kd

    # TODO: проверить результат руками!!!!!

    return "f(x) = " + mtxt.fc(a) + "x^2" + mtxt.fc(b, is_first=False) + "x" + mtxt.s(c) + ", постройте график функции: " + \
        "f(x) = " + mtxt.f_t(kn, kd) + "f(x" + mtxt.s(d) + ")" + ("" if mn < 0 else "+") + mtxt.f_t(mn, md), \
           "график функции y=" + mtxt.f_t(a * kn, kd) + "x^2"

def uprostite_vyirazhenie595():
# упростите выражение: x^2 + 6x - 1, заменив x на x-3
    a = mrnd.rnd_w(-5, 5, [0])
    b = mrnd.rnd_w(-5, 5, [0])
    c = mrnd.rnd_w(-5, 5, [0])
    d = mrnd.rnd_w(-5, 5, [0])
    return mtxt.fc(a) + "x^2" + mtxt.fc(b, is_first=False) + "x" + mtxt.s(c) + ", заменив x на x" + mtxt.s(d), \
           mtxt.fc(a) + "x^2" + mtxt.fc(2 * a * d + b, is_first=False) + "x" + mtxt.s(b * d + c)

def uprostite_vyirazhenie594():
# упростите выражение: a^2 + 6a - 1, если a=x-3
    a = mrnd.rnd_w(-5, 5, [0])
    b = mrnd.rnd_w(-5, 5, [0])
    c = mrnd.rnd_w(-5, 5, [0])
    d = mrnd.rnd_w(-5, 5, [0])
    return mtxt.fc(a) + "a^2" + mtxt.fc(b, is_first=False) + "a" + mtxt.s(c) + ", если a=x" + mtxt.s(d), \
           mtxt.fc(a) + "x^2" + mtxt.fc(2 * a * d + b, is_first=False) + "x" + mtxt.s(b * d + c)

def uprostite_vyirazhenie():
# упростите выражение: 2a + 3, если a=x-3
    a = mrnd.rnd_w(-5, 5, [0])
    b = mrnd.rnd_w(-5, 5, [0])
    c = mrnd.rnd_w(-5, 5, [0])
    return mtxt.fc(a) + "a" + mtxt.s(b) + ", если a=x" + mtxt.s(c) , mtxt.fc(a) + "x" + mtxt.s(a * c + b)


def skolko_polnyih_oborotov_i_v_kakuyu_storonu_soderzhitsya_v_ugle():
# Сколько полных оборотов и в какую сторону содержится в угле: - 13 и 1/2 pi радиан
    s = rnd.choice([-1, 1])
    n = rnd.randint(1, 16)
    n1 = rnd.choice([1, 2, 3, 5, 6, 7])
    nn, dd = mf.s_fraction((n1, 4))
    return str(s * n) + " и " +  mtxt.f_t(nn, dd) + " pi радиан", str(n // 2) + " " + ("по" if s == 1 else "против") + \
        " часовой стрелке"

def skolko_oborotov_soderzhitsya_v_ugle():
# сколько оборотов содержится в угле: 4pi радиан
    n = rnd.randint(1, 16)
    return str(n) + " pi радиан", str(n // 2)

def kakoj_ugol_bolshe():
# Какой угол больше: 60 градусов или pi/3 радиан
    n1 = rnd.randint(1, 11)
    n2 = rnd.randint(1, 7)

    nn, dd = mf.s_fraction((n2, 4))
    s1 = str(n1 * 30) + " градусов"
    s2 = mtxt.f_t(nn, dd) + " pi радиан"
    m = [s1, s2]
#    rnd.shuffle(m)
    return " или ".join(m), "равны" if 8 * n1 == 12 * n2 else (s2 if (n2 * 57.3 * 3.14 / 4) > (n1 * 30) else s1)

def vyirazite_v_gradusah_ugol():
# Выразите в градусах угол: - pi/2 радиан
    s = rnd.choice([-1, 1])
    n = rnd.randint(1, 4)
    n1, d1 = mf.s_fraction((s * n, 4))
    return mtxt.f_t(n1, d1) + " pi радиан", str(s * n * 45) + " градусов"

def vyirazite_v_radianah_ugol():
# Выразите в радианах угол: -135 градусов
    n = rnd.randint(1, 4)
    s = rnd.choice([-1, 1])
    n1, d1 = mf.s_fraction((s * n, 4))
    return str(45 * n * s) + " градусов", mtxt.f_t(n1, d1) + " pi радиан"

def kakuyu_chast_ot_razvernutogo_ugla_sostavlyaet_ugol_v():
# какую часть от развернутого угла, составчлет угол в: 135 градусов
    n = rnd.randint(1, 4)
    n1, d1 = mf.s_fraction((n, 4))
    return str(45 * n) + " градусов", mtxt.f_t(n1, d1)

def vyiberite_vernoe_utverzhdenie():
# выберите верное утверждение:
#    1 радиан (примерно равен (57|114|29) | немного больше 114 | немного меньше 29) градусов
#    (1|2) радиан это угол, которые получается если по окружности с радиусом (1|2)R пройти путь длиной в R;
#    развернутый угол это (2|1/2|1)pi радиан;
#   полный оборот это (1|2|1/2)pi радиан

    text = ""
    answer = ""

    t = rnd.randint(1, 4)
    if t == 1:
        tt = rnd.randint(1, 3)
        v = rnd.randint(0, 1)
        if v == 0:
            text = "1 радиан примерно равен 57 градусам"
            answer = "верно"
        else:
            text = "1 радиан " + ("примерно равен " + ("114" if rnd.choice([True, False]) else "29") if tt == 1 \
                                      else ("немного больше 114" if tt == 2 else "немного меньше 29")) + " градусов"
            answer = "не верно"
    if t == 2:
        o = rnd.randint(1, 2)
        n = rnd.choice([1, 2, 3])
        text = ("1 радиан" if o == 1 else "2 радиана") + " это угол, который получается если по окружности радиусом R пройти путь длиной в " + \
               ("" if n == 1 else ("2" if n == 2 else "1/2")) + " R"
        answer = "верно" if o == n else "не верно"
    if t == 3:
        u = rnd.choice([1, 2, 3])
        text = "развернутый угол - это " + ("" if u == 1 else ("2" if u == 2 else "1/2")) + " pi радиан"
        answer = "верно" if u == 1 else "не верно"
    if t == 4:
        u = rnd.choice([1, 2, 3])
        text = "полный оборот - это " + ("" if u == 1 else ("2" if u == 2 else "1/2")) + " pi радиан"
        answer = "верно" if u == 2 else "не верно"

    return text, answer

def vyichislite_dlinu_okruzhnosti_esli_ee_radius_raven():
# Вычислите длину окружности, если ее радиус равен: 3 см
    r = rnd.randint(1, 12)
    return str(r) + " см", "{0:.2f}".format(2 * 3.14 * r) + " см"

def pri_kakih_znacheniyah_a_tochka():
# При каких значениях a точка: (a; 64) принадлежит графику функции y = 2x^(2|3)
    k = mrnd.rnd_w(-4, 4, [0])
    p = rnd.choice([2, 3])
    x = mrnd.rnd_w(-4, 4, [0])
    y = k * pow(x, p)

    answer = ""
    if p == 2:
        if rnd.randint(0, 1) == 0:
            answer = str(x) + " и " + str(-x)
        else:
            answer = "не при каких"
            y = -y
    else:
        answer = str(x)

    return mtxt.point("a", y) + " принадлежит графику функции y=" + mtxt.fc(k) + "x^" + str(
        p), answer


def prinadlezhit_li_tochka():
# принадлежит ли точка: (2; 8) графику функции y = 2x^(2|3)
    k = mrnd.rnd_w(-4, 4, [0])
    p = rnd.choice([2, 3])
    pr = rnd.randint(0, 1)
    x = mrnd.rnd_w(-4, 4, [0])
    y = k * pow(x, p) if pr == 0 else k * pow(x, p) + mrnd.rnd_w(-10, 10, [0])
    return mtxt.point(x, y) + " графику функции y=" + mtxt.fc(k) + "x^" + str(p), "принадлежит" if pr == 0 else "не принадлжеит"


def kakomu_uglu_sootvetstvuet582():
# Какому углу соответствует: 1 и 3/4 оборота (в обратную сторону)
    obr = rnd.randint(0, 1)
    n = rnd.randint(1, 7)
    n1, d1 = mf.s_fraction((n, 8))
    m = rnd.randint(1, 3)
    return str(m) + " и " + mtxt.f_t(n1, d1) + " оборота" + ("" if obr == 1 else " в обратную сторону"), \
           ("" if obr == 1 else "-") + str((m * 8 + n)*45) + " градусов"

def kakomu_uglu_sootvetstvuet():
# какому углу соответствует: 3/4 оборота // крато 1/8 оборота
    n = rnd.randint(1, 7)
    n1, d1 = mf.s_fraction((n, 8))
    return mtxt.f_t(n1, d1) + " оборота", str(45 * n)

def kakomu_uglu_sootvetsvutet():
# какому углу соответсвутет: 2 оборота // целое число оборотов
    n = rnd.randint(1, 4)
    return str(n) + " оборота", str(n * 360) + " градусов"

def otobrazi_na_koordinatnoj_ploskosti_ugol():
# Отобрази на координатной плоскости угол: -270 град.
    s = rnd.randint(0, 1)
    n = rnd.randint(1, 7)
    return str((1 if s == 0 else -1) * n * 45) + " градусов", "рисунок"

def vyirazi_obyiknovennoj_drobyu_chislo_oborotov_sootvetstvuyuschee_uglu():
# Вырази обыкновенной дробью число оборотов, соответствующее углу: (+|-)450 град.
    s = rnd.randint(0, 1)
    n = rnd.randint(1, 7)
    m = rnd.randint(0, 2)

    n1, d1 = mf.s_fraction((m * 8 + n, 8))

    return str((1 if s == 0 else -1) * (m * 360 + n * 45)) + " градусов", ("" if s == 0 else "-") + mtxt.f_t(n1, d1)

def v_kakuyu_storonu_nuzhno_delat_oborotyi_protiv_chasovoj_ili_po_chasovoj_strelke_chtobyi_sootvetstvovat_uglu():
# в какую сторону нужно делать обороты (против часовой или по часовой стрелке), чтобы соответствовать углу: 720 град
    s = rnd.randint(0, 1)
    n = rnd.randint(1, 7)
    return str((1 if s == 0 else -1) * n * 45) + " градусов", "по часовой" if s == 0 else "против часовой"

def kakaya_chast_oborota_sootvetstvuet_uglu():
# какая часть оборота соответствует углу: 270 град // кратно 1/8 полного оборота
    n = rnd.randint(1, 7)
    m, d = mf.s_fraction((n, 8))
    return str(int(45 * n)) + " градусов", mtxt.f_t(m, d)

def skolko_oborotov_sootvetstvuet_uglu():
# сколько оборотов соответсвуте углу: 720 град // 360*n
    n = rnd.randint(1, 6)
    return str(n * 360) + " градусов", str(n)

def ispolzuya_grafiki_funktsij():
# Используя графики функций: y=-x^2 и y=2x-3, реши неравенство: -x^2 >= 2x-3
    v = rnd.randint(0, 1)

    x1 = (mrnd.rnd_w(-4, 4, [0]), mrnd.rnd_w(-5, 5, [0]))
    x2 = (mrnd.rnd_w(-4, 4, [0, x1[0]]), mrnd.rnd_w(-5, 5, [0, x1[0]]))

    if x1[0] / x1[1] > x2[0] / x2[1]:
        t = x1
        x1 = x2
        x2 = t

    a, b, c = mf.quad_pol_by_roots(x1, x2)

    x1n, x1d = mf.s_fraction((x1[0], x1[1]))
    x2n, x2d = mf.s_fraction((x2[0], x2[1]))

    if (v == 0 and a > 0) or (v == 1 and a < 0):
        answer = "(-oo; " + mtxt.f_t(x1n, x1d) + "] и [" + mtxt.f_t(x2n, x2d) + "; +oo)"
    else:
        answer = "[" + mtxt.f_t(x1n, x1d) + "; " + mtxt.f_t(x2n, x2d) + "]"

    y1s = mtxt.fc(a) + "x^2"
    y2s = mtxt.fc(-b) + "x" + mtxt.s(-c)

    return "y=" + y1s + " и y=" + y2s + " реши неравенство " + y1s + " " + (">=" if v == 0 else "<=") + " " + y2s, answer


def na_kakih_otrezkah_grafik_funktsii():
# на каких отрезках график функции: -x^2 лежит выше | ниже графика функции y = 2x-3
    v = rnd.randint(0, 1)

    x1 = (mrnd.rnd_w(-4, 4, [0]), mrnd.rnd_w(-5, 5, [0]))
    x2 = (mrnd.rnd_w(-4, 4, [0, x1[0]]), mrnd.rnd_w(-5, 5, [0, x1[0]]))

    if x1[0] / x1[1] > x2[0] / x2[1]:
        t = x1
        x1 = x2
        x2 = t

    a, b, c = mf.quad_pol_by_roots(x1, x2)

    x1n, x1d = mf.s_fraction((x1[0], x1[1]))
    x2n, x2d = mf.s_fraction((x2[0], x2[1]))

    if (v == 0 and a > 0) or (v == 1 and a < 0):
        answer = "(-oo; " + mtxt.f_t(x1n, x1d) + ") и (" + mtxt.f_t(x2n, x2d) + "; +oo)"
    else:
        answer = "(" + mtxt.f_t(x1n, x1d) + "; " + mtxt.f_t(x2n, x2d) + ")"

    return "y=" + mtxt.fc(a) + "x^2 лежит " + ("выше" if v == 0 else "ниже") + " графика функции y=" + mtxt.fc(-b) + "x" + mtxt.s(-c), \
           answer

def grafik_kakoj_funktsii_lezhit():
# график какой функции лежит: выше | ниже в точке x = -2 , y = -x^2 или y = -x - 3
    v = rnd.randint(0, 1)
    k = mrnd.rnd_w(-4, 4, [-1, 0, 1])
    a = mrnd.rnd_w(-7, 7, [0])
    b = mrnd.rnd_w(-7, 7, [0, a])
    x = rnd.randint(-5, 5)

    y1s = mtxt.fc(k) + "x^2"
    y2s = mtxt.fc(a) + "x" + mtxt.s(b)
    y1v = k * pow(x, 2)
    y2v = a * x + b

    if y1v == y2v:
        answer = "значения одинаковы"
    else:
        answer = (y1s if y1v > y2v else y2s) if v == 0 else (y1s if y1v < y2v else y2s)

    return ("выше" if v == 0 else "ниже") + " в точке x=" + str(x) + " y=" + y1s + " или y=" + y2s, answer

def chto():
    # что: меньше | больше -x^2 или 2x-3, если x = -2
    m = rnd.randint(0, 1)
    k = mrnd.rnd_w(-4, 4, [-1, 0, 1])
    a = mrnd.rnd_w(-7, 7, [0])
    b = mrnd.rnd_w(-7, 7, [0, a])
    x = rnd.randint(-5, 5)

    y1s = mtxt.fc(k) + "x^2"
    y2s = mtxt.fc(a) + "x" + mtxt.s(b)
    y1v = k * pow(x, 2)
    y2v = a * x + b

    if y1v == y2v:
        answer = "значения одинаковы"
    else:
        answer = (y1s if y1v < y2v else y2s) if m == 0 else (y1s if y1v > y2v else y2s)

    return ("меньше" if m == 0 else "больше") + " " + y1s + " или " + y2s + ", если x=" + str(x), answer

def graficheski_opredeli_chislo_reshenij_sistemyi_uravnenij():
# Графически определи число решений системы уравнений: {y=3x^2; y=x-3}
    t = rnd.randint(0, 2)

    a, b, c = mrnd.quad_pol_by_rcount(t)
    b = -b
    c = -c

    return "{y=" + mtxt.fc(b) + "x" + mtxt.s(c) + "; y=" + mtxt.fc(a) + "x^2}", \
           ("0") if t == 0 else ("1" if t == 1 else "2")

def skolko_raz_grafik_pryamoj():
# сколько раз график прямой y=x-3 пересекает параболу y = 3x^2
    t = rnd.randint(0, 2)

    a, b, c = mrnd.quad_pol_by_rcount(t)
    b = -b
    c = -c

    return "y=" + mtxt.fc(b) + "x" + mtxt.s(c) + " пересекает параболу y=" + mtxt.fc(a) + "x^2", \
           ("0") if t == 0 else ("1" if t == 1 else "2")

def reshi_graficheski_sistemu_uravnenij568():
# Реши графически систему уравнений: {y = -3|x|; y = -x^2}
    s1 = rnd.randint(0, 1)
    s2 = rnd.randint(0, 1)

    k = rnd.choice([1, 2, 3, 5])
    m = rnd.choice([1, 2, 3, 5])
    a = m * k

    if s1 == s2:
        answer = "0; " + str(m) + "; -" + str(m)
    else:
        answer = "0"

    return "{y=" + mtxt.fc(a * (1 if s1 == 0 else -1)) + "|x|; y=" +  mtxt.fc(k * (1 if s2 == 0 else -1)) + "x^2}", answer

def postroj_grafik_funktsii():
# построй график функции: y = -2|x|
    a = mrnd.rnd_w(-3, 3, [0])
    return "y = " + mtxt.fc(a) + "|x|", "график"

def reshi_graficheski_sistemu_uravnenij():
# Реши графически систему уравнений: {y = 2x^2; y + 2x - 4 = 0}
    x1 = mrnd.rnd_w0(-6, 6)
    x2 = mrnd.rnd_w(-6, 6, [0, x1])

    a = 1
    b = -x1 - x2
    c = x1 * x2

    return "{y=x^2; y" + mtxt.fc(b, is_first=False) + "x" + mtxt.s(c) + "=0}", \
        str(x1) + " и " + str(x2)


def tochki_peresecheniya_kakih_grafikov_nuzhno_najti_chtobyi_graficheski_reshit_sistemu_uravnenij():
# точку пересечения каких гафиков нужно найти, чтобы графически решить систему уравнений: {y = 2x^2; y + 2x - 4 = 0}
    a = mrnd.rnd_w(-7, 7, [0])
    b = mrnd.rnd_w(-7, 7, [0, a])

    k = mrnd.rnd_w(-5, 5, [0])

    return "{y=" + mtxt.fc(k) + "x^2; y" + mtxt.fc(-a, is_first=False) + "x" + mtxt.s(-b) + "=0}", \
           "y=" + mtxt.fc(k) + "x^2 и y=" + mtxt.fc(a) + "x" + mtxt.s(b)

def vyirazi_y_iz_uravneniya():
# вырази y из уравнения: y + 2x - 4 = 0
    a = mrnd.rnd_w(-7, 7, [0])
    b = mrnd.rnd_w(-7, 7, [0, a])
    return "y" + mtxt.fc(-a, is_first=False) + "x" + mtxt.s(-b) + "=0", "y=" + mtxt.fc(a) + "x" + mtxt.s(b)

def reshi_graficheski_uravnenie():
# Реши графически уравнение: 1/2*x^2 = 1/2*x + 2
    x1 = mrnd.rnd_w0(-6, 6)
    x2 = mrnd.rnd_w(-6, 6, [0, x1])

    a = 1
    b = -x1 - x2
    c = x1 * x2

    return "x^2 = " + mtxt.fc(x1 + x2) + "x" + ("+" if -c > 0 else "") + str(-c), str(x1) + " и " + str(x2)

def tochku_peresecheniya_kakih_gafikov_nuzhno_najti_chtobyi_graficheski_reshit_uravnenie():
# точку пересечения каких гафиков нужно найти, чтобы графически решить уравнение: 2x^2 = 2x - 2
    a = mrnd.rnd_w(-6, 6, [0])
    k = mrnd.rnd_w(-4, 4, [0])
    b = mrnd.rnd_w(-7, 7, [0])
    y1s = mtxt.fc(a) + "x^2"
    y2s = mtxt.fc(k) + "x" + ("+" if b > 0 else "") + str(b)

    return y1s + " = " + y2s, "y=" + y1s + " и " + "y=" + y2s

def vozrastaet_ili_ubyivaet_funktsiya_na_otrezke():
# Возрастает или убывает функция на отрезке: [1; 3], y = -2x^2
    a = mrnd.rnd_w(-6, 6, [-1, 0, 1])
    x1 = rnd.randint(-10, 5)
    x2 = rnd.randint(x1 + 1, 10)

    answer = ""
    if x1 * x2 < 0:
        answer = "на отрезке [" + str(x1) + "; 0] - " + ("убывает" if a > 0 else "возрастает") + \
                 ", на отрезке [0; " + str(x2) + "] - " + ("возрастает" if a > 0 else "убывает")
    else:
        answer = ("убывает" if a > 0 else "возрастает") if x1 < 0 else ("убывает" if a < 0 else "возрастает")

    return "[" + str(x1) + "; " + str(x2) + "], y=" + mtxt.fc(a) + "x^2", answer

def najdite_koeffitsient_k_v_uravnenii_parabolyi_esli_izvestno_chto_parabola_prohodit_cherez_tochku():
# Найдите коэффициент k в уравнении параблоы, если известно, что парабола проходит через точку: M(2; -8)
    a = mrnd.rnd_w(-7, 7, [-1, 0, 1])
    x = mrnd.rnd_w(-4, 4, [0])
    y = a * pow(x, 2)
    return "M(" + str(x) + "; " + str(y) + ")", str(a)

def opredelite():
# Определите: максимум | минимум функции на отрезке: [|)-1; 4]|), y = x^2
    is_max = rnd.randint(0, 1)
    a = mrnd.rnd_w(-5, 5, [-1, 0, 1])
    x1 = rnd.randint(1, 7)
    x2 = mrnd.rnd_w(-7, -1, [-x1])

    answer = ""
    if a > 0:
        if is_max == 1:
            answer = 0
        else:
            answer = a * pow(x1, 2) if x1 > -x2 else a * pow(x2, 2)
    else:
        if is_max == 0:
            answer = 0
        else:
            answer = a * pow(x1, 2) if x1 > -x2 else a * pow(x2, 2)

    return ("максимум" if is_max == 0 else "минимум") + " функции на отрезке " +\
        rnd.choice(["(", "["]) + str(x2) + "; " + str(x1) + rnd.choice([")", "]"]) + ", y=" + mtxt.fc(a) + "x^2", \
        str(answer)

def v_kakoj_tochke_funktsiya_prinimaet():
# в какой точке функция принимает: большее | меньшее значение, при x = 2 или при x = -3, y = -2x^2
    b = rnd.randint(0, 1)
    a = mrnd.rnd_w(-5, 5, [-1, 0, 1])
    x1 = rnd.randint(1, 7)
    x2 = mrnd.rnd_w(-7, -1, [-x1])

    answer = ""
    if b == 0:
        answer = "при x=" + (str(x1) if a*pow(x1, 2) > a*pow(x2, 2) else str(x2))
    else:
        answer = "при x=" + (str(x1) if a * pow(x1, 2) < a * pow(x2, 2) else str(x2))

    return ("большее" if b == 0 else "меньшее") + " значение, при x=" + str(x1) + " или при x=" + str(x2) + ", y=" + mtxt.fc(a) + "x^2", \
           answer

def opredelite_kakim_promezhutkam_prinadlezhit_argument_funktsii_esli_znacheniya_funktsii_nahodyatsya_v_diapazone():
# Определите каким промежуткам принадлежит аргумент, если значения функции находятся в диапазоне: [4, 9], y = x^2
    a = mrnd.rnd_w(-5, 5, [-1, 0, 1])

    x1 = rnd.randint(1, 6)
    x2 = rnd.randint(x1 + 1, 9)

    if a > 0:
        y1 = a * pow(x1, 2)
        y2 = a * pow(x2, 2)
    else:
        y1 = a * pow(x2, 2)
        y2 = a * pow(x1, 2)

    return "[" + str(y1) + "; " + str(y2) + "], y=" + mtxt.fc(a) + "x^2", "[" + str(-x2) + "; " + str(-x1) + "]" + " и " + \
        "[" + str(x1) + "; " + str(x2) + "]"

def pri_kakih_znacheniyah_argumenta_funktsiya():
# при каких значениях аргумента функция: y = -2x^2 принимает значение -8
    a = mrnd.rnd_w(-8, 8, [-1, 0, 1])
    x = rnd.randint(-7, 7)
    y = a * pow(x, 2)
    return "y=" + mtxt.fc(a) + "x^2 принимает значение " + str(y), str(x) + " и " + str(-x)

def skolko_raznyih_znachenij_x_sootvetstvuet_znacheniyu():
# сколько разных значений x соответствует значению: y = (+|-)3 для функции y = 2x^2
    a = mrnd.rnd_w(-8, 8, [-1, 0, 1])
    y = mrnd.rnd_w(-5, 5)
    return "y=" + str(y) + " для функции y=" + mtxt.fc(a) + "x^2", (("2" if y > 0 else "0") if a!= 0 else "1") if a > 0 \
        else (("2" if y < 0 else "0") if a!= 0 else "1")

def grafik_kakoj_funktsii():
# График какой функции выше | ниже в точке: x = 2, y1=3x^2 или y2=-2x^2
    v = rnd.randint(0, 1)
    a1 = mrnd.rnd_w(-7, 7, [-1, 0, 1])
    a2 = mrnd.rnd_w(-7, 7, [-1, 0, 1, a1])
    x = rnd.randint(-6, 6)
    y1s = "y=" + mtxt.fc(a1) + "x^2"
    y2s = "y=" + mtxt.fc(a2) + "x^2"

    if x == 0:
        answer = "одинаковое значение"
    else:
        answer = (y1s if a1 > a2 else y2s) if v == 0 else (y1s if a1 < a2 else y2s)

    return ("выше" if v == 0 else "ниже") + " в точке x=" + str(x) + ": " + y1s + " или " + y2s, answer

def postrojte_grafik_funktsii():
# Постройте график функции: y = (+|-)3x^2
    a = mrnd.rnd_w(-7, 7, [-1, 0, 1])
    return "y = " + mtxt.fc(a) + "x^2", "график"

def prinadlezhit_li_grafiku_funktsii():
# принадлежит ли графику функции: y = -3x^2 точка (-2; -8)
    a = mrnd.rnd_w(-7, 7, [-1, 0, 1])
    p = rnd.randint(0, 1)
    x = rnd.randint(-10, 10)

    y = a * pow(x, 2)
    if p == 1:
        if rnd.randint(0, 1) == 0:
            y += (1 if rnd.randint(0, 1) == 0 else -1) * rnd.randint(1, 3)
        else:
            y = -y

    return "y = " + mtxt.fc(a) + "x^2 точка " + mtxt._(str(x) + "; " + str(y)), "принадлежит" if p == 0 else "не принадлежит"

def postroj_po_tochkam_grafik_funktsii551():
# построй по точкам график функции: y = -2x^2
    a = rnd.randint(2, 7)
    return "y = -" + mtxt.fc(a) + "x^2", "график"

def postroj_po_tochkam_grafik_funktsii():
# построй по точкам график функции: y = 3x^2
    a = rnd.randint(2, 7)
    return "y = " + mtxt.fc(a) + "x^2", "график"

def chemu_ravno549():
# чему равно: 2x^2, если x = -3
    a = rnd.randint(2, 7)
    sx = rnd.randint(0, 1)
    sa = rnd.randint(0, 1)
    x = rnd.randint(1, 5)
    return mtxt.fc(a * (-1 if sa == 1 else 1)) + "x^2, если x = " + ("" if sx == 0 else "-") + str(x), str((-1 if sa == 1 else 1) * a * pow(x, 2))


def reshi_neravenstvo548():
# Реши неравенство: 3/(2^x-1) - 2/(2^x-2) <= 0
    n = rnd.choice([2, 3, 5, 7])
    s = rnd.randint(0, 1)

    n1 = rnd.randint(1, 7)
    k1 = rnd.randint(1, 3)
    m1 = mrnd.rnd_w(2, 5, [k1])

    n2 = mrnd.rnd_w(1, 7, [n1])
    k2 = mrnd.rnd_w(1, 3, [k1])
    while n1 * k2 + (1 if s == 0 else -1) * k1 * n2 == 0:
        k2 = mrnd.rnd_w(1, 3, [k1])
    m2 = mrnd.rnd_w(2, 5, [k2])
    while m1 * k2 == m2 * k1:
        m2 = mrnd.rnd_w(2, 5, [k2])

    lr = rnd.randint(0, 1)

    s1 = n1 * k2 + (1 if s == 0 else -1) * k1 * n2

    t1n, t1d = mf.s_fraction((n1 * m2 + (1 if s == 0 else -1) * n2 * m1, s1))
    t2n, t2d = mf.s_fraction((m1, k1))
    t3n, t3d = mf.s_fraction((m2, k2))

    ts = [(t1n, t1d), (t2n, t2d), (t3n, t3d)]
    ts.sort(key=lambda x: x[0] / x[1])

    def sk(t, ind):
        if ind == ts.index((t1n, t1d)) + 1:
            return "[" if t == 0 else "]"
        else:
            return "(" if t == 0 else ")"

    def l(ti):
        if ts[ti-1][1] != ts[ti-1][0]:
            p = mf.get_power_of(ts[ti-1][0]/ts[ti-1][0], n)
            if p == -1:
                return mtxt.log_text(n, mtxt.f_t(ts[ti-1][0], ts[ti-1][1]))
            else:
                return str(p)
        else:
            return "0"

    t1 = ts[0][0] / ts[0][1]

    slr = lr if s1 > 0 else 1 - lr
    if slr == 0:
        if t1 > 0:
            answer = sk(0, 1) + l(1) + "; " + l(2) + sk(1, 2) + " и " + sk(0, 3) + l(3) + "; +oo)"
        else:
            if ts[1][0] != ts[1][1]:
                answer = "(-oo; " + l(2) + sk(1, 2) + " и " + sk(0, 3) + l(3) + "; +oo)"
            else:
                answer = sk(0, 3) + l(3) + "; +oo)"
    else:
        if t1 > 0:
            if ts[1][0] != ts[1][1]:
                answer = "(-oo; " + l(1) + sk(1, 1) + " и " + sk(0, 2) + l(2) + "; " + l(3) + sk(1, 3)
            else:
                answer = sk(0, 2) + l(2) + "; " + l(3) + sk(1, 3)
        else:
            answer = sk(0, 2) + l(2) + "; " + l(3) + sk(1, 3)

    return str(n1) + "/" + mtxt._(mtxt.fc(k1) + ("*" if k1 != 1 else "") + mtxt.pow_text(str(n), "x") + "-" + str(m1)) + mtxt.p0m1(s) + \
           str(n2) + "/" + mtxt._(mtxt.fc(k2) + ("*" if k2 != 1 else "") + mtxt.pow_text(str(n), "x") + "-" + str(m2)) + " " + (">=" if lr == 0 else "<=") + " 0", \
           answer


def reshi_neravenstvo547():
# реши неравенство: 3/(2t-1) - 2/(t-2) <= 0
    s = rnd.randint(0, 1)

    n1 = rnd.randint(1, 7)
    k1 = rnd.randint(1, 3)
    m1 = mrnd.rnd_w(2, 5, [k1])

    n2 = mrnd.rnd_w(1, 7, [n1])
    k2 = mrnd.rnd_w(1, 3, [k1])
    while n1 * k2 + (1 if s == 0 else -1) * k1 * n2 == 0:
        k2 = mrnd.rnd_w(1, 3, [k1])
    m2 = mrnd.rnd_w(2, 5, [k2])
    while m1 * k2 == m2 * k1:
        m2 = mrnd.rnd_w(2, 5, [k2])

    lr = rnd.randint(0, 1)

    t1n, t1d = mf.s_fraction((n1 * m2 + (1 if s == 0 else -1) * n2 * m1, n1 * k2 + (1 if s == 0 else -1) * k1 * n2))
    t2n, t2d = mf.s_fraction((m1, k1))
    t3n, t3d = mf.s_fraction((m2, k2))

    ts = [(t1n, t1d), (t2n, t2d), (t3n, t3d)]
    ts.sort(key = lambda x: x[0]/x[1])

    def sk(t, ind):
        if ind == ts.index((t1n, t1d)) + 1:
            return "[" if t == 0 else "]"
        else:
            return "(" if t == 0 else ")"

    if lr == 0:
        answer = sk(0, 1) + mtxt.f_t(ts[0][0], ts[0][1]) + "; " + mtxt.f_t(ts[1][0], ts[1][1]) + sk(1, 2) + " и " + \
            sk(0, 3) + mtxt.f_t(ts[2][0], ts[2][1]) + "; +oo)"
    else:
        answer = "(-oo; " + mtxt.f_t(ts[0][0], ts[0][1]) + sk(1, 1) + " и " + sk(0, 2) + mtxt.f_t(ts[1][0], \
            ts[1][1]) + "; " + mtxt.f_t(ts[2][0], ts[2][1]) + sk(1, 3)

    return str(n1) + "/" + mtxt._(mtxt.fc(k1) + "t" + "-" + str(m1)) + mtxt.p0m1(s) + \
           str(n2) + "/" + mtxt._(mtxt.fc(k2) + "t" + "-" + str(m2)) + " " + (">=" if lr == 0 else "<=") + " 0", \
           answer


def reshi_neravenstvo546():
# Решите неравенство: log3->(log2->x) < 1
    n1 = rnd.choice([2, 3, 5, 7])
    n2 = mrnd.choice_w([2, 3, 5, 7], [n1])

    lr = rnd.randint(0, 1)
    a = rnd.choice([-2, -1, 1, 2])

    return mtxt.log_text(n1, mtxt._(mtxt.log_text(n2, "x"))) + " " + (">" if lr == 0 else "<") + " " + str(a), \
           "x " + (">" if lr == 0 else "<") + " " + mtxt.pow_text(n2, mtxt._(pow(n1, a) if a > 0 else ("1/" + str(pow(n1, -a)))))


def reshi_neravenstvo545():
# Решите неравенство: (log2->x)^2 - 6log5->x*log9->x > 0
    n = rnd.choice([2, 3, 5, 7])
    lr = rnd.randint(0, 1)

    k1 = rnd.randint(2, 4)
    k2 = mrnd.rnd_w(2, 4, [k1])

    fpol = rnd.randint(0, 1)
    a = rnd.randint(1, 3)
    b = a * k1 * k2

    if fpol == 1:
        osn1 = str(pow(n, k1) - rnd.randint(1, 2))
        osn2 = str(pow(n, k2) - rnd.randint(1, 2))
    else:
        osn1 = str(pow(n, k1) + rnd.randint(1, 2))
        osn2 = str(pow(n, k2) + rnd.randint(1, 2))

    answer = "(0; +oo)\{1}" if fpol == lr else "нет решений"

    return mtxt.fc(a) + mtxt.pow_text(mtxt._(mtxt.log_text(n, "x")), 2) + " - " + \
           mtxt.fc(b) + " * " + mtxt.log_text(osn1, "x") + " * " + mtxt.log_text(osn2, "x") + " " + (">" if lr == 0 else "<") + " 0", \
           answer

def reshite_neravenstvo544():
# решите неравенство: log2->x < | > 0
    n = rnd.choice([2, 3, 5, 7])
    lr = rnd.randint(0, 1)
    return mtxt.log_text(n, "x") + " " + (">" if lr == 0 else "<") + " 0", "x " + (">" if lr == 0 else "<") + " 1"

def chto_bolshe543():
# что больше: 6 или log2->5 * log2->9
    n = rnd.choice([3, 5])
    lr = rnd.randint(0, 1)

    k1 = rnd.randint(2, 4)
    k2 = mrnd.rnd_w(2, 4, [k1])

    if lr == 0:
        x1s = str(pow(n, k1) - rnd.randint(1, 2))
        x2s = str(pow(n, k2) - rnd.randint(1, 2))
    else:
        x1s = str(pow(n, k1) + rnd.randint(1, 2))
        x2s = str(pow(n, k2) + rnd.randint(1, 2))

    exp = mtxt.log_text(n, x1s) + " * " + mtxt.log_text(n, x2s)

    return str(k1 * k2) + " или " + exp, (str(k1 * k2) if lr == 0 else exp) + " больше"

def reshi_neravenstvo542():
# Реши неравенство: log1/7->(x^2-4x-5) >= -1
    n = rnd.choice([2, 3, 5, 7])
    k = rnd.choice([-2, -1])
    lr = rnd.randint(0, 1)

    x1 = (mrnd.rnd_w(-4, 4, [0]), rnd.randint(1, 5))
    x2 = (mrnd.rnd_w(-4, 4, [0, x1[0]]), mrnd.rnd_w(1, 5, [x1[0]]))

    if x1[0] / x1[1] > x2[0] / x2[1]:
        t = x1
        x1 = x2
        x2 = t

    a = x1[1] * x2[1]
    b = -x1[0] * x2[1] - x1[1] * x2[0]
    c = x1[0] * x2[0] + pow(n, -k)

    px = pol.Polynomial([a, b, c], [2, 1, 0])

    x1n, x1d = mf.s_fraction(x1)
    x2n, x2d = mf.s_fraction(x2)

    answer = ""
    if a > 0 and lr == 0:
        answer = "[" + mtxt.f_t(x1n, x1d) + "; " + mtxt.f_t(x2n, x2d) + "]"
    else:
        answer = "(-oo; " + mtxt.f_t(x1n, x1d) + "] и [" + mtxt.f_t(x2n, x2d) + "; +oo)"

    return mtxt.log_text("1/" + str(n), mtxt._(px.get_str())) + (" >= " if lr == 0 else " <= ") + str(k), \
           answer

def reshite_neravenstvo():
# решите неравенство: log1/7->t >= -1
    n = rnd.choice([2, 3, 5, 7])
    a = rnd.choice([-2, -1, 1, 2])
    lr = rnd.randint(0, 1)
    return mtxt.log_text(mtxt.f_t(1, n), "t") + (" >= " if lr == 0 else " <= ") + str(a), \
           "t" + (" <= " if lr == 0 else " >= ") + ((mtxt.f_t(1, pow(n, a))) if a > 0 else (str(pow(n, -a))))

def reshi_neravenstvo539():
# Реши неравенство: 9^(x-1) + 3^(5-2x) <= 28
    n = rnd.randint(2, 5)
    lr = rnd.randint(0, 1)

    k1 = rnd.randint(0, 3)
    k2 = rnd.randint(0, 3)

    t1 = (pow(n, k1), 1)
    t2 = (1, pow(n, k2))

    a = t1[1] * t2[1]
    b = -t1[0] * t2[1] - t1[1] * t2[0]
    c = t1[0] * t2[0]

    k = mrnd.rnd_w(-5, 5, [0])

    s = str(k1 - 2 * k) + "-" + "2x"

    x1n, x1d = mf.s_fraction((k1 - 2*k, 2))
    x2n, x2d = mf.s_fraction((-k2 - 2*k, 2))

    if x1n/x1d > x2n/x2d:
        x1n, x2n = x2n, x1n
        x1d, x2d = x2d, x1d

    answer = ("(-oo; " + mtxt.f_t(x1n, x1d) + "] и [" + mtxt.f_t(x2n, x2d) + "; +oo)") if lr == 0 else ("[" + mtxt.f_t(x1n, x1d) + "; " + mtxt.f_t(x2n, x2d) + "]")

    return mtxt.fc(a) + ("*" if a != 1 else "") + mtxt.pow_text(pow(n, 2), mtxt._("x" + ("+" if k > 0 else "") + str(k))) + \
           " + " + mtxt.pow_text(n, mtxt._(s)) + (" >= " if lr == 0 else " <= ") + str(-b), \
            answer

def reshi_neravenstvo538():
# Реши неравенство:(1/2)^(2x^2+3x-6) < 2
    n = rnd.randint(2, 5)
    obr = rnd.randint(0, 1)
    lr = rnd.randint(0, 1)
    k = rnd.randint(1, 3)

    x1 = (mrnd.rnd_w(-4, 4, [0]), rnd.randint(1, 5))
    x2 = (mrnd.rnd_w(-4, 4, [0, x1[0]]), mrnd.rnd_w(1, 5, [x1[0]]))

    if x1[0] / x1[1] > x2[0] / x2[1]:
        t = x1
        x1 = x2
        x2 = t

    a = x1[1] * x2[1]
    b = -x1[0] * x2[1] - x1[1] * x2[0]
    c = x1[0] * x2[0]

    if obr == 0:
        alr = 1 - lr
        c -= k
    else:
        alr = lr
        c += k

    px = pol.Polynomial([a, b, c], [2, 1, 0])

    x1n, x1d = mf.s_fraction(x1)
    x2n, x2d = mf.s_fraction(x2)

    return mtxt.pow_text(str(n) if obr == 1 else mtxt._("1/" + str(n)), mtxt._(px.get_str())) + (" > " if lr == 0 else " < ") + str(pow(n, k)),\
        ("(-oo; " + mtxt.f_t(x1n, x1d) + "), (" + mtxt.f_t(x2n, x2d) + "; +oo)" ) if alr == 0 else \
               ("(" + mtxt.f_t(x1n, x1d) + "; " + mtxt.f_t(x2n, x2d) + ")")


def reshi_neravenstvo537():
# реши неравенство: 2x^2 + 3x - 5 > 0
    lr = rnd.randint(0, 1)

    x1 = (mrnd.rnd_w(-4, 4, [0]), rnd.randint(1, 5))
    x2 = (mrnd.rnd_w(-4, 4, [0, x1[0]]), mrnd.rnd_w(1, 5, [x1[0]]))

    if x1[0]/x1[1] > x2[0]/x2[1]:
        t = x1
        x1 = x2
        x2 = t

    a = x1[1] * x2[1]
    b = -x1[0] * x2[1] - x1[1] * x2[0]
    c = x1[0] * x2[0]

    px = pol.Polynomial([a, b, c], [2, 1, 0])

    x1n, x1d = mf.s_fraction(x1)
    x2n, x2d = mf.s_fraction(x2)

    return px.get_str() + (" > " if lr == 0 else " < ") + "0", \
           ("(-oo; " + mtxt.f_t(x1n, x1d) + "), (" + mtxt.f_t(x2n, x2d) + "; +oo)" ) if lr == 0 else \
               ("(" + mtxt.f_t(x1n, x1d) + "; " + mtxt.f_t(x2n, x2d) + ")")


def narisuj_grafik_funktsii():
# Нарисуй график функции: y = loga->x, если a = (3 | 1/3)
    obr = rnd.randint(0, 1)
    n = rnd.randint(2, 9)
    osn = ("1/" + str(n)) if obr == 0 else str(n)
    return "y = " + mtxt.log_text(osn, "x"), "график"

def verno_li_utverzhdenie536():
# верно ли утверждение:
# функция y = loga->x (пересекает | не пересекает) ось (x|y) в точке (0|1|a);
# функция y = loga->x в точке x = a (равна | не равна) (0|1);
# функция y = loga->x (возрастает|убывает) на отрезку (4 отрезка)
    t = rnd.randint(1, 3)

    obr = rnd.randint(0, 1)
    n = rnd.randint(2, 9)
    osn = ("1/" + str(n)) if obr == 0 else str(n)

    text = ""
    answer = ""
    if t == 1:
        p = rnd.randint(0, 1)
        os_x = rnd.randint(0, 1)
        tt = rnd.randint(1, 3)

        text = "функция y = " + mtxt.log_text(osn, "x") + \
               (" пересекает " if p == 0 else " не пересекает ") + "ось " + ("x" if os_x == 0 else "y") + \
                " в точке " + ("0" if tt == 0 else ("1" if tt == 1 else osn))
        if os_x == 0:
            if tt == 1:
                answer = "верно" if p == 0 else "не верно"
            else:
                answer = "верно" if p == 1 else "не верно"
        else:
            answer = "верно" if p == 1 else "не верно"
    if t == 2:
        r = rnd.randint(0, 1)
        z = rnd.randint(0, 1)
        text = "функция y = " + mtxt.log_text(osn, "x") + " в точке x = " + osn + (" равна" if r == 0 else " не равна") + \
               (" 0" if z == 0 else " 1")
        answer = ("верно" if z == 1 else "не верно") if r == 0 else ("верно" if z == 0 else "не верно")
    if t == 3:
        v = rnd.randint(0, 1)
        ot = rnd.randint(1, 4)
        ots = ""
        if ot == 1:
            ots = "(-oo; -1)"
        if ot == 2:
            ots = "(-1; 0)"
        if ot == 3:
            ots = "(0; 1)"
        if ot == 4:
            ots = "(1; +oo)"
        text = "функция y = " + mtxt.log_text(osn, "x") + " " + ("возрастает" if v == 0 else "убывает") + \
            " на отрезке " + ots

        if ot in [1, 2]:
            answer = "не верно"
        else:
            if v == 0:
                answer = "верно" if obr == 1 else "не верно"
            else:
                answer = "верно" if obr == 0 else "не верно"

    return text, answer

def ubyivaet_ili_vozrastaet_funktsiya_y_ravno_logaminus_x_esli():
# убывает или возрастает функция y = loga->x если: a = 3 | 1/3
    n = rnd.randint(2, 9)
    obr = rnd.randint(0, 1)
    return "y = " + mtxt.log_text(("1/" + str(n) if obr == 0 else str(n)), "x"), "убывает" if obr == 0 else "возрастает"


def reshi_neravenstvo533():
# Решите неравенство: 5logk(3)->x - 4log3->x + 4log9->x <= 8
    n = rnd.choice([2, 3, 5, 7])

    b1 = mrnd.rnd_w(-5, 5, [0, -1, 1])
    b2 = mrnd.rnd_w(-5, 5, [0, -1, 1])
    b3 = 2 * mrnd.rnd_w(-3, 3, [0])
    b = 2 * b1 + b2 + int(b3/2)
    while b == 0:
        b1 = mrnd.rnd_w(-5, 5, [0, -1, 1])
        b2 = mrnd.rnd_w(-5, 5, [0, -1, 1])
        b3 = 2 * mrnd.rnd_w(-3, 3, [0])
        b = 2 * b1 + b2 + int(b3/2)


    lr = rnd.randint(0, 1)

    answer = "x" + ((" >= " if b > 0 else " <= ") if lr == 0 else (" <= " if b > 0 else " >= ")) + str(n)

    return mtxt.fc(b1) + "*" + mtxt.log_text(mtxt.k_t(n), "x") + mtxt.p0m1(0 if b2 > 0 else 1) + \
           mtxt.fc(int(math.fabs(b2))) + "*" + mtxt.log_text(n, "x") + mtxt.p0m1(0 if b3 > 0 else 1) + \
           mtxt.fc(int(math.fabs(b3))) + "*" + mtxt.log_text(str(pow(n, 2)), "x") + (" >= " if lr == 0 else " <= ") + str(b), \
           answer

def reshi_neravenstvo532():
# реши неравенство: log3->x <= 2
    n = rnd.choice([2, 3, 5, 7])
    b = rnd.choice([-2, -1, 1, 2])
    lr = rnd.randint(0, 1)
    obr = rnd.randint(0, 1)

    mb = int(math.fabs(b))
    if obr == 1:
        answer = "x " + (" >= " if lr == 0 else " <= ") + ("1/" + str(pow(n, mb)) if b < 0 else str(pow(n, b)))
    else:
        tb = -b
        answer = "x " + (" <= " if lr == 0 else " >= ") + (("1/" + str(pow(n, mb))) if tb < 0 else str(pow(n, tb)))

    return mtxt.log_text(("" if obr == 1 else "1/") + str(n), "x") + (" >= " if lr == 0 else " <= ") + str(b), \
           answer

def najdi():
    kb = rnd.randint(0, 4)
    s = rnd.randint(0, 1)
    if kb == 0:
        n = rnd.randint(1, 7)
        k = pow(n, 2) + rnd.randint(1, 7)
    else:
        n = rnd.randint(3, 7)
        k = pow(n, 2) - rnd.randint(1, 7)

    exp = str(n) + mtxt.p0m1(s) + mtxt.k_t(k)
    expm = mtxt.k_t(k) + " - " + str(n)

    return mtxt.mod(exp), exp if (s == 0 or (s == 1 and kb == 1)) else expm

def modul_chisla_minus_eto_rasstoyanie_ot_chisla_do_0_najdi_modul_chisla():
    if rnd.choice([0, 0, 1, 0]) == 0:
        n = rnd.randint(-9, -1)
    else:
        n = rnd.randint(1, 9)
    return str(n), str(int(math.fabs(n)))

def najdi_rasstoyanie_ot_nulya_do_chisla_esli_polozhitelnoe_to_samo_chislo_esli_otritsatelnoe_to_domnozhit_na_minus1():
    if rnd.choice([0, 0, 1]) == 0:
        n = rnd.randint(-9, -1)
    else:
        n = rnd.randint(1, 9)
    return str(n), str(int(math.fabs(n)))

def chislo_bolshe_nulya_ili_menshe():
    kb = rnd.randint(0, 1)
    s = rnd.randint(0, 1)
    if kb == 0:
        n = rnd.randint(1, 7)
        k = pow(n, 2) + rnd.randint(1, 7)
    else:
        n = rnd.randint(3, 7)
        k = pow(n, 2) - rnd.randint(1, 7)

    return str(n) + mtxt.p0m1(s) + mtxt.k_t(k), "больше нуля" if (s == 0 or (s == 1 and kb == 1)) else "меньше нуля"

def umnozh_chislo_na_minus1():
    n = rnd.randint(1, 9)
    s = rnd.randint(0, 1)
    return ("" if s == 0 else "-") + str(n), ("-" + str(n)) if s == 0 else str(n)

def chemu_ravno():
    n = rnd.randint(1, 9)
    s = rnd.randint(0, 1)
    return "-" + mtxt._(("" if s == 0 else "-") + str(n)), ("-" + str(n)) if s == 0 else str(n)

def predstavte_v_vide():
# Представьте в виде: квадрата|куба одночлена a^6 * b^12
    kv_kb = rnd.randint(0, 1)
    a_base = rnd.randint(1, 7)
    b_base = mrnd.rnd_w(1, 7, [a_base])
    return ("квадрата" if kv_kb == 0 else "куба") + " " + mtxt.pow_text("a", (2 if kv_kb == 0 else 3) * a_base) + "*" + mtxt.pow_text("b", (2 if kv_kb == 0 else 3) * b_base) \
        , mtxt.pow_text(mtxt._(mtxt.pow_text("a", a_base) + "*" +  mtxt.pow_text("b", b_base)), (2 if kv_kb == 0 else 3))


def umnozh_odnochlenyi():
    ps = []
    for i in range(0, 3):
        psi = []
        for j in range(0, 3):
            psi.append(mrnd.rnd_w(1, 7, psi))
        ps.append(psi)

    text = ""
    for o in ps:
        text += mtxt.pow_text("a", o[0]) + "*" + mtxt.pow_text("b", o[1]) + "*" + mtxt.pow_text("c", o[2])
        if ps.index(o) != len(ps) - 1:
            text += ", "

    return text, mtxt.pow_text("a", ps[0][0] + ps[1][0] + ps[2][0]) + "*" + mtxt.pow_text("b", ps[0][1] + ps[1][1] + ps[2][1]) + "*" + mtxt.pow_text("c", ps[0][2] + ps[1][2] + ps[2][2])


def vozvedi_odnochlen_v_kvadrat():
# Возведи одночелн в квадрат: a^2*b^3*с
    a = rnd.randint(1, 7)
    b = mrnd.rnd_w(1, 7, [a])
    c = mrnd.rnd_w(1, 7, [a, b])
    return mtxt.pow_text("a", a) + "*" + mtxt.pow_text("b", b) + "*" + mtxt.pow_text("c", c), \
           mtxt.pow_text("a", 2*a) + "*" + mtxt.pow_text("b", 2*b) + "*" + mtxt.pow_text("c", 2*c)

def najdite_znachenie_vyirazheniya__aplusb_():
# Найдите значение выражения |a+b|: если a=2k(7)-5, b=k(7)-3
    n2 = mrnd.rnd_w(3, 10, [4, 9])
    kb = rnd.randint(0, 1)
    if kb == 0:
        n1 = rnd.choice([2, 3, 5])
        d = math.floor(n2 / math.sqrt(n1))
        f = max([2, rnd.randint(d + 1, d + 7)])
    else:
        f = rnd.randint(2, 4)
        n1 = rnd.randint(math.floor(f * math.sqrt(n2)) + 1, math.floor(f * math.sqrt(n2)) + 7)

    n11 = rnd.randint(1, n1 - 1)
    n12 = n1 - n11

    f1 = rnd.randint(1, f - 1)
    f2 = f - f1

    a = str(n11) + " - " + mtxt.fc(f1) + mtxt.k_t(n2)
    b = str(n12) + " - " + mtxt.fc(f2) + mtxt.k_t(n2)

    if kb == 0:
        answer = mtxt.fc(f) + mtxt.k_t(n2) + " - " + str(n1)
    else:
        answer = str(n1) + " - " + mtxt.fc(f) + mtxt.k_t(n2)

    return "a = " + a + ", b = " + b, answer

def chemu_ravnyaetsya523():
# чему равняется |2k(7)-5 + (k(7) - 3)|
    n2 = rnd.randint(3, 10)
    kb = rnd.randint(0, 1)
    if kb == 0:
        n1 = rnd.choice([2, 3, 5])
        d = math.floor(n2 / math.sqrt(n1))
        f = max([2, rnd.randint(d + 1, d + 7)])
    else:
        f = rnd.randint(2, 4)
        n1 = rnd.randint(math.floor(f * math.sqrt(n2)) + 1, math.floor(f * math.sqrt(n2)) + 7)

    n11 = rnd.randint(1, n1 - 1)
    n12 = n1 - n11

    f1 = rnd.randint(1, f - 1)
    f2 = f - f1

    a = str(n11) + " - " + mtxt.fc(f1) + mtxt.k_t(n2)
    b = str(n12) + " - " + mtxt.fc(f2) + mtxt.k_t(n2)

    if kb == 0:
        answer = mtxt.fc(f) + mtxt.k_t(n2) + " - " + str(n1)
    else:
        answer = str(n1) + " - " + mtxt.fc(f) + mtxt.k_t(n2)

    return mtxt.mod(a + " + " +b), answer

def najdi_znachenie_vyirazheniya__aminusb_():
# Найдите значение выражения |a-b|: если a=2k(3)-3, b=2-k(3)
    n2 = mrnd.rnd_w(3, 10, [4, 9])
    kb = rnd.randint(0, 1)
    if kb == 0:
        n1 = rnd.choice([2, 3, 5])
        d = math.floor(n2 / math.sqrt(n1))
        f = max([2, rnd.randint(d + 1, d + 7)])
    else:
        f = rnd.randint(2, 4)
        n1 = rnd.randint(math.floor(f * math.sqrt(n2)) + 1, math.floor(f * math.sqrt(n2)) + 7)

    n11 = rnd.randint(1, n1 - 1)
    n12 = n1 - n11

    f1 = rnd.randint(1, f - 1)
    f2 = f - f1

    a = mtxt.fc(f1) + mtxt.k_t(n2) + " - " + str(n11)
    b = str(n12) + " - " + mtxt.fc(f2) + mtxt.k_t(n2)

    if kb == 0:
        answer = mtxt.fc(f) + mtxt.k_t(n2) + " - " + str(n1)
    else:
        answer = str(n1) + " - " + mtxt.fc(f) + mtxt.k_t(n2)

    return "a = " + a + ", b = " + b, answer

def chemu_ravnyaetsya519():
# чему равняется: |2k(3) - 3 - (2 - k(3))|
    n2 = rnd.randint(3, 10)
    kb = rnd.randint(0, 1)
    if kb == 0:
        n1 = rnd.choice([2, 3, 5])
        d = math.floor(n2 / math.sqrt(n1))
        f = max([2, rnd.randint(d + 1, d + 7)])
    else:
        f = rnd.randint(2, 4)
        n1 = rnd.randint(math.floor(f * math.sqrt(n2)) + 1, math.floor(f * math.sqrt(n2)) + 7)

    n11 = rnd.randint(1, n1 - 1)
    n12 = n1 - n11

    f1 = rnd.randint(1, f - 1)
    f2 = f - f1

    a = mtxt.fc(f1) + mtxt.k_t(n2) + " - " + str(n11)
    b = str(n12) + " - " + mtxt.fc(f2) + mtxt.k_t(n2)

    if kb == 0:
        answer = mtxt.fc(f) + mtxt.k_t(n2) + " - " + str(n1)
    else:
        answer = str(n1) + " - " + mtxt.fc(f) + mtxt.k_t(n2)

    return mtxt.mod(a + " - " + mtxt._(b)), answer

def chemu_ravnyaetsya518():
# чему равняется: |2 +- k(5)|
    n1 = rnd.randint(2, 9)
    kb = rnd.randint(0, 1)
    if kb == 0:
        n2 = rnd.randint(pow(n1, 2) + 1, pow(n1, 2) + 7)
    else:
        n2 = rnd.randint(2, pow(n1, 2) - 1)
    s = rnd.randint(0, 1)

    exp = str(n1) + mtxt.p0m1(s) + mtxt.k_t(n2)
    if s == 1 and kb == 0:
        answer = mtxt.k_t(n2) + " - " + str(n1)
    else:
        answer = exp

    return mtxt.mod(exp), answer

def chemu_ravnyaetsya517():
# чему равняется: |k(3)|-k(3)|
    n = rnd.randint(1, 9)
    return mtxt.mod(("" if rnd.randint(0, 1) == 0 else "-") + mtxt.k_t(n)), mtxt.k_t(n)

def chemu_ravnyaetsya():
# чему равняется: |-3|3|
    n = rnd.randint(1, 9)
    return mtxt.mod(("" if rnd.randint(0, 1) == 0 else "-") + str(n)), str(n)

def reshi_neravenstvo515():
# Реши неравенство: 81*2^x - 16*3^x < 0
    n1 = rnd.choice([2, 3, 5])
    n2 = mrnd.choice_w([2, 3, 5], [n1])
    k = rnd.randint(2, 4)
    lr = rnd.randint(0, 1)
    obr = rnd.randint(0, 1)

    ms = (">" if n1 > n2 else "<") if lr == 0 else ("<" if n1 > n2 else ">")

    return mtxt.fc(pow((n2 if obr == 1 else n1), k)) + "*" + mtxt.pow_text(n1, "x") + " - " + mtxt.fc(pow((n1 if obr == 1 else n2), k)) + "*" + mtxt.pow_text(n2, "x") + (" > " if lr == 0 else " < " ) + "0", \
           "x" + " " + ms + " " + ("" if obr == 1 else "-") + str(k)

def reshi_neravenstvo514():
# Реши неравенство: 3^(2x+1) - 9^x < 2/3
    n, a = mrnd.common_base_power()
    k = rnd.randint(2, 3)
    lr = rnd.randint(0, 1)
    s = rnd.randint(0, 1)
    return mtxt.pow_text(n, mtxt._(str(k) + "x+" + str(a))) + mtxt.p0m1(s) + mtxt.pow_text(pow(n, k), "x") + \
           (" > " if lr == 0 else " < ") + mtxt.f_t((pow(n, a) + 1 if s == 0 else pow(n, a) - 1), n), \
            ("x > " + "-1/" + str(k)) if lr == 0 else ("x < " + "-1/" + str(k))

def reshi_neravenstvo513():
# реши неравенство: 3^(2x) < 1/3
    n = rnd.randint(2, 7)
    k = mrnd.rnd_w(2, 7, [n])
    lr = rnd.randint(0, 1)
    return mtxt.pow_text(n, mtxt._(str(k) + "x")) + (" > " if lr == 0 else " < ") + "1/" + str(n), \
           ("x > " + "-1/" + str(k)) if lr == 0 else ("x < " + "-1/" + str(k))

def reshi_uravnenie512():
# Реши уравнение: 9^x - 5*3^x + 6 = 0
    x1 = (mrnd.rnd_w(-4, 4, [0]), rnd.randint(1, 5))
    x2 = (mrnd.rnd_w(-4, 4, [0, x1[0]]), mrnd.rnd_w(1, 5, [x1[0]]))
    a = x1[1] * x2[1]
    b = -x1[0] * x2[1] - x1[1] * x2[0]
    c = x1[0] * x2[0]

    n = rnd.randint(2, 5)

    def get_answer(n, rn, rd):
        if rn == rd:
            return "0"
        tn, td = mf.s_fraction((rn, rd))

        if mf.if_power_of(tn / td, n):
            return str(int((tn / td) // n))
        if mf.if_power_of(n, tn / td):
            return str(int(n // (tn / td)))
        return mtxt.log_text(n, mtxt.f_t(tn, td))

    if x1[0] < 0 and x2[0] < 0:
        answer = "нет решений"
    if x1[0] > 0 and x2[0] > 0:
        answer = get_answer(n, x1[0], x1[1]) + " и " + get_answer(n, x2[0], x2[1])
    if x1[0] > 0 and x2[0] < 0:
        answer = get_answer(n, x1[0], x1[1])
    if x1[0] < 0 and x2[0] > 0:
        answer = get_answer(n, x2[0], x2[1])

    return mtxt.fc(a) + "*" + mtxt.pow_text(pow(n, 2), "x") + mtxt.fc(b, False) + "*" + mtxt.pow_text(n, "x") + mtxt.fc(c, False) + "=0", answer

def chemu_ravno_a511():
# чему равно a: 9^x = (3^x)^a
    n, k = mrnd.common_base_power()
    return mtxt.pow_text(pow(n, k), "x") + " = " + mtxt.pow_text(mtxt._(mtxt.pow_text(n, "x")), "a"), str(k)

def reshi_neravenstvo510():
# Реши неравенство: 48 * (1/4)^x > 3
    n, k = mrnd.common_base_power()
    m = mrnd.choice_w([2, 3, 5, 7], [n])
    lr = rnd.randint(0, 1)
    return str(pow(n, k) * m) + mtxt.pow_text(mtxt._("1/" + str(n)), "x") + (" > " if lr == 0 else " < ") + str(m), \
           "x" + (" > " if lr == 1 else " < ") + str(k)

def reshi_neravenstvo():
# реши неравенство: (1/4)^x > (1/4)^2
    n = rnd.randint(2, 7)
    k = rnd.randint(2, 7)
    lr = rnd.randint(0, 1)
    return mtxt.pow_text(mtxt._("1/" + str(n)), "x") + (" > " if lr == 0 else " < ") + mtxt.pow_text(mtxt._("1/" + str(n)), k), \
           "x" + (" > " if lr == 1 else " < ") + str(k)

def h_dolzhen_byit_bolshe_ili_menshe_chem508():
# х должен быть больше или меньше чем: 2, чтобы (1/2)^x > (1/2)^2
    n = rnd.randint(2, 7)
    k = rnd.randint(2, 7)
    lr = rnd.randint(0, 1)
    return str(k) + ", чтобы " + mtxt.pow_text(mtxt._("1/" + str(n)), "x") + (" > " if lr == 0 else " < ") + mtxt.pow_text(mtxt._("1/" + str(n)), k), \
       "больше" if lr == 1 else "меньше"

def h_dolzhen_byit_bolshe_ili_menshe_chem():
# х должен быть больше или меньше чем: 2, чтобы 3^x > 3^2
    n = rnd.randint(2, 7)
    k = rnd.randint(2, 7)
    lr = rnd.randint(0, 1)
    return str(k) + ", чтобы " + mtxt.pow_text(n, "x") + (" > " if lr == 0 else " < ") + mtxt.pow_text(n, k),\
           "больше" if lr == 0 else "меньше"

def chto_bolshe():
# что больше: (1/4|4)^3 или (1/4|4)^2
    n = rnd.randint(2, 7)
    d = rnd.randint(0, 1)
    k1 = rnd.randint(2, 7)
    k2 = mrnd.rnd_w(2, 7, [k1])
    s1 = mtxt.pow_text(mtxt._(("1/" + str(n)) if d == 1 else str(n)), k1)
    s2 = mtxt.pow_text(mtxt._(("1/" + str(n)) if d == 1 else str(n)), k2)
    return s1 + " или " + s2, (s1 if k1 < k2 else s2) if d == 1 else (s1 if k1 > k2 else s2)

def uvelichitsya_chislo_ili_umenshitsya_esli_ego_umnozhat_na():
# увеличится число или уменьшится если его умножать на: (1/4|4)
    n = rnd.randint(2, 7)
    d = rnd.randint(0, 1)
    return ("1/" + str(n)) if d == 1 else str(n), "уменьшится" if d == 1 else "увеличится"

def reshi_uravnenie504():
# Реши уравнение: 3^(8x^2-6x-13) - 3^(4x^2-3x-7) = 2
    n = rnd.randint(2, 3)
    k1 = rnd.randint(2, 3)
    bt_sign = rnd.randint(0, 1)
    bt = pow(n, k1) if bt_sign == 0 else -pow(n, k1)
    rc = mrnd.rnd_w(2, 3, [k1])
    t1 = pow(n, rc)
    t2 = - t1 - bt
    at = 1
    ct = t1 * t2

    x1 = (mrnd.rnd_w(-4, 4, [0]), rnd.randint(1, 5))
    x2 = (mrnd.rnd_w(-4, 4, [0, x1[0]]), mrnd.rnd_w(1, 5, [x1[0]]))
    a = x1[1] * x2[1]
    b = -x1[0] * x2[1] - x1[1] * x2[0]
    c = x1[0] * x2[0] + rc
    px = pol.Polynomial([a, b, c], [2, 1, 0])
    px1 = pol.Polynomial([2 * a, 2 * b, 2 * c - 2*k1], [2, 1, 0])

    x1n, x1d = mf.s_fraction(x1)
    x2n, x2d = mf.s_fraction(x2)

    return mtxt.pow_text(n, mtxt._(px1.get_str())) + mtxt.p0m1(bt_sign) + mtxt.pow_text(n, mtxt._(px.get_str()) + " = " + str(-ct)), \
        mtxt.f_t(x1n, x1d) + " и " + mtxt.f_t(x2n, x2d)

def reshi_uravnenie503():
# реши уравнение: 3t^2 - t - 2 = 0
    t1 = mrnd.rnd_w(-10, 10, [0])
    t2 = mrnd.rnd_w(-10, 10, [0, t1, -t1])
    p1 = pol.Polynomial([1, -t1], [1, 0])
    p2 = pol.Polynomial([1, -t2], [1, 0])
    p = pol.Polynomial.product(polynomials=(p1, p2))
    m = p.monomials[0]
    p.monomials[0] = p.monomials[2]
    p.monomials[2] = m
    return p.get_str() + " = 0", str(t1) + " и " + str(t2)

def dokazhi_tozhdestvo():
# докажи тождество: 3^(8x^2-6x-13) = 3 * (3^(4x^2 - 3x - 7))^2
    n, k1 = mrnd.common_base_power()
    p = pol.Polynomial([mrnd.rnd_w(-5, 5, [0]), mrnd.rnd_w(-5, 5, [0]), mrnd.rnd_w(-10, 10, [0])], [2, 1, 0])
    k = rnd.randint(2, 3)
    pr = pol.Polynomial.product(polynomials=(p, pol.Polynomial([k], [0])))
    pr.monomials[0].coefficient = pr.monomials[0].coefficient + k1
    return mtxt.pow_text(n, mtxt._(pr.get_str())) + " = " + str(pow(n, k1)) + mtxt.pow_text(mtxt._(mtxt.pow_text(n, mtxt._(p.get_str()))), k), ''

def chemu_ravno_a():
# чему равно a: 3^(x + 3) = a * 3^x
    n, k = mrnd.common_base_power()
    return mtxt.pow_text(str(n), mtxt._("x + " + str(k))) + " = a * " + mtxt.pow_text(n, "x"), "a = " + str(pow(n, k))

def vo_skolko_raz():
# во сколько раз: 3^(x + 3) больше чем 3^x?
    n, k = mrnd.common_base_power()
    return mtxt.pow_text(str(n), mtxt._("x + " + str(k))) + " больше чем " + mtxt.pow_text(n, "x"), "в " + str(pow(n, k)) + " раз"


def vyichisli_ploschad_pryamougolnika_esli_ego_perimetr_raven():
# Вычисли площадь прямоугольника, если его периметр равен: 30 см, а одна сторона больше другой на 1 см.
    a = rnd.randint(3, 7)
    b = a + rnd.randint(1, 4)
    return str(2 * (a + b)) + " см, а одна сторона больше другой на " + str(b - a), str(a * b) + " см^2"

def najdi_storonyi_pryamougolnika_esli_ego_perimetr_raven():
# найди стороны прямоугольника, если его периметр равен: 30 см, а одна сторона больше другой на 1 см.
    a = rnd.randint(3, 7)
    b = a + rnd.randint(1, 4)
    return str(2 * (a + b)) + " см, а одна сторона больше другой на " + str(b - a), str(a) + " см и " + str(b) + " см"

def vyichisli_perimetr_pryamougolnika_esli_odna_ego_storona_ravna():
# вычисли периметр прямоугольника, если одна его сторона равна: 4 см, а другая на 1 см больше первой
    a = rnd.randint(3, 7)
    b = a + rnd.randint(1, 4)
    return str(a) + " см, а другая на " + str(b - a) + " см больше первой", str(2 * (a + b)) + " см"

def vyichisli_perimter_pryamougolnika_esli_odna_storona_ravna():
# вычисли перимтер прямоугольника, если одна сторона равна: 4 см, а другая 5 см
    a = rnd.randint(3, 10)
    b = mrnd.rnd_w(3, 10, [a])
    return str(a) + " см, а другая " + str(b) + " см", str(2 * (a + b)) + " см"

def vyichisli_ploschad_pryamougolnika_esli_odna_storona_ravna():
# вычисли площадь прямоугольника, если одна сторона равна: 4 см, а другая 5 см
    a = rnd.randint(3, 10)
    b = mrnd.rnd_w(3, 10, [a])
    return str(a) + " см, а другая " + str(b) + " см", str(a * b) + " см^2"

def razdeli_chislo495():
# Раздели число 138 в отношении 18:5
    n1 = rnd.randint(5, 20)
    n2 = mrnd.rnd_w(5, 20, [n1])
    c = rnd.randint(3, 6)
    return str((n1 + n2) * c) + " в отношении " + str(n1) + ":" + str(n2), str(n1 * c) + " и " + str(n2 * c)

def nuzhno_razdelit():
# нужно разделить: 138 яблок на две кучи в отношении 18:5. На сколько частей будешь делить, чтобы потом объединить части в кучи?
    n1 = rnd.randint(5, 20)
    n2 = mrnd.rnd_w(5, 20, [n1])
    c = rnd.randint(3, 6)
    return str((n1 + n2) * c) + " яблок нужно разделить на две кучи в отношении " + str(n1) + ":" + str(n2) + ". На сколько частей будешь делить, чтобы потом объединить части в кучи? ", str(n1 + n2)

def skolko_yablok_v_kazhdoj_kuche_esli():
# сколько яблок в каждой куче если: 138 яблок разделили на 23 равных части. В одну кучу положили 18 частей, а оставшиеся 5 частей в другую кучу.
    n1 = rnd.randint(5, 20)
    n2 = mrnd.rnd_w(5, 20, [n1])
    c = rnd.randint(3, 6)
    return str((n1 + n2) * c) + " яблок разделили на " + str(n1 + n2) + " равных частей. В одну кучу положили " + str(n1) + " частей, а оставшиеся " + str(n2) + " частей в другую кучу", \
           str(n1 * c) + " и " + str(n2 * c)

def razdelili():
# разделили: 138 на 23 равные части. Чему равна каждая часть?
    n = rnd.randint(15, 35)
    c = rnd.randint(3, 6)
    return str(c * n) + " на " + str(n) + " равные части. Чему равна каждая часть?", str(c)

def najdite():
# Найдите: диаметр|радиус окружности, если ее радиус|диаметр равен 4 см 4 мм
    dano = rnd.randint(0, 1)
    v = 2 * rnd.randint(10, 30)
    return ("радиус" if dano == 0 else "диаметр") + " окружности, если ее " + ("радиус" if dano == 1 else "диаметр") + " равен " \
        + str(v // 10) + " см " + str(v % 10) + " мм" , str(2*v // 10) + " см " + str(2*v % 10) + " мм" if dano == 1 else \
        str(int(v/2) // 10) + " см " + str(int(v/2) % 10) + " мм"

def opredeli_skorost_poezda_i_zapolni_tablitsu():
# Определи скорость поезда и заполни таблицу:
# t, ч:    3, 8,   x, 1.2,  x |
# s, км: 225, x, 300,   x, 60
    count = rnd.randint(5, 7)
    speed = rnd.randint(1, 20) * 5 + 50
    ds = [rnd.randint(5, 16) for x in range(0, count)]
    hs = [rnd.randint(0, 1) for x in range(0, count)]
    pos0 = rnd.randint(0, count - 1)
    return "время, ч: " + ", ".join([str(x) if hs[i] == 0 or i == pos0 else "x" for i, x in enumerate(ds)]) + " | " \
        + "расстояние, км: " + ", ".join([str(x * speed) if hs[i] == 1 or i == pos0 else "x" for i, x in enumerate(ds)]), \
           str(speed) + " км/ч, " + ", ".join([str(x) for i, x in enumerate(ds)]) + " | " + ", ".join([str(x * speed) for i, x in enumerate(ds)])

def opredeli_skorost_poezda_esli():
# Определи скорость поезда, если: за 3 часа он проехал 450 км
    speed = rnd.randint(1, 20) * 5 + 50
    n = rnd.randint(3, 7)
    return "за " + str(n) + " часа он проехал " + str(n * speed), str(speed) + " км/ч"


def za_m_kg_konfet_zaplatitli_p_rub_po_tablitse_opredelite_skolko_stoit_1_kg_konfet_i_zapolni_tablitsu():
# За m кг конфет заплатитли p руб. По таблице определите сколько стоит 1 кг конфет и заполни таблицу:
# m, кг  :   3, 8,   x, 1.2,  x
# p, руб.: 225, x, 300,   x, 60
    count = rnd.randint(5, 7)
    kg = rnd.randint(1, 40) * 5 + 100
    ws = [rnd.randint(1, 12) for x in range(0, count)]
    hs = [rnd.randint(0, 1) for x in range(0, count)]
    pos0 = rnd.randint(0, count - 1)
    return "m, кг: " + ", ".join([str(x) if hs[i] == 0 or i == pos0 else "x" for i, x in enumerate(ws)]) + " | " \
        + "p. руб.: " + ", ".join([str(x * kg) if hs[i] == 1 or i == pos0 else "x" for i, x in enumerate(ws)]), \
           str(kg) + " руб., " + ", ".join([str(x) for i, x in enumerate(ws)]) + " | " + ", ".join([str(x * kg) for i, x in enumerate(ws)])


def opredeli_skolko_stoit_1_kg_konfet_esli():
# Определи сколько стоит 1 кг конфет, если: 3 кг стоят 450 руб.
    kg = rnd.randint(1, 20) * 5 + 20
    n = rnd.randint(3, 7)
    return str(n) + " кг стоят " + str(n * kg) + " руб.", str(kg) + " руб."

def predstavte_vyirazhenie_v_vide_zavisimosti_ot_aplusb_i_ot_ab():
    # докажите тождество: 2a^2-5ab+2b^2 = 2(a-b)^2 - ab
    s = rnd.randint(0, 1)
    f1 = rnd.choice([1, 2, 3, 5])
    f2 = mrnd.choice_w([1, 2, 3, 5], [f1])
    k = rnd.randint(2, 5)
    c = rnd.randint(1, 5)
    return mtxt.fc(pow(f1, 2) * k) + mtxt.pow_text("a", 2) + mtxt.p0m1(s) + mtxt.fc(
        f1 * f2 * 2 * k + (c if s == 1 else -c)) + "ab + " + mtxt.fc(pow(f2, 2) * k) + mtxt.pow_text("b", 2), \
           str(k) + mtxt.pow_text(mtxt._(mtxt.fc(f1) + "a" + mtxt.p0m1(s) + mtxt.fc(f2) + "b"), 2) + " - " + mtxt.fc(c) + "ab"

def najdi_znachenie_vyirazheniya():
# Найди значение выражения: 2a^2-5ab+2b^2 при a=k(6)+k(5) b=k(6)-k(5)
    s = rnd.randint(0, 1)
    f1 = rnd.choice([1, 2, 3, 5])
    f2 = mrnd.choice_w([1, 2, 3, 5], [f1])
    a = rnd.choice([1, 2, 3, 5, 6, 7, 8, 10])
    b = mrnd.choice_w([1, 2, 3, 5, 6, 7, 8, 10], [a])
    k = rnd.randint(2, 5)
    c = rnd.randint(1, 5)

    x, y = mf.s_fraction((a, pow(f1, 2)))
    a1 = mtxt.f_t(x, y)
    x, y = mf.s_fraction((a, pow(f2, 2)))
    a2 = mtxt.f_t(x, y)
    x, y = mf.s_fraction((b, pow(f1, 2)))
    b1 = mtxt.f_t(x, y)
    x, y = mf.s_fraction((b, pow(f2, 2)))
    b2 = mtxt.f_t(x, y)

    if s == 0:
        a_x, a_y = mf.s_fraction_sum((4 * k * a, 1), (-c * (a - b), f1 * f2))
    else:
        a_x, a_y = mf.s_fraction_sum((4 * k * b, 1), (-c * (a - b), f1 * f2))

    return mtxt.fc(pow(f1, 2) * k) + mtxt.pow_text("a", 2) + mtxt.p0m1(s) + mtxt.fc(f1 * f2 * 2 * k + (c if s == 1 else -c)) + "ab + " + mtxt.fc(pow(f2, 2) * k) + mtxt.pow_text("b", 2) + \
        ", при a = " + mtxt.k_t(a1) + " + " + mtxt.k_t(b1) + ", b = " + mtxt.k_t(a2) + " - " + mtxt.k_t(b2), \
        mtxt.f_t(a_x, a_y)


def vyichisli_znachenie_vyirazheniya483():
# вычисли значение выражения: 2(a-b)^2 - ab при a=k(6)+k(5) b=k(6)-k(5)
    s = rnd.randint(0, 1)
    f1 = rnd.choice([1, 2, 3, 5])
    f2 = mrnd.choice_w([1, 2, 3, 5], [f1])
    a = rnd.choice([1, 2, 3, 5, 6, 7, 8, 10])
    b = mrnd.choice_w([1, 2, 3, 5, 6, 7, 8, 10], [a])
    k = rnd.randint(2, 5)
    c = rnd.randint(1, 5)

    x, y = mf.s_fraction((a, pow(f1, 2)))
    a1 = mtxt.f_t(x, y)
    x, y = mf.s_fraction((a, pow(f2, 2)))
    a2 = mtxt.f_t(x, y)
    x, y = mf.s_fraction((b, pow(f1, 2)))
    b1 = mtxt.f_t(x, y)
    x, y = mf.s_fraction((b, pow(f2, 2)))
    b2 = mtxt.f_t(x, y)

    if s == 0:
        a_x, a_y = mf.s_fraction_sum((4 * k * a, 1), (-c * (a - b), f1 * f2))
    else:
        a_x, a_y = mf.s_fraction_sum((4 * k * b, 1), (c * (a - b), f1 * f2))

    return str(k) + mtxt.pow_text(mtxt._(mtxt.fc(f1) + "a" + mtxt.p0m1(s) + mtxt.fc(f2) + "b"), 2) + mtxt.p0m1(1-s) + mtxt.fc(c) + "ab" + ", при a = " + mtxt.k_t(a1) + " + " + mtxt.k_t(b1) \
           + ", b = " + mtxt.k_t(a2) + " - " + mtxt.k_t(b2), \
           mtxt.f_t(a_x, a_y)

def vyichisli_znachenie_vyirazheniya482():
# вычисли значение выражения: ab при a=k(6)+k(5) b=k(6)-k(5)

    f1 = rnd.choice([1, 2, 3, 5])
    f2 = mrnd.choice_w([1, 2, 3, 5], [f1])
    a = rnd.choice([1, 2, 3, 5, 6, 7, 8, 10])
    b = mrnd.choice_w([1, 2, 3, 5, 6, 7, 8, 10], [a])

    x, y = mf.s_fraction((a, pow(f1, 2)))
    a1 = mtxt.f_t(x, y)
    x, y = mf.s_fraction((a, pow(f2, 2)))
    a2 = mtxt.f_t(x, y)
    x, y = mf.s_fraction((b, pow(f1, 2)))
    b1 = mtxt.f_t(x, y)
    x, y = mf.s_fraction((b, pow(f2, 2)))
    b2 = mtxt.f_t(x, y)

    a_x, a_y = mf.s_fraction((a-b, f1*f2))

    return "a*b, при a = " + mtxt.k_t(a1) + " + " + mtxt.k_t(b1) + ", b = " + mtxt.k_t(a2) + " - " + mtxt.k_t(b2), \
       mtxt.f_t(a_x, a_y)

def vyichisli_znachenie_vyirazheniya():
# вычисли значение выражения: a - b при a=k(6)+k(5) b=k(6)-k(5)
    s = rnd.randint(0, 1)
    f1 = rnd.choice([1, 2, 3, 5])
    f2 = mrnd.choice_w([1, 2, 3, 5], [f1])
    a = rnd.choice([1, 2, 3, 5, 6, 7, 8, 10])
    b = mrnd.choice_w([1, 2, 3, 5, 6, 7, 8, 10], [a])

    x, y = mf.s_fraction((a, pow(f1, 2)))
    a1 = mtxt.f_t(x, y)
    x, y = mf.s_fraction((a, pow(f2, 2)))
    a2 = mtxt.f_t(x, y)
    x, y = mf.s_fraction((b, pow(f1, 2)))
    b1 = mtxt.f_t(x, y)
    x, y = mf.s_fraction((b, pow(f2, 2)))
    b2 = mtxt.f_t(x, y)

    return mtxt.fc(f1) + "a" + mtxt.p0m1(s) + mtxt.fc(f2) + "b, при a = " + mtxt.k_t(a1) + " + " + mtxt.k_t(b1) \
           + ", b = " + mtxt.k_t(a2) + " - " + mtxt.k_t(b2), \
           "2*" + mtxt.k_t(b if s == 1 else a)

def dokazhite_tozhdestvo480():
# докажите тождество: 2a^2-5ab+2b^2 = 2(a-b)^2 - ab
    s = rnd.randint(0, 1)
    f1 = rnd.choice([1, 2, 3, 5])
    f2 = mrnd.choice_w([1, 2, 3, 5], [f1])
    k = rnd.randint(2, 5)
    c = rnd.randint(1, 5)
    return mtxt.fc(pow(f1, 2) * k) + mtxt.pow_text("a", 2) + mtxt.p0m1(s) + mtxt.fc(f1 * f2 * 2 * k + (c if s == 1 else -c)) + "ab + " + mtxt.fc(pow(f2, 2) * k) + mtxt.pow_text("b", 2) + \
        " = " + mtxt.fc(k) + mtxt._(mtxt.fc(f1) + "a" + mtxt.p0m1(s) + mtxt.fc(f2) + "b") + "^2 - " + mtxt.fc(c) + "ab", ''

def reshi_uravnenie479():
# Реши уравнение: log1/3->(x + 12) = -2
    n, k = mrnd.common_base_power()
    s = rnd.randint(0, 1)
    log_s = rnd.randint(0, 1)
    a = rnd.randint(1, 20)
    log_base_str = "1/" + str(n) if s == 1 else str(n)

    return mtxt.log_text(log_base_str, mtxt._("x" + mtxt.p0m1(log_s) + str(a))) + " = " + ("-" if s == 1 else "") + str(k) ,\
           'x = ' + str(pow(n, k) + (-a if log_s == 0 else a))

def reshi_uravnenie478():
# реши уравнение: log2->x = 3
    n, k = mrnd.common_base_power()
    return mtxt.log_text(n, "x") + " = " + str(k), str(pow(n, k))

def chto_poluchitsya_esli_vozvesti():
# что получится если возвести: 3 в 2-ю степень // k = [1, 3]
    n, k = mrnd.common_base_power()
    return str(n) + " в " + str(k) + " степень", str(pow(n, k))

def razlozhit_na_mnozhiteli476():
# Разложить на множители: 2ab+3ak(a)+4bk(b)+6k(ab)
    cs = rnd.randint(0, 1)
    gs = rnd.randint(0, 1)

    fc1 = rnd.choice([1, 2, 3, 5, 7])
    fc2 = mrnd.choice_w([1, 2, 3, 5, 7], [fc1])
    acp = rnd.randint(1, 3)
    bcp = rnd.randint(1, 3)

    f1 = rnd.randint(1, 7)
    f2 = mrnd.rnd_w(1, 7, [f1])
    a1p = rnd.randint(1, 3)
    b1p = rnd.randint(1, 3)
    a2p = rnd.randint(1, 3)
    b2p = rnd.randint(1, 3)

    def get_term(f, ap, bp):
        return mtxt.fc(f) + mtxt.get_k("a", ap) + mtxt.get_k("b", bp)

    def get_common_str():
        return mtxt._(get_term(fc1, acp, 0) + mtxt.p0m1(cs) + get_term(fc2, 0, bcp))

    return get_term(f1 * fc1, a1p + acp, b1p) + mtxt.p0m1(cs) + get_term(f1 * fc2, a1p, b1p + bcp) + \
        mtxt.p0m1(gs) + get_term(f2 * fc1, a2p + acp, b2p) + mtxt.p0m1(0 if cs == gs else 1) + get_term(f2 * fc2, a2p, bcp + b2p), \
        get_common_str() + mtxt._(get_term(f1, a1p, b1p) + mtxt.p0m1(gs) + get_term(f2, a2p, b2p))

def vyinesi_obschij_mnozhitel475():
# вынеси общий множитель: 3a(2a - k(b)) - k(b)(2a - k(b))
    cs = rnd.randint(0, 1)
    gs = rnd.randint(0, 1)

    fc1 = rnd.choice([1, 2, 3, 5, 7])
    fc2 = mrnd.choice_w([1, 2, 3, 5, 7], [fc1])
    acp = rnd.randint(1, 3)
    bcp = rnd.randint(1, 3)

    f1 = rnd.randint(1, 7)
    f2 = mrnd.rnd_w(1, 7, [f1])
    a1p = rnd.randint(1, 3)
    b1p = rnd.randint(1, 3)
    a2p = rnd.randint(1, 3)
    b2p = rnd.randint(1, 3)

    def get_term(f, ap, bp):
        return mtxt.fc(f) + mtxt.get_k("a", ap) + mtxt.get_k("b", bp)

    def get_common_str():
        return mtxt._(get_term(fc1, acp, 0) + mtxt.p0m1(cs) + get_term(fc2, 0, bcp))

    return get_term(f1, a1p, b1p) + get_common_str() + mtxt.p0m1(gs) + get_term(f2, a2p, b2p) + get_common_str(),\
           get_common_str() + mtxt._(get_term(f1, a1p, b1p) + mtxt.p0m1(gs) + get_term(f2, a2p, b2p))

def vyinesi_obschij_mnozhitel():
# вынеси общий множитель: 2ab + 4ak(b)
    common_factor = rnd.randint(1, 7)
    f1 = rnd.choice([1, 2, 3, 5, 7])
    f2 = mrnd.choice_w([1, 2, 3, 5, 7], [f1])
    apk = rnd.randint(1, 3)
    bpk = rnd.randint(1, 3)
    acpk = mrnd.rnd_w(1, 4 - apk)
    bcpk = mrnd.rnd_w(1, 4 - bpk)
    s = rnd.randint(0, 1)

    return mtxt.fc(common_factor * f1) + mtxt.get_k("a", apk + acpk) + mtxt.get_k("b", bcpk) + mtxt.p0m1(s) + \
           mtxt.fc(common_factor * f2) + mtxt.get_k("a", acpk) + mtxt.get_k("b", bpk + bcpk), \
        mtxt.fc(common_factor) + mtxt.get_k("a", acpk) + mtxt.get_k("b", bcpk) + \
           mtxt._(mtxt.fc(f1) + mtxt.get_k("a", apk) + mtxt.p0m1(s) + mtxt.fc(f2) + mtxt.get_k("b", bpk))

def ploschad_koltsa_ravna_ploschad_vneshnego_kruga_minus_ploschad_vnutrennego_kruga_poschitaj_ploschad_koltsa_esli():
    r1 = rnd.randint(2, 7)
    r2 = rnd.randint(r1 + 1, 9)
    pi = 3.14
    return "радиус внешнего круга равен 1/" + str(r1) + " см, а внутреннего 1/" + str(r2), \
           format(pi * (pow(1 / r1, 2) - pow(1 / r2, 2)), '.2f') + " см^2"


def poschitaj_ploschad_kruga_esli_radius_raven():
    r = rnd.randint(2, 9)
    pi = 3.14
    return "радиус круга равен 1/" + str(r) + " см", format(pi * pow(1/r, 2), '.2f') + " см^2"


def ploschad_kruga_vyichislyaetsya_po_fromule_pi__r2_poschitaj_ploschad_kruga_esli_pi_ravno_314_i():
    r = rnd.randint(2, 9)
    pi = 3.14
    return "радиус круга равен " + str(r) + " см", format(pi * pow(r, 2), '.2f') + " см^2"

def vyichisli():
# вычисли: -3 * (-2/3)^3 + (1/3)^2
    d = rnd.choice([2, 3, 5])

    terms_count = rnd.randint(2, 3)
    terms = []
    for i in range(0, terms_count):
        n = rnd.choice([2, 3, 4, 5])
        # s1, a, s2, n, d, k
        terms.append((rnd.randint(0, 1), rnd.randint(2, 7), rnd.randint(0, 1), mrnd.rnd_w(2, 5, [d]), d, rnd.randint(2, 4)))

    def get_term_text(t, is_first=False):
        s1, a, s2, n, d, k = t
        return (("-" if is_first else " - ") if s1 == 1 else (" + " if not is_first else "")) + mtxt.fc(a) + "*" + \
               mtxt.pow_text(mtxt._(("-" if s2 == 1 else "") + mtxt.f_t(n, d)), k)

    def get_term_value(t):
        s1, a, s2, n, d, k = t


        return mf.s_fraction((pow(n, k) * a * pow(-1, (pow(-s2, k) + pow(-s1, 1)) % 2), pow(d, k)))

    def get_exp_value():
        r_n = 0
        r_d = 1
        for t in terms:
            n, d = get_term_value(t)
            r_n, r_d = mf.s_fraction((n * r_d + r_n * d, r_d * d))
        return r_n, r_d

    text = ""
    for t in terms:
        text += get_term_text(t, terms.index(t) == 0)

    answer_n, answer_d = get_exp_value()

    return text, mtxt.f_t(answer_n, answer_d)

def skolko_budet469():
#  сколько будет (-1/3)^3
    a = rnd.randint(2, 5)
    n = rnd.randint(3, 5)
    return mtxt.pow_text(mtxt._("-1/" + str(a)), n), ("-" if n % 2 != 0 else "") + "1/" + str(pow(a, n))

def skolko_budet468():
# сколько будет: (1/3)^3
    a = rnd.randint(2, 5)
    n = rnd.randint(3, 5)
    return mtxt.pow_text(mtxt._("1/" + str(a)), n), "1/" + str(pow(a, n))


def skolko_budet467():
# сколько будет: 3^3
    a = rnd.randint(2, 5)
    n = rnd.randint(3, 5)
    return mtxt.pow_text(a, n), str(pow(a, n))

def skolko_budet466():
# сколько будет: 3 * 3 * 3
    a = rnd.randint(2, 5)
    n = rnd.randint(3, 5)
    return mtxt.mp(str(a), n), str(pow(a, n))

def skolko_budet():
# сколько будет: 3 умножить само на себя 3 раза
    a = rnd.randint(2, 5)
    n = rnd.randint(3, 5)
    return str(a) + " умножить само на себя " + str(n) + " раз", str(pow(a, n))


def predstav464():
# Представь: 2^30 в виде степени с основанием 2^10
    a = rnd.choice([2, 3, 4, 5])
    n1 = rnd.randint(2, 10)
    n2 = rnd.randint(2, 10)
    return mtxt.pow_text(a, n1 * n2) + " в виде степени с основанием " + mtxt.pow_text(a, n1), \
           mtxt.pow_text(mtxt._(mtxt.pow_text(a, n1)) , n2)

def chemu_raven_x_v_uravnenii():
# чему равен x в уравнении [a^40 = (a^20)^x]
    x = rnd.randint(3, 20)
    n = rnd.randint(3, 20)
    return mtxt.pow_text("a", x * n) + " = " + mtxt.pow_text(mtxt._(mtxt.pow_text("a", n)), "x"), str(x)

def predstav462():
    a = rnd.choice([2, 3, 4, 5, 6, 7])
    n1 = rnd.randint(2, 4)
    n2 = rnd.randint(2, 7)
    return mtxt.pow_text(pow(a, n1), n2) + " в виде степени с основанием " + str(a), mtxt.pow_text(a, n1 * n2)

def predstav461():
    a = rnd.choice([2, 3, 4, 5, 6, 7])
    n1 = rnd.randint(2, 4)
    n2 = rnd.randint(2, 7)
    return mtxt.pow_text(mtxt._(mtxt.pow_text(a, n1)), n2) + " в виде степени с основанием " + str(a), mtxt.pow_text(a, n1 * n2)

def predstav460():
    a = rnd.choice([2, 3, 4, 5, 6, 7])
    n1 = rnd.randint(2, 4)
    return str(pow(a, n1)) + " в виде степени с основанием " + str(a), mtxt.pow_text(a, n1)


def uprosti459():
    n1 = rnd.randint(3, 8)
    n2 = rnd.randint(1, n1 - 1)
    n3 = rnd.randint(2, 7)
    n4 = rnd.randint(2, (n1 + n2)*n3 - 1)
    return mtxt.pow_text(mtxt._(mtxt.pow_text("a", n1) + "*" + mtxt.pow_text("a", n2)), n3) + "/" + \
           mtxt._(mtxt.pow_text("a", n4)), mtxt.pow_text("a", (n1 + n2) * n3 - n4)

def uprosti458():
    n1 = rnd.randint(3, 8)
    n2 = rnd.randint(1, n1 - 1)
    n3 = rnd.randint(2, 7)
    return mtxt.pow_text(mtxt._(mtxt.pow_text("a", n1) + "*" + mtxt.pow_text("a", n2)), n3), mtxt.pow_text(
        "a", (n1 + n2) *n3)

def uprosti457():
    n1 = rnd.randint(3, 8)
    n2 = rnd.randint(1, n1 - 1)
    n3 = rnd.randint(1, n1 + n2 - 1)
    return mtxt.pow_text("a", n1) + "*" + mtxt.pow_text("a", n2) + "/" + mtxt._(mtxt.pow_text("a", n3)), mtxt.pow_text("a", n1 + n2 - n3)


def uprosti456():
    n1 = rnd.randint(3, 8)
    n2 = rnd.randint(1, n1 - 1)
    return mtxt.pow_text("a", n1) + "/" + mtxt._(mtxt.pow_text("a", n2)), mtxt.pow_text("a", n1 - n2)

def uprosti455():
    n1 = rnd.randint(3, 8)
    n2 = rnd.randint(1, n1 - 1)
    return mtxt.pow_text("a", n1) + "/" + mtxt._(mtxt.mp("a", n2)), mtxt.pow_text("a", n1 - n2)

def uprosti454():
    n1 = rnd.randint(3, 8)
    n2 = rnd.randint(1, n1 - 1)
    return mtxt.mp("a", n1) + "/" + mtxt._(mtxt.mp("a", n2)), mtxt.pow_text("a", n1 - n2)

def uprosti453():
    n1 = rnd.randint(2, 7)
    n2 = mrnd.rnd_w(2, 7, [n1])
    n3 = rnd.randint(2, 5)
    return mtxt.pow_text("a", n1) + "*" + mtxt.pow_text("a", n2) + "*" + mtxt.pow_text("a", n3), mtxt.pow_text("a",
                                                                                                        n1 + n2 + n3)

def uprosti452():
    n1 = rnd.randint(2, 7)
    n2 = mrnd.rnd_w(2, 7, [n1])
    c = rnd.randint(2, 5)
    return mtxt.pow_text("a", n1) + "*" + mtxt.pow_text("a", n2) + "*" + mtxt.mp("a", c), mtxt.pow_text("a", n1 + n2 + c)

def uprosti451():
    n1 = rnd.randint(2, 7)
    n2 = mrnd.rnd_w(2, 7, [n1])
    return mtxt.pow_text("a", n1) + "*" + mtxt.pow_text("a", n2), mtxt.pow_text("a", n1 + n2)

def uprosti450():
    c = rnd.randint(2, 5)
    n = rnd.randint(2, 4)
    return mtxt.pow_text("a", n) + "*" + mtxt.mp("a", c), mtxt.pow_text("a", c + n)

def uprosti449():
    c = rnd.randint(3, 7)
    return mtxt.mp("a", c), mtxt.pow_text("a", c)


def uprosti448():
# упрости: (4x)/(2k(x) - k(y)) : (12xk(x)/(4x-y) : (2x)/(6x-3k(xy))
    k1 = rnd.choice([1, 2, 3])
    k2 = mrnd.choice_w([1, 2, 3], [k1])
    s = rnd.randint(0, 1)

    o_pos = rnd.randint(0, 5)
    o2_pos = rnd.randint(0, 2) if o_pos in [3, 4, 5] else rnd.randint(3, 5)
    osh_pos = mrnd.rnd_w(0, 2, [o2_pos]) if o2_pos in [0, 1, 2] else mrnd.rnd_w(3, 5, [o2_pos])

    m = rnd.choice([2, 3, 5])
    mx = rnd.randint(1, 3)
    my = rnd.randint(1, 3)

    a = rnd.choice([2, 3, 5, 7])
    b = mrnd.choice_w([2, 3, 5, 7], [a])
    a_pos_possible = {0, 1, 2}.difference({o2_pos, osh_pos}) if osh_pos in [0, 1, 2] else {3, 4, 5}.difference({o2_pos, osh_pos})
    a_pos = rnd.choice(list(a_pos_possible))
    b_pos_possible = {3, 4, 5}.difference({o_pos}) if o_pos in [3, 4, 5] else {0, 1, 2}.difference({o_pos})
    b_pos = rnd.choice(list(b_pos_possible))

    xy = rnd.randint(0, 1)
    if xy == 0:
        ma = rnd.randint(0, mx - 1)
        mb = mx - ma
    else:
        ma = rnd.randint(0, my - 1)
        mb = my - ma

    xy_pos_possible = {0, 1, 2}.difference({b_pos, o_pos}) if o_pos in [0, 1, 2] else {3, 4, 5}.difference({b_pos, o_pos})
    xy_pos = rnd.choice(list(xy_pos_possible))

    a2 = rnd.randint(0, 1)
    a3 = rnd.randint(0, 1)

    t = ['', '', '', '', '', '']

    xys = "x" if xy == 0 else "y"

    def get_o_text(br=True):
        res = mtxt.fc(k1) + mtxt.k_t("x") + mtxt.p0m1(s) + mtxt.fc(k2) + mtxt.k_t("y")
        return res if not br else mtxt._(res)

    def get_k(symb, p):
        if p == 0:
            return ""
        if p == 1:
            return mtxt.k_t(symb)
        if p == 2:
            return symb
        if p == 3:
            return symb + mtxt.k_t(symb)
        if p == 4:
            return mtxt.pow_text(symb, 2)

    def get_k2(symb1, symb2, p1, p2):
        res = ""
        c = 0
        if (p1 % 2 != 0) and (p2 % 2 != 0):
            res = mtxt.k_t(symb1 + symb2)
            c = 1
        res = get_k(symb1, p1 - c) + get_k(symb2, p2 - c) + res
        return res

    def get_om_text(br=True):
        res = mtxt.fc(k1 * m) + get_k2("x", "y", 1 + mx, my) + mtxt.p0m1(s) + mtxt.fc(k2 * m) + get_k2("x", "y", mx, my + 1)
        return res if not br else mtxt._(res)

    def get_osh_text(br=True):
        return mtxt._(mtxt.fc(pow(k1, 2)) + "x" + " - " + mtxt.fc(pow(k2, 2)) + "y")

    t[a_pos] = str(a)
    t[b_pos] = (str(b) if mb == 0 or b != 1 else "") + get_k(xys, mb)
    t[o_pos] = get_o_text()
    t[o2_pos] = get_om_text()
    t[xy_pos] = "1" if ma == 0 else get_k(xys, ma)
    t[osh_pos] = get_osh_text()

    answer = ""
    if o_pos in [3, 4, 5]:
        n, d = mf.s_fraction((a * m, b))
        answer = mtxt.f_t(n, d) + "*" + get_osh_text() + (get_k("y", my) if xy == 0 else get_k("x", mx))
    else:
        n, d = mf.s_fraction((b, a * m))
        answer = mtxt.f_t(b, mtxt._(str(a * m) + get_osh_text() + (get_k("y", my) if xy == 0 else get_k("x", mx))))

    # return str({"o": o_pos, "o2": o2_pos, "osh": osh_pos, "a": a_pos, "b": b_pos, "xy": xy_pos}), ""

    return t[0] + "/" + t[3] + (" * " if a2 == 0 else " : ") + (t[1] + "/" + t[4] if a2 == 0 else t[4] + "/" + t[1]) + \
           (" * " if a3 == 0 else " : ") + (t[2] + "/" + t[5] if a3 == 0 else t[5] + "/" + t[2]), answer

def uprosti():
# упрости: (a - 4b)/(k(a) - 2k(b)) // произвольный коэффициенты
    k1 = rnd.choice([1, 2, 3, 5, 7, 8])
    k2 = mrnd.choice_w([1, 2, 3, 5, 7, 8], [k1])
    s = rnd.randint(0, 1)

    def get_f_text(ch1, f1, ch2, f2, sign):
        return mtxt._(mtxt.k_t(mtxt.fc(f1) + ch1) + mtxt.p0m1(sign) + mtxt.k_t(mtxt.fc(f2) + ch2))

    return mtxt._(mtxt.fc(k1) + "a" + " - " + mtxt.fc(k2) + "b") + "/" + get_f_text("a", k1, "b", k2, s), \
           get_f_text("a", k1, "b", k2, 1-s)

def vyinesi_obschij_mnozhitel_za_skobku():
    n = rnd.choice([1, 2, 3, 5, 7])
    k1 = mrnd.choice_w([1, 2, 3, 5, 7, 9], [n])
    k2 = mrnd.choice_w([1, 2, 3, 5, 7, 9], [n, k1])

    # coeff, sign, a^, k(a), b^, k(b)
    t1p = (n * k1, rnd.randint(0, 1), rnd.randint(0, 5), rnd.randint(0, 1), rnd.randint(0, 5), rnd.randint(0, 1))
    t2p = (n * k2, rnd.randint(0, 1), mrnd.rnd_w(0, 5, [t1p[2]]), rnd.randint(0, 1), mrnd.rnd_w(0, 5, [t1p[4]]), rnd.randint(0, 1))

    def get_term_text(term, space=False):
        c, s, ap, akp, bp, bkp = term
        if c == 1 and ap == 0 and akp == 1 and bp == 0 and bkp == 1:
            return ("" if s == 0 else "-") + "1"

        return ("" if s == 0 else ("-" if not space else " - ")) + mtxt.fc(c) + (mtxt.pow_text("a", ap) if ap != 0 else "") + (mtxt.k_t("a", 2) if akp == 0 else "") + \
               (mtxt.pow_text("b", bp) if bp != 0 else "") + (mtxt.k_t("b", 2) if bkp == 0 else "")

    def get_param_sub(t1, t2):
        c1, s1, ap1, akp1, bp1, bkp1 = t1
        c2, s2, ap2, akp2, bp2, bkp2 = t2

        c = int(c1/c2)
        s = s1 if s2 == 0 else 1 - s1
        ap = ap1 - ap2
        bp = bp1 - bp2
        akp = akp1 if akp2 == 1 else 1
        bkp = bkp1 if bkp2 == 1 else 1

        return c, s, ap, akp, bp, bkp

    atpf = (n, 1 if (t1p[1] == 1 and t2p[1] == 1) else 0, min(t1p[2], t2p[2]), 0 if (t1p[3] == 0 and t2p[3] == 0) else 1,
           min(t1p[4], t2p[4]), 0 if (t1p[5] == 0 and t2p[5] == 0) else 1)

    atp1 = get_param_sub(t1p, atpf)
    atp2 = get_param_sub(t2p, atpf)

    return get_term_text(t1p) + (" + " if t2p[1] == 0 else "") + get_term_text(t2p, True) , get_term_text(atpf) + " * " + \
           mtxt._(get_term_text(atp1) + (" + " if atp2[1] == 0 else "") + get_term_text(atp2, True))

def postroj_v_odnoj_sisteme_koordinat_grafiki_funktsij445():
    # Построй в одной системе координат графики функций:  y = x^-2, y = x^-3 и y = x^-4
    k_min = 2 * rnd.randint(1, 4)

    return "y=x^-" + str(k_min) + ", y=x^-" + str(k_min + 1) + " и y=x^-" + str(k_min + 2), ''

def kakovyi_oblast_opredelenij_i_oblast_znachenij_funktsii444():
    # каковы область определений и область значений функции y = x^-3 (n=[0, 10])
    k = rnd.randint(2, 9)
    return "y=x^-" + str(k), \
           "область определения: вся числовая ось, область значений: " + (
           "любое число" if k % 2 != 0 else "[0, +oo]")

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
    # какая из функции быстрее: убывает|возрастает на отрезке (-oo, -1) | (-1, 0) | (0, 1) | (1, +oo) y = x^-2 или x^-4
    uc = rnd.randint(0, 3)
    uv = rnd.randint(0, 1)
    k1 = rnd.randint(2, 9)
    k2 = mrnd.rnd_w(2, 9, [k1])

    if uc == 0:
        ucs = "(-oo, -1)"
    if uc == 1:
        ucs = "(-1, 0)"
    if uc == 2:
        ucs = "(0, 1)"
    if uc == 3:
        ucs = "(1, +oo)"

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
# y = x^-3 на участке (-oo, -1) | (-1, 0) | (0, 1) | (1, +oo)
    uc = rnd.randint(0, 3)
    k = rnd.randint(2, 9)

    if uc == 0:
        ucs = "(-oo, -1)"
    if uc == 1:
        ucs = "(-1, 0)"
    if uc == 2:
        ucs = "(0, 1)"
    if uc == 3:
        ucs = "(1, +oo)"

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
           "область определения: вся числовая ось, область значений: " + ("любое число" if k % 2 != 0 else "[0, +oo]")

def postroj_v_odnoj_sisteme_koordinat_grafiki_funktsij():
# построй в одной системе координат графики функции y = x^2 и y = x^4
    k1 = rnd.randint(1, 4)
    k2 = mrnd.rnd_w(1, 4, [k1])
    return "построй в одной системе координат графики функций: y=x^" + str(k1 * 2) + " и y=x^" + str(k2 * 2), ''

def kakaya_iz_funktsii_lezhit446():
# какая из функции быстрее: убывает|возрастает на отрезке (-oo, -1) | (-1, 0) | (0, 1) | (1, +oo) y = x^2 или x^4
    uc = rnd.randint(0, 3)
    uv = rnd.randint(0, 1)
    k1 = rnd.randint(2, 9)
    k2 = mrnd.rnd_w(2, 9, [k1])

    if uc == 0:
        ucs = "(-oo, -1)"
    if uc == 1:
        ucs = "(-1, 0)"
    if uc == 2:
        ucs = "(0, 1)"
    if uc == 3:
        ucs = "(1, +oo)"

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
# y = x^3 на участке (-oo, -1) | (-1, 0) | (0, 1) | (1, +oo)
    uc = rnd.randint(0, 3)
    k = rnd.randint(2, 9)

    if uc == 0:
        ucs = "(-oo, -1)"
    if uc == 1:
        ucs = "(-1, 0)"
    if uc == 2:
        ucs = "(0, 1)"
    if uc == 3:
        ucs = "(1, +oo)"

    if k % 2 == 0:
        answer = "возрастает " if uc in [2, 3] else "убывает"
    else:
        answer = "возрастает " if uc in [0, 1, 2, 3] else "убывает"

    return "y=x^" + str(k) + " на участке " + ucs, answer

def ne_vyipolnyaya_postroenij_najdite_tochku_peresecheniya_grafikov_linejnoj_funktsii474():
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
    t3s = mtxt.f_t("2" + mtxt.k_t(mtxt.fc(k1*k2) + "ab"), mtxt._(mtxt.fc(k2) + "b" + "-" + mtxt.fc(k1) + "a"))

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


def dana_funktsiya_v_kakoj_tochki_grafik_peresekaet_os474():
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
    x2 = x1 + l
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