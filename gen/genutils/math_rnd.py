import random as rnd

def common_base_power():
    n = rnd.randint(2, 10)
    if n in [6, 7, 8, 9, 10]:
        k = 2
    if n in [3, 4, 5]:
        k = rnd.randint(2, 3)
    if n in [2, 3]:
        k = rnd.randint(2, 5)
    if n in [2]:
        k = rnd.randint(2, 10)
    return n, k

def rnd_w0(min, max):
    return rnd.choice(list(range(min, 0)) + list(range(1, max + 1)))

def rnd_w(min, max, exc=[]):
    ch = list(range(min, max + 1))
    return choice_w(ch, exc)

def choice_w(choices, exc=[]):
    ch = choices
    for e in exc:
        if e in ch:
            ch.remove(e)
    return rnd.choice(ch)

def quad_pol_by_rcount(count):
    if count == 0:
        b = rnd.choice([-7, -5, -3, -2, -1, 1, 2, 3, 5, 7])* rnd.choice([-1, 1])
        a = rnd.randint(3, 7)
        c = int(pow(b, 2) / (4 * a)) + rnd.randint(2, 5)
    if count == 1:
        c1 = rnd.choice([1, 2, 3, 5])
        c2 = choice_w([1, 2, 3, 5], [c1])
        b = 2 * c1 * c2 * rnd.choice([-1, 1])
        a = 1
        c = 1
        for ci in [c1, c2, c1, c2]:
            if rnd.randint(0, 1) == 0:
                a *= ci
            else:
                c *= ci
        if rnd.randint(0, 1) == 0:
            a = -a
            c = -c
    if count == 2:
        b = rnd.choice([-7, -5, -3, -2, 1, 1, 2, 3, 5, 7]) * rnd.choice([-1, 1])
        a = rnd.randint(3, 7)
        c = int(pow(b, 2) / (4 * a)) - rnd.randint(2, 5)

    return a, b, c


mns = ['положительные', 'отрицательные', 'неположительные', 'неотрицательные']

def get_ch_mn(m):
        s = (-1 if m in ['отрицательные', 'неположительные'] else 1)

        if rnd.randint(0, 4) == 0 and m in ['неположительные', 'неотрицательные']:
            return "0",  ['неположительные', 'неотрицательные']

        at = [m]
        if m == 'отрицательные':
            at.append('неположительные')
        if m == 'положительные':
            at.append('неотрицательные')
        if m == 'неположительные':
            at.append('отрицательные')
        if m == 'неотрицательные':
           at.append('положительные')

        t = rnd.randint(1, 3)
        if t == 1:
            return str(rnd.randint(1, 100) * s), at
        if t == 2:
            return str(rnd.randint(1, 100) * s) + "/" + str(rnd.choice([11, 13, 17, 19, 23])), at
        if t == 3:
            return str(rnd.randint(11, 99)/10 * s), at
